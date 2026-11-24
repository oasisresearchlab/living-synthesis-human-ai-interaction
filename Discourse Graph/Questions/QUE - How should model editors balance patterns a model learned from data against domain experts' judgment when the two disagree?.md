---
nodeTypeId: node_Gp7JMdrzm9DUuPfBzUptc
nodeInstanceId: 01a20e92-2249-7d18-991f-3b928a27c200
NodeFormality: ai-draft
aliases:
extractedFrom: "[[SP-25 W02 (2025-02-05)]]"
created: 2026-11-24
---
## Context
Claude:
> S01 (🚧 Safety Inspection Expert, SP-25 W02 notes), echoing participant P2 in [[@wangInterpretabilityThenWhat2022]] ("it was more 'objective' to retrain the model until it learned expected patterns rather than manually modifying the model"), asked "how should we balance data-driven insight (pure GAM model) and expert judgement (actions of edits)". Whether an odd shape is counterintuitive and needs changing, or is real signal "which should not be overlooked", relies heavily on the user's expertise.
>
> In discussion, a participant used the asthma example from [[EVD - it was possible for a physician and ML researcher to use ART - GAM Changer to edit a GAM model for pneumonia risk prediction to account for possible issues with age and asthma predictors - @wang]]: "ideally ... the data should be suggesting" the right prediction, because data feels "more objective". The response was "Given that the data collection is objective and high quality?" Then: "Do we always have access to a data set that can reveal these properties for our model? Probably not." (SP-25 W02, [00:23:32]–[00:25:44])

## Other Notes
Claude:
> - The study participants also disagreed about whether to retrain, edit, or collect more data. Joel Chan judged these questions "out of scope" for what [[ART - GAM Changer]] is designed for: "if you want to edit it, you can do it" (SP-25 W02, [00:25:44]).
> - See [[CLM - noticing a discrepancy between a model and expert knowledge is a separate problem from deciding whether to retrain, collect more data, or edit the model]] and [[EVD - a data scientist in the GAM Changer study felt it was more objective to retrain the model until it learned expected patterns than to manually edit it - @wangInterpretabilityThenWhat2022]].

## Suggested relations
Claude:
> - derived from → [[EVD - a data scientist in the GAM Changer study felt it was more objective to retrain the model until it learned expected patterns than to manually edit it - @wangInterpretabilityThenWhat2022]]: the participant quote that prompted the question (S01, SP-25 W02)
> - informs → [[CLM - noticing a discrepancy between a model and expert knowledge is a separate problem from deciding whether to retrain, collect more data, or edit the model]]: separates noticing from deciding (SP-25 W02, [00:24:59])
> - informs → [[CLM - interpretable but non-explanatory model editing tools put the onus for correct edits on the user's expertise]]: the balance falls on the user (SP-25 W02, [00:27:00])
