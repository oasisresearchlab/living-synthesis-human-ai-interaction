---
nodeTypeId: node_wZiOhnAnXKDVhrvl-7Z4P
nodeInstanceId: 01a20e70-661f-7f34-99d6-1800b1ff7068
aliases:
roamUrl: https://roamresearch.com/#/app/umd-inst828-hcai-design/page/PffjArFYx
roamAuthor: "S13"
created: 2024-04-10
---

## Discussion notes
Claude:
> **What the paper is.** "To our knowledge, this paper presents the first human-centered evaluation of a production-level deep learning model for diagnostic prediction, being used across several clinics for patient care." (p. 3) The system screens for diabetic retinopathy (DR) in Thailand, where nurses take photos of the retina during diabetes check-ups and send them to an ophthalmologist for review (p. 2). The algorithm "has been shown to have specialist-level accuracy (>90% sensitivity and specificity)" (p. 2). (SP-24 seminar annotations, 👾 Hacker role)
> - Context: "In Thailand, there are 1500 ophthalmologists," "a ratio of about 1:3000, about double of what it is in the United States" (p. 1), and "less than 50% of the diabetic patients are screened annually since the inception of the program" (p. 3).
> - Takeaways from the accompanying video: patients wait about 5 hours for a brief checkup, then another week for physicians to examine the retinal images; about 20% of images were not gradable by the model; AI plus human clinician works best. (SP-24 seminar notes)
> ![[A7TwZfJCos.mp4]]

Claude:
> **Motivation: accuracy is not enough.**
> - "no requirements for AI systems to be evaluated through observational clinical studies, nor is it common practice. This is a problem because the success of a deep learning model does not rest solely on its accuracy, but also on its ability to improve patient care" (p. 2). An annotator compared this to the lack of an analogue to the FDA's drug and vaccine development pathway. (SP-24 seminar annotations)
> - Prior CAD tools in mammography "have been shown to require a radiologist to do more work, not less, and generally do not improve a radiologist’s diagnostic accuracy" (p. 2), reminiscent of the IT productivity paradox. (SP-24 seminar annotations)
> - Lab studies help clinicians "gain an initial 'global' impression of a model", but "do not account for the highly situated nature of activities in clinical environments" (p. 2); "clinical trials fail to grasp the situated social and collaborative dimensions of medical work" (p. 2).

Claude:
> **Methods.** Fieldwork at 11 clinics in Pathum Thani and Chiang Mai (November 2018, April 2019, August 2019), before deployment: "26 hours of observation (adopting a non-member role) across 11 clinics" of more than 100 patients, plus "15 hours of interviews with the 13 nurses who lead eye screening at eight clinics" (pp. 4-5). After deployment: "12 hours observing the eye screening process of about 50 patients, and ... seven hours of interviews among five nurses and one camera technician" (p. 5). Interviews (~90 minutes) used a Thai interpreter; analysis used daily affinity notes and affinity mapping, yielding themes of "gradability, referrals, design implications, satisfaction, consent considerations, eye-screening workflows, and patient education" (p. 5). The system was deployed in a prospective study with 7600 patients (p. 3).
> - A prospective cohort study is "a type of observational study focused on following a group of people (called a cohort) over a period of time" ([Scribbr](https://www.scribbr.com/methodology/prospective-cohort-study/)). (SP-24 seminar notes, April 17th, 2024)
> ![[0ptPSCiKbf.png]]

Claude:
> **Key findings: sociotechnical mismatch.**
> - Image gradability: "If an image has a bit of blur or a dark area, for instance, the system will reject it, even if it could make a strong prediction." 21% of images "didn't meet the system’s high standards for grading" (p. 8). "The system’s high standards for image quality is at odds with the consistency and quality of images that the nurses were routinely capturing under the constraints of the clinic, and this mismatch caused frustration and added work." (p. 8)
> - Environmental constraints: "Waiting 60 seconds before imaging the second eye is nearly impossible when a nurse has 150 patients in the queue waiting to be screened." (p. 8) An internet outage of two hours cut the number of patients screened from 200 to 100 (p. 8).
> - Consent and referrals: because the system gives an immediate referral recommendation, and referral could mean an hour's drive to Pathum Thani Hospital without reliable transportation, nurses at two clinics dissuaded patients from participating; "50% of patients at clinic 4 opted out of participating in the study, even though it was unlikely that they would be referred." (p. 7)
> - Workarounds: for ungradable images, nurses used their own judgement, e.g., sending patients with no DR history and well-controlled blood sugar home without a referral. (p. 9)

Claude:
> **Implications.** "end-users and their environment determine how a new system will be implemented; that implementation is of equal importance to the accuracy of the algorithm itself" (p. 9). Many environmental factors can be reduced "by tactical means (in our case, through lighting adjustments and camera repairs)" (p. 9). The authors call for formative work (clinical ethnography, observation, interviews, participatory design) "prior to, and in parallel with, system development", studies with live clinical data rather than only retrospective datasets, and participatory and service design; they began participatory design workshops with nurses, camera operators, and retinal specialists (p. 10).

Claude:
> **Connections.** Lauren Wilcox, a co-author, later adapted datasheets to healthcare: Healthsheet: Development of a Transparency Artifact for Health Datasets, https://arxiv.org/pdf/2202.13028.pdf. (Joel Chan, responding to S13 as 🕸️ Connector, SP-24)
