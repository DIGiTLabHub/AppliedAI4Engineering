# Topic 18 - AI Futures, World Models, Embodied Intelligence, and Engineering Judgment

> Working thesis: the most credible post-LLM future is not a single replacement paradigm. It is a layered stack. Foundation models remain powerful interface engines; neuro-symbolic methods matter where explicit constraints and verification matter; world models matter where prediction, control, and action matter; embodiment matters where intelligence must survive contact with the physical world. None of this justifies surrendering engineering judgment to general-intelligence rhetoric.

This chapter moves from systems that already shape engineering practice into frontier arguments that are technically serious but not yet settled. The task is not to predict a winner. The task is to separate what exists now from what is emerging, what is evidenced from what is hypothesized, and what is useful for engineers from what is mostly narrative inflation. Throughout, the chapter takes a stricter position than a neutral survey: the next decade is more likely to be defined by hybridization and domain-specific progress than by one clean leap to human-level or superhuman general intelligence.

## 1. Introduction: entering the frontier

The foundation-model era has already changed software, search, content generation, and parts of engineering workflow. Broadly pretrained models can be adapted to many downstream tasks, and the dominant practical stack is no longer "a model alone" but a model linked to retrieval, tools, environments, and human supervision [@bommasani2021foundation; @yao2022react; @schick2023toolformer; @wang2023voyager]. That stack is powerful. It is also incomplete.

The incompleteness matters. Current systems are strong at language interface, pattern matching, code generation, and procedural decomposition, yet they remain weaker at robust grounding, stable world-state tracking, and reliable reasoning about physical consequence under open-ended uncertainty. Benchmarks on physical reasoning show progress, but they also show clear limits: text-centric models can answer many scenario-based questions, yet on harder and more realistic physics problems they still trail human experts by a substantial margin [@wang2023newton; @qiu2025phybench].

This is the entry point for Topic 18. The central question is not whether present AI is impressive. It is. The question is what kinds of architecture and training signal are likely to matter once present LLM-plus-tool systems stop scaling cleanly into the domains we care about most: scientific reasoning, safety-critical control, robotics, and accountable engineering deployment.

## 2. Taking stock of the current AI paradigm

The present paradigm is best described as foundation-model pragmatism. A large pretrained model supplies broad prior knowledge, then external mechanisms compensate for its weaknesses. Retrieval helps factuality. Tools help arithmetic, search, and action. Prompting and agent loops help decomposition. Humans remain in the loop when consequences matter [@bommasani2021foundation; @yao2022react; @schick2023toolformer]. In embodied simulation environments such as Minecraft, this recipe can even support open-ended skill accumulation, as shown by Voyager, but that still occurs inside a strongly scaffolded environment with explicit APIs and constrained feedback channels [@wang2023voyager].

That matters for interpretation. The most important practical fact about current AI is not that one model has become universally competent. It is that model competence is increasingly purchased by system design. The system boundary now includes prompts, memory, retrieval, action interfaces, verification layers, and operators. This is an engineering fact before it is a philosophical one.

The major unresolved weakness is grounding. Current language-first systems do not automatically acquire stable causal models of the physical world merely by becoming better next-token predictors. They can imitate reasoning traces, summarize physical rules, and sometimes solve structured physics tasks, but this is not the same as possessing robust sensorimotor understanding or actionable world models. The gap is visible whenever tasks require persistent state estimation, contact-rich manipulation, long-horizon control, or recovery from novel physical failure [@wang2023newton; @qiu2025phybench].

A sober conclusion follows. Current LLM systems are powerful enough to transform many engineering workflows. They are not yet a sufficient theory of intelligence, and they are not yet a sufficient substrate for reliable physical agency.

## 3. Neural-symbolic AI

