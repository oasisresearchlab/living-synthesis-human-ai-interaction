---
type: extraction-session
session: "SP-24 W13-16 Evaluation and accountability"
sources: [notes]
extractedBy: Claude
created: 2026-11-24
---
Claude:
> The last four SP-24 weeks were about evaluating AI and holding it accountable. W13 read Beede et al. (2020), a field evaluation of a deployed diabetic retinopathy model in Thai clinics. W14 read Raji et al. (2020) on internal algorithmic auditing (SMACTR). W15 read Braggaar et al. (2023), a systematic review of how task-oriented dialogue systems are evaluated. W16 read Suresh et al. (2022) on intersectional feminist, participatory ML for feminicide counterdata. Main threads: lab accuracy vs. deployment fit; whether problems could be caught earlier and more cheaply with participatory methods; metis vs. techne and deferral to frontline workers; Mary L. Gray's critique of dogfooding; measure validity and jingle-jangle problems; and designing with communities vs. retroactive audits. Contested points: whether the audit framework "works" (no evidence in the paper; S13 on cost and impact), and whether the feminist participatory approach produced a better model (Joel Chan read the Precision@K results as a wash and the deployment false-positive rates as high).

## Nodes created
### Questions
- [[QUE - How should the relative costs of false positives and false negatives in a clinical AI system be decided, and by whom?]]
- [[QUE - How many deployment problems of an AI system could be anticipated earlier and more cheaply than with a full prospective field evaluation?]]
- [[QUE - How can research teams without large-company resources run prospective in-the-wild evaluations of AI systems?]]
- [[QUE - How much does AI-based screening actually relieve scarce healthcare workers, and which burdens does it relieve?]]
- [[QUE - How might AI systems incorporate frontline workers' metis rather than override it?]]
- [[QUE - How can we tell whether an internal AI audit framework actually works, at what cost, and whether its recommendations change practice?]]
- [[QUE - Who should conduct AI audits, and can auditing be democratized beyond elite institutions?]]
- [[QUE - How might critical appraisal tools from open science and metascience speed up the development of AI auditing?]]
- [[QUE - Should triangulation be limited to a single study, or can it combine evidence across a body of studies?]]
- [[QUE - How can we validate measures of human-AI interaction constructs, for example through shared studies and psychometric methods?]]
- [[QUE - How should success be defined and measured for general-purpose dialogue systems that have no single task?]]
- [[QUE - How can ML systems serve groups organized around race and gender without imposing fixed classifications on fluid identities?]]
- [[QUE - Does training ML builders in data feminism change their design decisions?]]

### Claims
- [[CLM - the real-world value of a clinical AI system depends as much on its fit with local workflows, environments, and infrastructure as on its model accuracy]]
- [[CLM - input-quality thresholds tuned for accuracy in controlled settings can clash with real-world capture conditions and shift extra work onto frontline users]]
- [[CLM - deferring hard cases from an AI system to humans works better when the humans can handle those cases under suboptimal conditions and the handoff is not time-critical]]
- [[CLM - the cost function for an AI system's errors is easier to surface with participatory methods before any code is written than through post-deployment evaluation]]
- [[CLM - the order in which humans and AI contribute to a decision workflow shapes how much people trust and rely on the AI]]
- [[CLM - a mismatch between work-as-imagined and work-as-done is a major reason technologies fail to be adopted in organizations]]
- [[CLM - dogfooding embeds a tacit theory of power that sidelines risk and harm and flattens differences between builders and other users]]
- [[CLM - early prototyping and dogfooding can anchor a design trajectory so that later user feedback cannot drive fundamental changes]]
- [[CLM - for systems in social use, a single person with a device is the wrong unit of analysis for the end user]]
- [[CLM - lab-based accuracy evaluations of AI mirror modernist evidence-based medicine and need complementing by contextual, theory-driven evaluation]]
- [[CLM - internal audits complement external audits by giving access to intermediate stages of AI development, much as participatory design complements post-hoc usability testing]]
- [[CLM - audit practices from aerospace, medical devices, and finance do not transfer directly to AI because AI systems are large-scale, data-entangled, general-purpose, and highly customized]]
- [[CLM - accountability for AI requires explanations of the process behind a model's development, not just explanations of the model itself]]
- [[CLM - many widely deployed AI models do not disclose their training data or follow the internal audit practices proposed for accountable AI]]
- [[CLM - evaluation of conversational AI suffers from jingle-jangle problems, where one construct is measured in many ways and different constructs share names, which makes studies hard to compare]]
- [[CLM - in fields with unstable terminology, keyword searches miss relevant work, so literature reviews need citation chaining and network search]]
- [[CLM - ML model performance measured on internal test data often drops substantially in real-world deployment]]
- [[CLM - success in participatory ML includes relational outcomes such as trust, shared power, community, and imagined future work, not just model metrics]]
- [[CLM - designing AI with affected communities from the start is preferable to relying on retroactive audits of potentially flawed systems]]
- [[CLM - classifiers trained on news articles can perpetuate the erasure of marginalized victims because news coverage misgenders people and omits race]]

### Evidence
- [[EVD - about 21% of retinal images captured by nurses in Thai clinics failed a deployed diabetic retinopathy model's gradability standards, causing retakes and frustration - @beede2020humancentered]]
- [[EVD - nurses in Thai clinics dissuaded patients from joining a deep learning eye-screening study because a positive result could mean referral to a distant hospital - @beede2020humancentered]]
- [[EVD - slow internet connections in Thai clinics delayed a cloud-based diabetic retinopathy model's results and cut the number of patients screened - @beede2020humancentered]]
- [[EVD - a nurse tried to combine two ungradable photos of one eye into a composite image, expecting a diabetic retinopathy model to accept it - @beede2020humancentered]]
- [[EVD - radiologists who gave their own assessment before seeing an AI assessment were more likely to distrust the AI and find it less useful - Fogliato et al 2022]]
- [[EVD - a longitudinal ethnography of healthcare technology programmes found a substantial mismatch between work-as-imagined and work-as-done - Greenhalgh et al 2018]]
- [[EVD - an analysis of over 7,000 Hugging Face data cards found that many recommended sections were ignored, focusing on data description over considerations for use - James Zou group ICLR 2024]]
- [[EVD - a systematic review of 122 evaluation studies of task-oriented dialogue systems found 108 constructs, which authors rarely defined and sometimes defined incompatibly - Braggaar et al 2023]]
- [[EVD - studies of task-oriented dialogue systems measured realism or humanness only with human evaluation, mostly surveys, and never with automatic metrics - Braggaar et al 2023]]
- [[EVD - in 5-fold cross-validation, hybrid and contextual hybrid feminicide article classifiers beat a joint model on AUPRC and AUROC but not clearly on Precision at K - Suresh et al 2022]]
- [[EVD - in deployment, a contextual hybrid classifier for police killings of Black women returned 12 relevant cases out of 37 articles, despite few false positives in internal testing - Suresh et al 2022]]
- [[EVD - in deployment, a contextual hybrid classifier for missing and murdered Indigenous women returned 10 of 20 articles describing specific cases - Suresh et al 2022]]

### Patterns
- [[PTN - selective deferral to human experts for uncertain or low-quality inputs]]
- [[PTN - dogfooding]]
- [[PTN - participatory execution]]
- [[PTN - internal algorithmic auditing]]
- [[PTN - Failure Modes and Effects Analysis (FMEA)]]
- [[PTN - triangulation]]
- [[PTN - participation as justice vs participation as work]]
- [[PTN - co-designing datasets and ML models with affected communities]]

### Artifacts
- [[ART - SMACTR internal algorithmic audit framework]]
- [[ART - Model Cards]]
- [[ART - Datasheets for Datasets]]
- [[ART - Email Alerts system for feminicide counterdata collection]]

### Theories
- [[THE - metis and techne]]
- [[THE - Data Feminism]]
- [[THE - Matrix of Domination]]
- [[THE - Intersectionality]]

## Bears on existing nodes
Claude:
> - [[QUE - What design considerations must system developers consider when deploying deep learning models in clinical settings?]]: now backed by four Beede EVDs and two CLMs (deployment fit; quality thresholds vs. capture conditions). (S11, SP-24 W13)
> - [[QUE - How can one evaluate deep learning models in clinical settings?]]: adds the prospective-vs-cheaper-earlier-methods question, the resource question for small labs, and the lab vs. realist evaluation framing (Joel Chan, S11, SP-24 W13).
> - [[@beede2020humancentered]]: adds the gradability quote and Figure 5 composite-image workaround, consent/referral quotes, and the internet quote as separate EVDs.
> - [[PTN - comicboarding for stakeholder feedback on ML decision-making models]] and [[@kuoUnderstandingFrontlineWorkers2023]]: now linked as a means of surfacing the error "cost function" before building (Joel Chan, SP-24 W13).
> - [[@alkhatibStreetLevelAlgorithmsTheory2019]]: linked to the new metis/techne theory node; nurses' workarounds as street-level discretion (Joel Chan, SP-24 W13).
> - [[@wieringaHasEvidencebasedMedicine2017]]: now grounds a claim that lab-based AI evaluation mirrors "modernist" EBM (Joel Chan, SP-24 W13).
> - [[@ackermanIntellectualChallengeCSCW2000]] and [[@grudinWhyCSCWApplications1988]]: ground the new work-as-imagined vs. work-as-done claim and the dogfooding/social-use claims.
> - [[@rajiClosingAIAccountability2020]]: the source note had only metadata; the SMACTR stages, the transfer-from-other-industries argument, and the Selbst and Barocas process-explanation quote are now nodes.
> - [[ART - Auditing Ai]]: linked from the audit democratization question (S13, SP-24 W14).
> - [[ART - CheckList]] (created in parallel from SP-25 W03): S11 also proposed it in SP-24 W14 for the testing stage of internal audits. I didn't create a duplicate; it's linked from SMACTR.
> - [[CLM - algorithmic audits work better as ongoing public practices around matters of concern than as one-time certifications of matters of fact]] (created in parallel from SP-24 W08-12): consistent with the internal auditing pattern; linked.
> - [[PTN - Think-aloud triangulation of evaluation metrics]] (created in parallel from SP-25 W04): a specific case of the new general triangulation pattern; linked.
> - [[@liptonMythosModelInterpretability2017]]: Joel framed "explanations of the process behind a model's development" as another property of interpretability (SP-24 W14).
> - [[@bennettHowDoesHCI2023]]: proposed as a model for theory-building on dialogue-evaluation constructs (Joel Chan, SP-24 W15); Joel also asked where agency fits among the UX constructs.
> - [[PTN - Seamful XAI]]: S13 (Connector, SP-24 W16) said Ehsan's seamful XAI process meets goals similar to Suresh et al.'s.
> - [[PTN - Invisible Labor]]: Data Feminism's "Make Labor Visible" principle is the contrast S13 drew (SP-24 W16); linked from THE - Data Feminism.
> - [[CLM - LLM-generated personas can flatten and caricature marginalized identity groups]]: consistent with the new claim that news-trained classifiers perpetuate erasure.
> - [[QUE - What metrics-framework should be used to evaluate LLM policy effectiveness (technical implementability, interpretability, alignment, etc.)?]]: informed by the jingle-jangle claim, the measure-validation question, and the relational-success claim.

## Suggested relations
Claude:
> - [[CLM - ML model performance measured on internal test data often drops substantially in real-world deployment]] — consistent with → [[CLM - the real-world value of a clinical AI system depends as much on its fit with local workflows, environments, and infrastructure as on its model accuracy]]: the W13 and W16 deployments both underperformed lab expectations, for different reasons
> - [[EVD - in 5-fold cross-validation, hybrid and contextual hybrid feminicide article classifiers beat a joint model on AUPRC and AUROC but not clearly on Precision at K - Suresh et al 2022]] — opposes → [[CLM - designing AI with affected communities from the start is preferable to relying on retroactive audits of potentially flawed systems]]: Joel Chan's critique of the evidence for a better model
> - [[CLM - the cost function for an AI system's errors is easier to surface with participatory methods before any code is written than through post-deployment evaluation]] — consistent with → [[CLM - designing AI with affected communities from the start is preferable to relying on retroactive audits of potentially flawed systems]]: W13 and W16 converge on the "starting point"
> - [[CLM - internal audits complement external audits by giving access to intermediate stages of AI development, much as participatory design complements post-hoc usability testing]] — consistent with → [[CLM - early prototyping and dogfooding can anchor a design trajectory so that later user feedback cannot drive fundamental changes]]: timing and access determine what feedback can change
> - [[THE - metis and techne]] — informs → [[PTN - selective deferral to human experts for uncertain or low-quality inputs]]: deferral is one way to make room for frontline metis
> - [[EVD - a systematic review of 122 evaluation studies of task-oriented dialogue systems found 108 constructs, which authors rarely defined and sometimes defined incompatibly - Braggaar et al 2023]] — consistent with → [[EVD - phd student reading ChainForge paper found it difficult to formalize intuitive sense on different dimensions when comparing into metrics that can be studied systematically]]
> - [[CLM - many widely deployed AI models do not disclose their training data or follow the internal audit practices proposed for accountable AI]] — consistent with → [[EVD - an analysis of over 7,000 Hugging Face data cards found that many recommended sections were ignored, focusing on data description over considerations for use - James Zou group ICLR 2024]]
> - Each new node's own "Suggested relations" section has the full per-node list.

## Skipped or uncertain
Claude:
> - **Un-pseudonymized name**: the W16 Connector notes mention "[name]" in INST 808, plausibly a student. I left it out of every node.
> - No source notes exist for Braggaar et al. 2023, Suresh et al. 2022, Fogliato et al. 2022, Greenhalgh et al. 2018, Mitchell et al. 2018, or Gebru et al. 2018. They are cited in plain text, and the EVD titles use "Author et al YEAR" instead of a citekey. Joel may want source notes for Braggaar and Suresh, since they were core readings.
> - The Hugging Face data-card EVD comes only from a tweet by James Zou that Joel shared; the paper wasn't read and its authors aren't in the notes. I believe it is Yang, Liang & Zou (ICLR 2024), but I haven't verified that, so the title says "James Zou group". Check the citation.
> - The ChatGPT-doesn't-disclose claim is S11's characterization next to Birhane et al. (2024), not a finding attributed to that paper.
> - Skipped: the Birhane tweet about auditing being absorbed by traditional auditors (folded into the democratization QUE as context); the cognitive-tutor and One Laptop per Child shared-device connection (passing mention); the Queer Art of Failure, Appreciative Inquiry, Tech Otherwise, and Eve Tuck pointers (no development); S13's research synthesis method, WISDOM, 3ieimpact, and seaboat.io links (mentioned but not argued); the idea of turning the review's tables into JSON with an LLM (a hacker-task aside); ELI5 definitions of observational study and ethnomethodology; S05 on patient attitudes and the "liability of AI" (one line, not developed).
> - The Data Feminism node lists the six principles as written in the notes, which follow the feminist data visualization summary. The Data Feminism book (D'Ignazio & Klein 2020) has seven principles, with examine power and challenge power as separate principles. Suresh et al. also use "Challenge Power". Reconcile against the source if it matters.
> - W15 had no Archaeologist, Connector, or Hacker contributions; W14 and W15 had no Hacker work.
