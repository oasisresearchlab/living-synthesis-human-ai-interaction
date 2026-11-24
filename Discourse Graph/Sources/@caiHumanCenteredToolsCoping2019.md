---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-6620-72df-8926-d1c6c5f5f420
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/VorxBCB67
roamAuthor: "Joel Chan"
created: 2024-01-24
---

- Title: Human-Centered Tools for Coping with Imperfect Algorithms During Medical Decision-Making
- Author(s):: Carrie J. Cai, Emily Reif, Narayan Hegde, Jason Hipp, Been Kim, Daniel Smilkov, Martin Wattenberg, Fernanda Viegas, Greg S. Corrado, Martin C. Stumpe, Michael Terry
- Type: Conference paper
- URL : https://dl.acm.org/doi/10.1145/3290605.3300234
- Date Added: October 12th, 2023
- Zotero links: [Local library](zotero://select/groups/2451508/items/TUB55TDF), [Web library](https://www.zotero.org/groups/2451508/items/TUB55TDF)
- PDF links : [Cai et al_2019_Human-Centered Tools for Coping with Imperfect Algorithms During Medical.pdf](zotero://open-pdf/groups/2451508/items/I62T6MR9)

## Discussion notes
Claude:
> Read in Week 5 of the SP-24 seminar (February 21st, 2024, "Decision-making / trust / explainability"); also listed among the design-example readings.
>
> **Artifact and "secret sauce" (Joel Chan's notes)**
> - The system is [[ART - SMILY]].
> ![[IMicUpRFHI.png]]
> - The key secret sauce for refine-by-concept is [[PTN - Concept Activation Vectors (CAVs)]].
> ![[eANNWS0r00.png]]
> ![[8LF_fN_d2K.png]] (pp. 3-4)
> ![[WGhsHWWcY2.png]]
>
> **Critiques**
> - S11 worried about the linear assumptions in this implementation of CAVs: "Why use linear classifiers to model the refinable concepts independently, when at inference time search results are returned collectively?" This becomes an issue when a user noted they weren't sure about the "strength" of the slider, and the intensity of the shift could impact the overall search query.
> - Joel Chan noted that the focus on linear models in [[@liptonMythosModelInterpretability2017]] is a nice complement to S11's worries.