Neuro-symbolic AI refers to systems that combine learned subsymbolic representations with explicit symbolic structure: rules, programs, constraints, variables, knowledge bases, or logical and probabilistic reasoning machinery [@besold2017nesy; @colelough2025nesyreview]. The field exists because deep learning and symbolic methods fail in opposite ways. Neural models learn from raw data, tolerate noise, and scale in perception. Symbolic systems can represent compositional structure, explicit constraints, and traceable inference, but they are brittle when the world is high-dimensional, ambiguous, and only partially formalized.

The strongest argument for neuro-symbolic AI is not nostalgia for symbolic AI. It is engineering necessity in domains where correctness depends on explicit structure. Representative systems make this concrete. DeepProbLog injects neural predicates into probabilistic logic programming, allowing learned perception to interact with explicit reasoning and uncertainty handling [@manhaeve2019deepproblog]. Neural Logic Machines show that differentiable architectures with relational and logical inductive bias can recover lifted rules and generalize from small cases to larger ones on structured reasoning tasks [@dong2019nlm]. The Neuro-Symbolic Concept Learner combines object-centric perception, semantic parsing, and executable programs for visual question answering, showing how symbolic execution can be layered over learned scene representations [@mao2019nscl].

Recent review work supports both the promise and the limitation. A 2025 systematic review shows rapid growth in neuro-symbolic research during 2020-2024, but it also shows uneven maturity across the field: learning and inference are active, whereas trustworthiness and meta-cognition remain relatively underdeveloped [@colelough2025nesyreview]. That pattern is revealing. It means the field is technically alive, but it has not yet solved the harder problem of delivering broad, reliable, engineering-grade integration at scale.

The right conclusion is selective, not maximalist. Neuro-symbolic methods are most compelling when the domain contains real structure that engineers can and should preserve: laws, design constraints, ontologies, safety rules, operating procedures, geometric relations, program semantics, or scientific priors. In such domains, symbolic structure improves auditability and can reduce the amount of data required. In unconstrained open-world tasks, however, symbolic layers can become the new bottleneck. If the ontology is unstable, incomplete, or expensive to maintain, the symbolic component adds fragility rather than intelligence.

My extension of the argument is direct: neuro-symbolic AI is unlikely to replace foundation models as the dominant general interface layer, but it is likely to become more important as a constraint, reasoning, and verification layer around them. That is where its engineering value is strongest.

## 4. World models and predictive latent representations

"World model" is now used in more than one way. In model-based reinforcement learning, a world model is a learned dynamics model that lets an agent imagine futures and plan in latent space [@ha2018worldmodels; @hafner2019planet; @hafner2020dreamer]. In the more recent JEPA line associated with Yann LeCun and collaborators, the emphasis shifts toward learning abstract predictive representations that capture what is predictable and task-relevant without reconstructing every pixel or token [@lecun2022path; @assran2023ijepa; @garrido2024iwm]. These communities overlap, but they are not identical.

The classical model-based RL trajectory is already substantive. Ha and Schmidhuber popularized the modern "world models" framing by separating representation learning, temporal prediction, and control [@ha2018worldmodels]. PlaNet showed that latent dynamics models could support online planning directly from pixels [@hafner2019planet]. Dreamer then pushed further by learning behaviors through latent imagination rather than raw-environment interaction [@hafner2020dreamer]. DreamerV3 demonstrated how far this line can scale, reporting a single fixed algorithm that performs strongly across more than 150 tasks and domains [@hafner2025dreamerv3]. This is not hype. It is a real research program with credible empirical wins.

LeCun's position paper gives this broader philosophical force. His argument is that next-token prediction alone is an insufficient route to autonomous intelligence because intelligence requires hierarchical representation, prediction, planning, and action over latent world states rather than surface-level sequence continuation [@lecun2022path]. This is an important critique, but it remains partly a roadmap rather than a proven theory. A position paper is not a demonstration.

