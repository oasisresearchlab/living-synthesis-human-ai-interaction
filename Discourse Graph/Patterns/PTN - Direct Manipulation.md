---
nodeTypeId: node_VnAbDK_IqWL3QAteAd_FY
nodeInstanceId: 01a20e70-661f-708f-b844-134555c5db73
NodeFormality: draft
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/1lyO9GePS
roamAuthor: "Joel Chan"
created: 2024-02-07
---

## Description/Intuition and Key Sources
> [!info] What is the key intuition for the pattern? Include links to key/canonical sources.

Claude:
> Canonical source: Hutchins, E. L., Hollan, J. D., & Norman, D. A. (1985). Direct Manipulation Interfaces. *Human–Computer Interaction*, 1(4), 311–338. https://doi.org/10.1207/s15327051hci0104_2 (Joel Chan, SP-24 notes on [[@jiangGraphologueExploringLarge2023]], where the concept explains why linear chat is a poor medium for controlling intelligent assistance, though the paper did not cite it).
>
> Tradeoffs (Joel Chan, SP-25 Week 4 announcements, on DM tradeoffs for novices):
> - [[@shneidermanDirectManipulationVs1997]]: the 1990s debate between Ben Shneiderman and Pattie Maes on DM vs. interface agents. Maes: "there are real limits to what we can do with visualization and direct manipulation because our computer environments are becoming more and more complex. We cannot just add more and more sliders and buttons ... we will have to, to some extent, delegate certain tasks or certain parts of tasks to agents ... However, this is completely a complementary technique to well-designed interfaces—visualization, and direct manipulation—not a replacement. Users still need to be able to bypass the agent if they want to do that."
> - [[@maayanHowDomainExperts2020]]: experts making conceptual diagrams don't do all their work in DM paradigms (cf. canvases), nor entirely in programming. The paper is a deep dive into the affordances of each: DM for faster feedback and global control; programming for abstraction and local control.
> ![[p443b9ZFR7.png]]

## Key Examples
> [!info] What are some key examples of the pattern instantiated in artifacts/systems? Later we can link particularly instructive/illustrative ones via the "Instantiates" discourse relation.

Claude:
> - [[ART - GAM Changer]]: DM helps with the basic mechanics of editing a model for users without ML/software engineering expertise. Users edit the model by directly editing its shape function, with scaffolds like preset "modification types" (align, interpolate) (SP-25 seminar notes).
> ![[omkpng_BTY.png]]
> - S05 (SP-25, Group 1): GAM Changer affords "technical resources" through [[PTN - Shared Representation]] and DM to monitor and adjust model behavior directly.
> - S01 (SP-25) on Patchview: visualization helps make sense of models but can suffer optical illusions (ambiguity, distortion); Patchview counters this by letting users "adjust the layout of concepts (Figure 4d), aligning their visual presentation with how they want to think about these concepts and elements."
> - Non-example: [[ART - ChainForge]] is not a clear example of DM, compared to [[ART - GAM Changer]] (Joel Chan, SP-25 key insights).

## Other Notes

Claude:
> - Claim: [[CLM - ART - GAM Changer or PTN - Direct Manipulation-based approaches to steering models are best used in collaborative teams with domain experts - end users and ML engineers]] (discussed with the GAM Changer case studies, SP-25).
> - Hypothesis (Joel Chan, SP-25 Week 2): people with more technical expertise want more fine-grained control than is available in DM-based interfaces for computational work.
> - S01 (SP-25) linked DM to [[PTN - Actionable explainability]]: explainability not only increases users' understanding of how and why decisions are made, but can signal how to steer the model in a desired direction, if allowed.
> - S05 (SP-25) open question: when people without technical expertise get technical resources to influence model behavior, is their usage reasonable? Should we be cautious about how much access non-technical experts get?
> - Open question (Joel Chan, SP-25 Week 4): what constitutes a DM interface?
