"""Color graph nodes by discourse node type (the Graph plugin has no option for this).

  python3 site/patch_graph.py <quartz-dir>

Patches the node-color function in @quartz-community/graph. Fails loudly if the plugin's
code has changed, so an upgrade can't silently drop the colors.
"""
import os, sys

quartz = sys.argv[1]
ORIG = 'function $e(a){var D=a.id===g;return D?Ge:K.has(a.id)||a.id.startsWith("tags/")?Qu:ue}'
# Colors match the Discourse Graph plugin's node types (and the vault's Obsidian graph).
COLORS = {"Questions": "#99890e", "Claims": "#7DA13E", "Evidence": "#DB134A", "Patterns": "#4fdb33",
          "Artifacts": "#e87d7d", "Theories": "#808080", "Sources": "#cdc1c1"}
# Quartz slugs are lowercase, e.g. "discourse-graph/claims/clm---...".
table = ",".join(f'"discourse-graph/{k.lower()}/":"{v}"' for k, v in COLORS.items())
NEW = ('function $e(a){if(a.id===g)return Ge;var T={' + table + '};'
       'for(var k in T)if(a.id.startsWith(k))return T[k];'
       'return K.has(a.id)||a.id.startsWith("tags/")?Qu:ue}')

dist = os.path.join(quartz, "node_modules/@quartz-community/graph/dist")
patched = 0
for f in ("index.js", "components/index.js"):
    p = os.path.join(dist, f)
    s = open(p, encoding="utf-8").read()
    if NEW in s:
        patched += 1
        continue
    if s.count(ORIG) != 1:
        sys.exit(f"patch_graph: expected exactly one color function in {p}; the graph plugin changed")
    open(p, "w", encoding="utf-8").write(s.replace(ORIG, NEW))
    patched += 1
print(f"patch_graph: colored nodes by type in {patched} files")