The JEPA family is best interpreted as an attempt to operationalize that roadmap. I-JEPA predicts masked image representations in latent space rather than reconstructing pixels, aiming to bias learning toward semantic structure [@assran2023ijepa]. V-JEPA extends the idea to video, arguing that feature prediction in latent space can produce strong video representations without generative reconstruction [@bardes2024vjepa]. Garrido et al. then explicitly frame JEPA-style models as "image world models," showing that predictive latent models can be learned and later leveraged for visual tasks [@garrido2024iwm]. V-JEPA 2 is the most ambitious step in this line so far: it combines very large-scale video pretraining with a small amount of robot interaction data and shows a route from latent prediction to robotic planning [@assran2025vjepa2].

Yet this is exactly where discipline is required. The evidence for world models is strongest in control, reinforcement learning, video representation, and some goal-conditioned robotic planning. It is much weaker as a general claim that predictive latent modeling has already superseded or will soon supersede autoregressive modeling across all of AI. Even recent JEPA planning work states the limitation plainly: standard JEPA world models still have limited support for effective action planning, and extra objective shaping is needed to improve results even on simple control tasks [@destrade2026valueguidedjepa].

So the correct assessment is neither dismissal nor coronation. World models are one of the most serious candidates for progress beyond language-only systems because they target prediction, action, and abstraction directly. But outside domains where action and dynamics are central, their superiority over autoregressive methods remains unproven. The strongest hypothesis here is not "JEPA will replace transformers". It is narrower and better supported: systems that must predict consequences and act in the world will need learned state abstractions that are better than pure token continuation.

## 5. Embodied intelligence

Embodiment is often discussed imprecisely. The rigorous definition is not "having a camera" or "being multimodal." Embodiment means intelligence coupled to a body that acts in an environment, changes future observations through action, and must manage the sensorimotor consequences of its own behavior. Rodney Brooks made this point decades ago in his critique of disembodied, representation-heavy AI, arguing that situated action and world interaction are not optional extras but constitutive parts of intelligence in many settings [@brooks1990elephants; @brooks1991representation].

Current robotics research shows why the issue returned. RT-1 demonstrated that large-scale robot data and transformer architectures can support broad real-world robotic control [@brohan2022rt1]. RT-2 pushed further by directly folding web-scale vision-language knowledge into action generation, creating a recognizable vision-language-action model [@brohan2023rt2]. The Open X-Embodiment collaboration scaled data across 22 robots and 21 institutions, showing positive transfer across embodiments rather than single-robot isolation [@openx2023rtx]. Octo made the generalist robot policy idea open-source [@octo2024policy]. OpenVLA showed that an open 7B VLA trained on diverse real-world demonstrations can be competitive with larger closed systems and practically fine-tunable [@kim2025openvla]. pi0 pushed the foundation-model framing into more dexterous and varied real-world control [@black2025pi0]. Surveys of robotics with foundation models make clear that this is now a major research direction rather than a fringe project [@xu2024roboticsfm].

Still, embodiment should not be mystified. Not every useful AI system needs a humanoid body. A CAD copilot, a theorem assistant, and a scheduling optimizer do not become more intelligent merely because they are mounted on wheels. Embodiment matters most when tasks are closed-loop, irreversible, safety-critical, or contact-rich. It matters when perception and action co-determine each other. In those contexts, text-only competence is a weak proxy for intelligence.

The biological examples sharpen the point if used carefully. Paramecium is a striking case of minimal embodied intelligence: a unicellular organism with no nervous system, yet with sensorimotor behavior tied to electrical excitability, ciliary control, and adaptive movement in an environment [@brette2021paramecium]. Amoebae are even more provocative. A 2019 Nature Communications study reported motility patterns consistent with associative conditioned behavior in Amoeba proteus, which should be treated as suggestive rather than as a final verdict on "cellular learning" [@delafuente2019amoeba]. Later work in PNAS Nexus continued to frame directed cell migration as a systemic, self-organized behavior that cannot be reduced to one molecular switch [@delafuente2024migration]. These organisms are pedagogically useful because they show that adaptive, environment-coupled behavior begins below brains.

