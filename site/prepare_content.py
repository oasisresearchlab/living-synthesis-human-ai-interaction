"""Build Quartz's content/ folder from the vault, without touching the vault itself.

  python3 site/prepare_content.py <vault-dir> <content-dir>

- copies the publishable parts of the vault
- adds the site home page (site/index.md)
- adds a "Relations" section to each node from relations.json (Quartz can't read it)
- puts an "AI draft, not yet reviewed" banner on nodes with NodeFormality: ai-draft
- drops embeds of files that aren't published (e.g. git-ignored videos)
"""
import json, os, re, shutil, sys
from collections import defaultdict

vault, out = (os.path.abspath(p) for p in sys.argv[1:3])
SKIP = {".git", ".github", ".obsidian", "site", "Meta", "relations.json", "Welcome.md",
        "student-pseudonyms.csv", ".gitignore", ".DS_Store", ".trash"}
VIDEO = (".mp4", ".m4v", ".mov", ".webm")

if os.path.exists(out):
    shutil.rmtree(out)
shutil.copytree(vault, out, ignore=lambda d, names: [
    n for n in names if (d == vault and n in SKIP) or n == ".DS_Store" or n.lower().endswith(VIDEO)])
shutil.copy(os.path.join(vault, "site", "index.md"), os.path.join(out, "index.md"))

# ---- node index ----
dg = os.path.join(out, "Discourse Graph")
nodes = {}  # path -> (name, text)
by_iid = {}
for root, _, files in os.walk(dg):
    for f in files:
        if f.endswith(".md"):
            p = os.path.join(root, f)
            s = open(p, encoding="utf-8").read()
            nodes[p] = s
            m = re.search(r"^nodeInstanceId: (\S+)", s, re.M)
            if m:
                by_iid[m.group(1)] = f[:-3]

cfg = json.load(open(os.path.join(vault, ".obsidian/plugins/discourse-graphs/data.json")))
rtype = {r["id"]: (r["label"], r["complement"]) for r in cfg["relationTypes"]}
rels = json.load(open(os.path.join(vault, "relations.json")))["relations"].values()
lines = defaultdict(list)
for r in rels:
    s, d = by_iid.get(r["source"]), by_iid.get(r["destination"])
    if not (s and d and r["type"] in rtype):
        continue
    label, comp = rtype[r["type"]]
    lines[s].append((label, d))
    lines[d].append((comp, s))

published = set()
for root, _, files in os.walk(out):
    for f in files:
        published.add(f)
        published.add(f[:-3] if f.endswith(".md") else f)

def drop_missing_video(m):
    target = m.group(1).split("|")[0]
    if target.lower().endswith(VIDEO) and target not in published:
        return "*(A video was embedded here; it isn't included in the published site.)*"
    return m.group(0)

n_rel = n_draft = 0
for p, s in nodes.items():
    name = os.path.basename(p)[:-3]
    fm_end = s.find("\n---", 4) + 4 if s.startswith("---\n") else 0
    fm, body = s[:fm_end], s[fm_end:]
    body = re.sub(r"!\[\[([^\]]+)\]\]", drop_missing_video, body)
    if re.search(r"^NodeFormality: ai-draft", fm, re.M):
        src = re.search(r'^extractedFrom: "?(\[\[.+?\]\])"?', fm, re.M)
        where = f" from {src.group(1)}" if src else ""
        body = ("\n> [!warning] AI draft, not yet reviewed\n"
                f"> Claude extracted this node{where}. It hasn't been reviewed yet, "
                "so treat it as a lead rather than a settled part of the synthesis.\n" + body)
        n_draft += 1
    if lines.get(name):
        rel_md = "\n\n## Relations\n" + "\n".join(
            f"- {lab} [[{other}]]" for lab, other in sorted(lines[name]))
        body = body.rstrip() + rel_md + "\n"
        n_rel += 1
    open(p, "w", encoding="utf-8").write(fm + body)

print(f"content: {len(nodes)} nodes, {n_draft} ai-draft banners, {n_rel} nodes with relations -> {out}")
