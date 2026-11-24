---
nodeTypeId: node_1HEGLbbU4UMRzwDKj_PxA
nodeInstanceId: 01a20e94-6c86-7c6e-b3e6-08c6c2ba484d
NodeFormality: ai-draft
TruthValue: 0.5
aliases:
extractedFrom: "[[SP-24 W13-16 Evaluation and accountability]]"
created: 2026-11-24
---
## Grounds

Claude:
> - The distiller's general takeaway: "It is important to consider all types of socio-environmental factors that could go impact deployment! Including internet connection! Including environment setups! DL systems cannot be a one-size-fits all, and should ideally be robust to these kinds of issues." (S11, Distiller, SP-24 W13)
> - Situational issues in the environment lead to poor-quality inputs, poor-quality outputs, and strain in a fast-paced clinic. (S11, SP-24 W13)
> ![[dRsKpP04yO.png]]
> - The paper itself: "end-users and their environment determine how a new system will be implemented; that implementation is of equal importance to the accuracy of the algorithm itself" (p. 9, as recorded in [[@beede2020humancentered]]).
> - Evidence: [[EVD - about 21% of retinal images captured by nurses in Thai clinics failed a deployed diabetic retinopathy model's gradability standards, causing retakes and frustration - @beede2020humancentered]], [[EVD - nurses in Thai clinics dissuaded patients from joining a deep learning eye-screening study because a positive result could mean referral to a distant hospital - @beede2020humancentered]], [[EVD - slow internet connections in Thai clinics delayed a cloud-based diabetic retinopathy model's results and cut the number of patients screened - @beede2020humancentered]].

## Other Notes

Claude:
> - Clinics varied widely: nurses organized screening workflows themselves, resources differed (dilation drops in some Chiang Mai clinics, none in Pathum Thani), and only two clinics had a room that could be darkened. (S11, Distiller, SP-24 W13)
> - The Archaeologist's cited work (Greenhalgh et al. 2018) and classic CSCW make the same point about implementation complexity (S08 and Joel Chan, SP-24 W13).

## Suggested relations
Claude:
> - derived from → [[@beede2020humancentered]]
> - informs → [[QUE - What design considerations must system developers consider when deploying deep learning models in clinical settings?]]
> - consistent with → [[CLM - a mismatch between work-as-imagined and work-as-done is a major reason technologies fail to be adopted in organizations]]: both locate failure in the gap between the imagined and actual work setting
> - consistent with → [[CLM - ML model performance measured on internal test data often drops substantially in real-world deployment]]: lab performance doesn't carry over to deployment