At the opposite end, crows and dolphins show that sophisticated cognition is not confined to primates. New Caledonian crows manufacture hooked tools in the wild, and later experiments showed compound tool construction under novel conditions [@hunt1996crows; @vonbayern2018compoundcrows]. Bottlenose dolphins showed classic mirror self-recognition-style behavior in a now canonical PNAS study [@reiss2001dolphin]. The lesson is not that robots are about to become animal minds. The lesson is that intelligence is biologically plural. Bodies, niches, and action loops matter.

My extension of the argument is this: embodiment is necessary for robust physical agency, but it is not obviously necessary for every economically important form of AI competence. The mistake is to universalize from the robotics case. The stronger and cleaner claim is domain-specific: whenever the world can push back through physics, friction, delay, occlusion, or damage, embodiment ceases to be optional.

## 6. ASI as a technical and social idea

Artificial superintelligence is one of the least disciplined terms in public AI discourse. Even AGI lacks a universally accepted operational benchmark. Morris et al. propose "Levels of AGI" as a taxonomy of performance, generality, and autonomy, but this is a framework for comparison, not a proof that any system has crossed a natural threshold [@morris2023levels]. Chollet's critique is even more fundamental: task performance alone is a poor measure of intelligence because skill can be purchased with priors, compute, and data; what matters is skill-acquisition efficiency under bounded experience and transfer [@chollet2019measure].

This matters because ASI rhetoric often skips directly from impressive task performance to species-level narratives. That jump is unjustified. No cited result in this chapter demonstrates a system with broad autonomous competence across open-ended digital and physical environments, stable self-improvement under weak oversight, and reliable goal alignment under superhuman capability. Those are separate requirements, and the literature does not yet show them together.

The most serious current work connected to ASI is not proof of ASI. It is oversight research motivated by the possibility that future systems may outstrip direct human supervision. Constitutional AI studies whether models can be shaped through explicit principle sets and AI-generated critique rather than only human feedback [@bai2022constitutional]. Weak-to-strong generalization studies whether weak supervisors can elicit some of the capabilities of stronger models, while explicitly showing that naive weak supervision leaves large gaps [@burns2023weaktostrong]. Kenton et al. study debate and consultancy protocols with weaker LLM judges supervising stronger LLM agents, finding that results depend strongly on the task and asymmetry structure rather than yielding a universal oversight solution [@kenton2024scalableoversight].

The engineering interpretation is severe. ASI is currently more useful as a stress test for evaluation, supervision, and governance than as a near-term engineering deliverable. It forces hard questions: how do we verify systems that outrun average human inspection? How do we retain accountability when the model's internal route to a decision is opaque? How do we keep optimization pressure from outrunning our ability to define acceptable behavior? These are worthwhile questions. They do not imply that ASI is around the corner.

Therefore the responsible way to teach ASI is neither ridicule nor prophecy. It is to state clearly that the evidentiary burden is extreme. Serious ASI claims would require convincing demonstrations of broad transfer, autonomous competence, continual adaptation, robust control under distribution shift, and scalable oversight under capability gaps. That threshold has not been met.

## 7. Engineering interpretation of the future

From an engineering perspective, the likely next decade is not a clean handoff from LLMs to one successor architecture. It is a diversification of the stack.

First, foundation models will remain important as interface and integration layers. They are already effective at translating among language, code, documents, policies, and software tools [@bommasani2021foundation; @yao2022react; @schick2023toolformer].

Second, neuro-symbolic methods will matter where explicit constraints, provenance, and verification are first-order requirements rather than nice-to-have properties [@besold2017nesy; @manhaeve2019deepproblog; @colelough2025nesyreview].

Third, world models will matter where action, prediction, and planning are central: robotics, autonomy, industrial process control, scientific simulators, and high-consequence decision support [@hafner2019planet; @hafner2020dreamer; @lecun2022path; @assran2025vjepa2].

Fourth, embodiment will matter where intelligence is inseparable from physical deployment: sensing, manipulation, navigation, maintenance, mobility, and human-robot interaction [@brooks1990elephants; @brohan2023rt2; @openx2023rtx; @kim2025openvla].

The less credible forecast is the one preferred by hype cycles: one architecture becomes universally intelligent, human oversight fades, and engineering collapses into prompting. The literature does not support that forecast. What it supports is a more demanding picture in which future AI systems become more heterogeneous and more infrastructure-like. They will require more careful interfaces, better evaluation, stronger guardrails, clearer deployment boundaries, and more responsibility at the system level.

This is why the instructor's slogan is not rhetoric but a design principle. Engineers stay above AI because engineers define the task, the objective, the interface, the allowable action space, the training distribution, the test protocol, the fail-safe behavior, the audit trail, and the accountability chain. AI can optimize within those boundaries. It does not absolve humans of setting them.

## 8. Final message

The frontier after current LLM systems is real. Neuro-symbolic AI, world models, embodiment, and oversight research all point to genuine unresolved questions. But the honest conclusion is plural and conditional.

Neuro-symbolic AI says that intelligence without explicit structure is often not enough.

World-model research says that prediction and planning over latent state may matter more than surface continuation when action matters.

Embodiment says that intelligence tested only in language is not the same as intelligence tested in the world.

ASI discourse says that capability talk without measurement and oversight is mostly theater.

The resulting engineering stance is straightforward. Study the frontier. Do not worship it. Use future-facing paradigms where they solve real problems. Reject grand claims that run ahead of evidence. Preserve the distinction between engineering usefulness and general-intelligence mythology.

**Regardless of paradigm, engineers stay above AI.**

## Distinction sheet

| Theme | Established | Strong hypothesis | Speculative |
|---|---|---|---|
| Current LLM systems | Powerful as language, code, retrieval, and tool-using system components | Better scaffolding can keep extending usefulness in many professional workflows | Text-only scaling alone yields robust general intelligence |
| Neuro-symbolic AI | Hybrid models can improve structured reasoning, explicit constraint handling, and interpretability in some domains | Constraint-aware hybrid systems will become more important in engineering-grade AI | Symbolic layers will generally replace deep learning as the dominant paradigm |
| World models | Learned latent dynamics help control and planning in RL and robotics | Abstract predictive state models are necessary for robust physical agency | JEPA-style world models are already a general replacement for autoregressive modeling |
| Embodiment | Physical interaction changes the data distribution and the competence required | Many capabilities central to robotics and autonomy require embodiment | Every useful future AI system must be embodied, preferably humanoid |
| AGI/ASI | There is no consensus operational benchmark for AGI or ASI | Oversight and evaluation will become harder as capability gaps widen | Near-term ASI is an established engineering forecast |

## BibTeX

```bibtex
@article{bommasani2021foundation,
  title={On the Opportunities and Risks of Foundation Models},
  author={Bommasani, Rishi and Hudson, Drew A. and Adeli, Ehsan and Altman, Russ and Arora, Simran and von Arx, Sydney and Bernstein, Michael S. and Bohg, Jeannette and Bosselut, Antoine and Brunskill, Emma and Brynjolfsson, Erik and others},
  journal={arXiv preprint arXiv:2108.07258},
  year={2021}
}

@article{yao2022react,
  title={ReAct: Synergizing Reasoning and Acting in Language Models},
  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  journal={arXiv preprint arXiv:2210.03629},
  year={2022}
}

@article{schick2023toolformer,
  title={Toolformer: Language Models Can Teach Themselves to Use Tools},
  author={Schick, Timo and Dwivedi-Yu, Jane and Dessi, Roberto and Raileanu, Roberta and Lomeli, Maria and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
  journal={arXiv preprint arXiv:2302.04761},
  year={2023}
}

@article{wang2023voyager,
  title={Voyager: An Open-Ended Embodied Agent with Large Language Models},
  author={Wang, Guanzhi and Xie, Yuqi and Jiang, Yunfan and Mandlekar, Ajay and Xiao, Chaowei and Zhu, Yuke and Fan, Linxi and Anandkumar, Anima},
  journal={arXiv preprint arXiv:2305.16291},
  year={2023}
}

@article{wang2023newton,
  title={NEWTON: Are Large Language Models Capable of Physical Reasoning?},
  author={Wang, Yi Ru and Duan, Jiafei and Fox, Dieter and Srinivasa, Siddhartha},
  journal={arXiv preprint arXiv:2310.07018},
  year={2023}
}

@article{qiu2025phybench,
  title={PHYBench: Holistic Evaluation of Physical Perception and Reasoning in Large Language Models},
  author={Qiu, Shi and Guo, Shaoyang and Song, Zhuo-Yang and Sun, Yunbo and Cai, Zeyu and Wei, Jiashen and others},
  journal={arXiv preprint arXiv:2504.16074},
  year={2025}
}

@article{besold2017nesy,
  title={Neural-Symbolic Learning and Reasoning: A Survey and Interpretation},
  author={Besold, Tarek R. and d'Avila Garcez, Artur and Bader, Sebastian and Bowman, Howard and Domingos, Pedro and Hitzler, Pascal and Kuehnberger, Kai-Uwe and Lamb, Luis C. and Lowd, Daniel and Lima, Priscila Machado Vieira and others},
  journal={arXiv preprint arXiv:1711.03902},
  year={2017}
}

@article{manhaeve2019deepproblog,
  title={Neural Probabilistic Logic Programming in DeepProbLog},
  author={Manhaeve, Robin and Dumancic, Sebastijan and Kimmig, Angelika and Demeester, Thomas and De Raedt, Luc},
  journal={Artificial Intelligence},
  volume={298},
  pages={103504},
  year={2021}
}

@article{dong2019nlm,
  title={Neural Logic Machines},
  author={Dong, Honghua and Mao, Jiayuan and Lin, Tian and Wang, Chong and Li, Lihong and Zhou, Denny},
  journal={arXiv preprint arXiv:1904.11694},
  year={2019}
}

@article{mao2019nscl,
  title={The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences From Natural Supervision},
  author={Mao, Jiayuan and Gan, Chuang and Kohli, Pushmeet and Tenenbaum, Joshua B. and Wu, Jiajun},
  journal={arXiv preprint arXiv:1904.12584},
  year={2019}
}

@article{colelough2025nesyreview,
  title={Neuro-Symbolic AI in 2024: A Systematic Review},
  author={Colelough, Brandon C. and Regli, William},
  journal={arXiv preprint arXiv:2501.05435},
  year={2025}
}

@article{ha2018worldmodels,
  title={World Models},
  author={Ha, David and Schmidhuber, J{\"u}rgen},
  journal={arXiv preprint arXiv:1803.10122},
  year={2018}
}

@article{hafner2019planet,
  title={Learning Latent Dynamics for Planning from Pixels},
  author={Hafner, Danijar and Lillicrap, Timothy and Fischer, Ian and Villegas, Ruben and Ha, David and Lee, Honglak and Davidson, James},
  journal={arXiv preprint arXiv:1811.04551},
  year={2019}
}

@article{hafner2020dreamer,
  title={Dream to Control: Learning Behaviors by Latent Imagination},
  author={Hafner, Danijar and Lillicrap, Timothy and Ba, Jimmy and Norouzi, Mohammad},
  journal={arXiv preprint arXiv:1912.01603},
  year={2020}
}

@article{hafner2025dreamerv3,
  title={Mastering Diverse Control Tasks through World Models},
  author={Hafner, Danijar and Pasukonis, Jurgis and Ba, Jimmy and Lillicrap, Timothy},
  journal={Nature},
  volume={640},
  pages={604--614},
  year={2025}
}

@misc{lecun2022path,
  title={A Path Towards Autonomous Machine Intelligence},
  author={LeCun, Yann},
  howpublished={OpenReview preprint},
  year={2022},
  note={Version 0.9.2}
}

@article{assran2023ijepa,
  title={Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture},
  author={Assran, Mahmoud and Duval, Quentin and Misra, Ishan and Bojanowski, Piotr and Vincent, Pascal and Rabbat, Michael and LeCun, Yann and Ballas, Nicolas},
  journal={arXiv preprint arXiv:2301.08243},
  year={2023}
}

@article{bardes2024vjepa,
  title={Revisiting Feature Prediction for Learning Visual Representations from Video},
  author={Bardes, Adrien and Garrido, Quentin and Ponce, Jean and Chen, Xinlei and Rabbat, Michael and LeCun, Yann and Assran, Mido and Ballas, Nicolas},
  journal={arXiv preprint arXiv:2404.08471},
  year={2024}
}

@article{garrido2024iwm,
  title={Learning and Leveraging World Models in Visual Representation Learning},
  author={Garrido, Quentin and Assran, Mahmoud and Ballas, Nicolas and Bardes, Adrien and Najman, Laurent and LeCun, Yann},
  journal={arXiv preprint arXiv:2403.00504},
  year={2024}
}

@article{assran2025vjepa2,
  title={V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning},
  author={Assran, Mido and Bardes, Adrien and Fan, David and Garrido, Quentin and Howes, Russell and Komeili, Mojtaba and Muckley, Matthew and Rizvi, Ammar and Roberts, Claire and Sinha, Koustuv and others},
  journal={arXiv preprint arXiv:2506.09985},
  year={2025}
}

@article{destrade2026valueguidedjepa,
  title={Value-guided Action Planning with JEPA World Models},
  author={Destrade, Matthieu and Bounou, Oumayma and Le Lidec, Quentin and Ponce, Jean and LeCun, Yann},
  journal={arXiv preprint arXiv:2601.00844},
  year={2026}
}

@article{brooks1990elephants,
  title={Elephants Don't Play Chess},
  author={Brooks, Rodney A.},
  journal={Robotics and Autonomous Systems},
  volume={6},
  number={1-2},
  pages={3--15},
  year={1990}
}

@article{brooks1991representation,
  title={Intelligence without Representation},
  author={Brooks, Rodney A.},
  journal={Artificial Intelligence},
  volume={47},
  number={1-3},
  pages={139--159},
  year={1991}
}

@article{brohan2022rt1,
  title={RT-1: Robotics Transformer for Real-World Control at Scale},
  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Dabis, Joseph and Finn, Chelsea and Gopalakrishnan, Keerthana and Hausman, Karol and others},
  journal={arXiv preprint arXiv:2212.06817},
  year={2022}
}

@article{brohan2023rt2,
  title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Driess, Danny and Finn, Chelsea and Hausman, Karol and Levine, Sergey and others},
  journal={arXiv preprint arXiv:2307.15818},
  year={2023}
}

@article{openx2023rtx,
  title={Open X-Embodiment: Robotic Learning Datasets and RT-X Models},
  author={Open X-Embodiment Collaboration},
  journal={arXiv preprint arXiv:2310.08864},
  year={2023}
}

@article{octo2024policy,
  title={Octo: An Open-Source Generalist Robot Policy},
  author={Octo Model Team and others},
  journal={arXiv preprint arXiv:2405.12213},
  year={2024}
}

@inproceedings{kim2025openvla,
  title={OpenVLA: An Open-Source Vision-Language-Action Model},
  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan P. and Sanketi, Pannag R. and Vuong, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
  booktitle={Proceedings of the 8th Conference on Robot Learning},
  pages={2679--2713},
  year={2025},
  publisher={PMLR}
}

@article{black2025pi0,
  title={{pi_0}: A Vision-Language-Action Flow Model for General Robot Control},
  author={Black, Kevin and others},
  journal={arXiv preprint arXiv:2410.24164},
  year={2025}
}

@article{xu2024roboticsfm,
  title={A Survey on Robotics with Foundation Models: toward Embodied AI},
  author={Xu, Zhiyuan and Wu, Kun and Wen, Junjie and Li, Jinming and Liu, Ning and Che, Zhengping and Tang, Jian},
  journal={arXiv preprint arXiv:2402.02385},
  year={2024}
}

@article{brette2021paramecium,
  title={Integrative Neuroscience of Paramecium, a "Swimming Neuron"},
  author={Brette, Romain},
  journal={eNeuro},
  volume={8},
  number={3},
  year={2021}
}

@article{delafuente2019amoeba,
  title={Evidence of Conditioned Behavior in Amoebae},
  author={De la Fuente, Ildefonso M. and Bringas, Carlos and Malaina, Iker and Fedetz, Maria and Carrasco-Pujante, Jose and Morales, Miguel and Knafo, Shira and Martinez, Luis and Perez-Samartin, Alberto and Lopez, Jose I. and Perez-Yarza, Gorka and Boyano, Maria Dolores},
  journal={Nature Communications},
  volume={10},
  pages={3690},
  year={2019}
}

@article{delafuente2024migration,
  title={Systemic Cellular Migration: The Forces Driving the Directed Locomotion of Amoebae},
  author={De la Fuente, Ildefonso M. and others},
  journal={PNAS Nexus},
  volume={3},
  number={5},
  pages={pgae171},
  year={2024}
}

@article{hunt1996crows,
  title={Manufacture and Use of Hook-Tools by New Caledonian Crows},
  author={Hunt, Gavin R.},
  journal={Nature},
  volume={379},
  pages={249--251},
  year={1996}
}

@article{vonbayern2018compoundcrows,
  title={Compound Tool Construction by New Caledonian Crows},
  author={von Bayern, Auguste M. P. and Danel, S. and Auersperg, A. M. I. and Mioduszewska, B. and Kacelnik, A.},
  journal={Scientific Reports},
  volume={8},
  pages={15676},
  year={2018}
}

@article{reiss2001dolphin,
  title={Mirror Self-Recognition in the Bottlenose Dolphin: A Case of Cognitive Convergence},
  author={Reiss, Diana and Marino, Lori},
  journal={Proceedings of the National Academy of Sciences},
  volume={98},
  number={10},
  pages={5937--5942},
  year={2001}
}

@article{chollet2019measure,
  title={On the Measure of Intelligence},
  author={Chollet, Francois},
  journal={arXiv preprint arXiv:1911.01547},
  year={2019}
}

@article{morris2023levels,
  title={Levels of AGI for Operationalizing Progress on the Path to AGI},
  author={Morris, Meredith Ringel and others},
  journal={arXiv preprint arXiv:2311.02462},
  year={2023}
}

@article{bai2022constitutional,
  title={Constitutional AI: Harmlessness from AI Feedback},
  author={Bai, Yuntao and Kadavath, Saurav and Kundu, Sandipan and Askell, Amanda and Kernion, Jackson and Jones, Andy and Chen, Anna and Goldie, Anna and Mirhoseini, Azalia and McKinnon, Cameron and others},
  journal={arXiv preprint arXiv:2212.08073},
  year={2022}
}

@article{burns2023weaktostrong,
  title={Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision},
  author={Burns, Collin and Izmailov, Pavel and Kirchner, Jan Hendrik and Baker, Bowen and Gao, Leo and Aschenbrenner, Leopold and Chen, Yining and Ecoffet, Adrien and Joglekar, Manas and Leike, Jan and Sutskever, Ilya and Wu, Jeff},
  journal={arXiv preprint arXiv:2312.09390},
  year={2023}
}

@article{kenton2024scalableoversight,
  title={On Scalable Oversight with Weak LLMs Judging Strong LLMs},
  author={Kenton, Zachary and Siegel, Noah Y. and Kramar, Janos and Brown-Cohen, Jonah and Albanie, Samuel and Bulian, Jannis and Agarwal, Rishabh and Lindner, David and Tang, Yunhao and Goodman, Noah D. and Shah, Rohin},
  journal={arXiv preprint arXiv:2407.04622},
  year={2024}
}
```
