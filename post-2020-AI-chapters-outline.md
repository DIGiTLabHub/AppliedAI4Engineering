# Post-2020 AI Chapters Outline

## Course: CE 488/5588 — Applied AI for Engineers

---

## Narrative Arc

The pre-2020 chapters (Topics 01–12) covered classical machine learning: regression, classification, SVMs, Bayesian methods, clustering, and dimensionality reduction. These are **data-driven, small-to-medium-scale models** that function as reusable, well-characterized operators.

The post-2020 chapters (Topics 13–19) transition to the **Generative AI era**: deep neural networks that learn hierarchical representations, foundation models trained on web-scale corpora, and agentic systems that plan, retrieve, and act. The emphasis remains **introductory and conceptual** — engineering students gain literacy in what these systems do, why they work, where they fail, and how they are applied in practice, rather than mathematical derivation or low-level implementation.

### Design Principles

1. **Bridge from classical to modern** — Topic 13 starts with "why now?" to answer the implicit question: *We had neural networks since the 1980s. Why did they suddenly work in 2012?*
2. **High-level math, intuitive geometry** — Equations are presented as explanatory tools, not gatekeepers. Focus on geometric intuition and conceptual understanding.
3. **Engineering thread throughout** — Every topic includes at least one civil/engineering application example.
4. **Reuse existing content** — Topic 15/17 (LLM intro, NLP history, prompt engineering) and Topic 16/20 (GOFAI) and Topic 18/22 (LeCun) have draft content to be reorganized and integrated.
5. **Critical perspective** — Not hype. Students learn capabilities AND limitations, including the token-driven nature of current GenAI and the gap toward embodied intelligence.

---

## Chapter-by-Chapter Breakdown

### Topic 13: Deep Neural Networks — Foundations & Architectures

**Purpose:** The bridge from classical ML to modern deep learning. Answers why DNNs became practical and introduces the three architectures that define the post-2020 era.

**Sections:**

1. **Introduction & Learning Objectives**
   - From MLPs (covered earlier) to deep networks
   - What changed: data, compute, algorithms

2. **Why Deep Neural Networks Work Now: The Numerical Secrets**
   - The vanishing gradient problem (why early networks failed to train deep)
   - **ReLU and activation functions**: ReLU, Leaky ReLU, GELU — why non-linearity matters and why ReLU solved vanishing gradients
   - **Weight initialization**: Xavier/Glorot, He initialization — starting in the right regime
   - **Batch Normalization**: stabilizing internal covariate shift, allowing higher learning rates
   - **Optimization advances**: SGD → Momentum → RMSProp → Adam — adaptive learning rates
   - **Regularization**: Dropout, weight decay, early stopping — preventing overfitting in over-parameterized models
   - **The double descent phenomenon**: why over-parameterized networks generalize
   - Geometric intuition: loss landscapes, saddle points, and the role of depth

3. **Convolutional Neural Networks (CNNs)**
   - The convolution operation: learned feature extraction vs. hand-crafted filters
   - Convolutional layers, pooling, strides, padding
   - Architecture evolution (brief): LeNet → AlexNet → VGG → ResNet (skip connections)
   - Why CNNs dominate vision: translation equivariance, parameter sharing, hierarchical features
   - Engineering applications: crack detection in concrete, structural damage classification, construction progress monitoring from images

4. **Transformers**
   - From RNNs/LSTMs to attention: the sequential bottleneck
   - Self-attention mechanism: $Q, K, V$ formulation, scaled dot-product attention
   - Multi-head attention: parallel feature extraction
   - Positional encoding: injecting sequence order
   - Encoder vs. Decoder vs. Encoder-Decoder architectures
   - Why Transformers replaced RNNs: parallelization, long-range dependencies, scalability
   - Engineering applications: time-series forecasting from sensor data, document understanding

5. **Diffusion Models (Introduction)**
   - The intuition: learning to reverse a noise-adding process
   - Forward process (gradual noising) and reverse process (denoising)
   - Connection to score matching and Langevin dynamics (high-level)
   - Why diffusion outperformed GANs in generation quality and training stability
   - Engineering applications: synthetic data generation for rare events

6. **Summary & Comparison of Architectures**
   - CNNs: spatial hierarchies (images, grids)
   - Transformers: sequence and relationship modeling (text, time-series, graphs)
   - Diffusion: generative modeling (images, audio, design)
   - When to use which

---

### Topic 14: Deep Learning for Generation — GANs, VAEs, and Diffusion in Practice

**Purpose:** Deep dive into generative architectures, their trade-offs, and engineering applications.

**Sections:**

1. **Introduction to Generative Deep Learning**
   - Discriminative vs. generative models (review)
   - What makes a "good" generative model: sample quality, diversity, training stability

2. **Generative Adversarial Networks (GANs)**
   - Generator vs. Discriminator: the minimax game
   - Nash equilibrium intuition
   - Training dynamics and instability
   - Mode collapse: what it is and why it matters
   - Architecture evolution: DCGAN → StyleGAN
   - Engineering applications: synthetic structural images, data augmentation for rare damage types

3. **Variational Autoencoders (VAEs)**
   - Autoencoder review: encoding → latent space → decoding
   - The probabilistic twist: learning a distribution over latent space
   - KL divergence intuition: balancing reconstruction and regularization
   - Latent space interpolation: smooth generation
   - Engineering applications: dimensionality reduction with generative capability, anomaly detection

4. **Diffusion Models (Deep Dive)**
   - DDPM (Denoising Diffusion Probabilistic Models): step-by-step denoising
   - Classifier-free guidance: controlling generation with text prompts
   - Stable Diffusion: latent diffusion, U-Net backbone, CLIP text encoder
   - Text-to-image, image-to-image, inpainting
   - Engineering applications: design concept generation, visualization of structural scenarios

5. **Comparison & Trade-offs**
   - GANs: fast generation, hard to train, mode collapse
   - VAEs: stable training, blurry outputs, explicit latent space
   - Diffusion: high quality, slow generation, controllable
   - Emerging hybrids: GAN-diffusion, consistency models

6. **Conclusion**

---

### Topic 15: From NLP to Large Language Models

**Purpose:** The historical and technical path from classical NLP to modern LLMs. Reorganizes and consolidates existing Topic 15/17 content.

**Sections:**

1. **Introduction: Why Language?**
   - Language as the interface to human knowledge
   - From task-specific models to general-purpose foundation models

2. **Classical NLP: Pre-Transformer Era** *(reuse existing content)*
   - Weaver's Memorandum (1949) and the noisy-channel view
   - Rule-based and linguistic models (Chomsky, expert systems)
   - Statistical NLP: n-grams, HMMs, IBM Models 1–5, phrase-based SMT
   - Neural NLP emergence: RNNs, LSTMs, Seq2Seq with Attention
   - Historical timeline table

3. **Tokenization: The Bridge from Text to Numbers**
   - Why tokenization matters: vocabulary size vs. coverage trade-off
   - Word-level, character-level, subword tokenization
   - Byte-Pair Encoding (BPE): algorithm and example
   - WordPiece, SentencePiece (brief mention)
   - Engineering implication: how tokenization affects domain-specific terms (engineering jargon, chemical formulas)

4. **Embeddings: Representing Meaning as Vectors**
   - From one-hot to dense embeddings
   - Word2Vec, GloVe (brief historical context)
   - Contextual embeddings: the key innovation
   - Embedding dimension and sparsity: why large $d$ matters
   - Manifold concentration: token vectors lie on a low-dimensional manifold

5. **The Transformer Architecture**
   - Self-attention: $Q, K, V$ formulation with math
   - Multi-head attention: parallel representation subspaces
   - Feedforward networks and residual connections
   - Layer normalization: training stability
   - Encoder-only (BERT), Decoder-only (GPT), Encoder-Decoder (T5)
   - Why GPT-style (decoder-only) dominates today

6. **Pre-training & Fine-tuning**
   - Next-token prediction objective
   - Scale laws: parameters, data, compute
   - Fine-tuning: supervised adaptation
   - Parameter-efficient methods: LoRA, adapters
   - Table: major LLMs and benchmark performance (MMLU)

7. **Inference & Generation**
   - Autoregressive decoding loop
   - Decoding strategies: greedy, beam search, top-$k$, nucleus (top-$p$)
   - Temperature scaling
   - Context windows and their limits

8. **Key Properties & Limitations**
   - Strengths: zero/few-shot learning, in-context adaptation, large context
   - Limitations: hallucinations, bias, fixed context, training cost
   - Ongoing challenges: interpretability, continual learning, alignment

9. **Conclusion**

---

### Topic 16: LLMs in Practice — Capabilities, Limits, and Prompt Engineering

**Purpose:** Practical understanding of how to work with LLMs effectively and responsibly.

**Sections:**

1. **Introduction: Beyond the Hype**
   - What LLMs actually do: pattern completion, not symbolic reasoning
   - Inductive vs. deductive reasoning (reuse existing content)
   - The nature of knowledge in LLMs: distributed across parameters, not stored as facts

2. **Knowledge Representation in LLMs**
   - Implicit vs. symbolic knowledge (comparison table)
   - Why outputs are hard to trace: no discrete "fact table"
   - Model editing: ROME, MEMIT (brief mention)
   - Engineering implication: verification is non-negotiable

3. **Prompt Engineering Workflow**
   - Define objective → Provide context → Set constraints → Add examples → Iterate
   - Best practices: clarity, step-by-step, positive/negative examples, output structure
   - Few-shot vs. zero-shot prompting
   - Common pitfalls: ambiguity, excessive context, contradictory instructions

4. **Advanced Prompting Techniques**
   - Chain-of-Thought (CoT): revealing intermediate reasoning steps
   - Zero-shot CoT: "Let's think step by step"
   - Tree-of-Thought, self-consistency (brief mention)
   - Structured output: JSON schemas, function calling

5. **Retrieval-Augmented Generation (RAG)**
   - The hallucination problem and why grounding matters
   - RAG architecture: retrieval → augmentation → generation
   - Retrieval methods: BM25 (sparse), FAISS/embeddings (dense)
   - Engineering applications: code/standards lookup, document Q&A, compliance checking
   - Tools: LangChain, LlamaIndex

6. **Temperature, Decoding, and Control**
   - How temperature affects output diversity
   - When to use deterministic (low temp) vs. creative (high temp) settings
   - Top-$p$ and top-$k$ for controlled randomness

7. **Limitations & Responsible Use**
   - Hallucinations: plausible but false outputs
   - Bias: training data reflects societal biases
   - Context limits: what happens when information exceeds the window
   - Cost and latency: practical deployment considerations
   - Engineering responsibility: verification, documentation, human-in-the-loop

8. **Conclusion & Hands-On Exercises**
   - Prompt design exercises
   - Build a RAG pipeline for engineering documents
   - Explore parameter-efficient fine-tuning (LoRA)

---

### Topic 17: AI Agents — From Foundation Models to Action

**Purpose:** Understanding how LLMs become agents that perceive, reason, and act.

**Sections:**

1. **Introduction: What Is an AI Agent?**
   - From passive model to active system
   - The agent loop: perception → reasoning → action → feedback
   - Classical agents (RL, planning) vs. LLM-based agents

2. **Core Components of an LLM Agent**
   - **LLM as the "brain"**: reasoning, planning, decision-making
   - **Memory**:
     - Short-term: context window, conversation history
     - Long-term: vector stores, knowledge graphs
   - **Tools / Function Calling**:
     - What is tool calling: structured API invocation from natural language
     - Common tools: web search, code execution, database queries, calculators
   - **Planning**:
     - Task decomposition
     - ReAct paradigm: Reasoning + Acting
     - Self-reflection and correction

3. **Agent Architectures**
   - Single-agent: one LLM with tools and memory
   - Multi-agent: specialized agents collaborating
   - Supervisor/worker patterns
   - Debate and consensus mechanisms

4. **Engineering Applications of Agents**
   - Design assistant: code generation for structural analysis, parameter exploration
   - Code review agent: automated PR review, testing suggestions
   - Compliance checker: code/standards lookup with verification
   - Data analysis agent: sensor data interpretation, anomaly investigation

5. **Challenges & Limitations**
   - Reliability: agents can make cascading errors
   - Cost: multiple LLM calls per task
   - Security: tool access control, prompt injection
   - Evaluation: how do you know an agent is working correctly?
   - Engineering responsibility: accountability in automated workflows

6. **Conclusion**

---

### Topic 18: Agentic Workflows & Modern AI Engineering

**Purpose:** Systems-level understanding of how agents are orchestrated into production workflows.

**Sections:**

1. **Introduction: From Single Prompts to Workflows**
   - Why single prompts are insufficient for complex tasks
   - Workflow patterns as engineering design patterns for AI

2. **Workflow Patterns**
   - **Sequential**: step-by-step pipeline
   - **Routing**: conditional branching based on LLM classification
   - **Parallel**: independent tasks executed concurrently
   - **Evaluator-Optimizer**: generate → critique → revise loop
   - **Orchestrator-Workers**: central planner delegates to specialists

3. **Orchestration Frameworks**
   - LangChain: chains, agents, tools
   - LlamaIndex: data indexing and retrieval pipelines
   - CrewAI, AutoGen: multi-agent frameworks
   - Comparison: when to use which

4. **Human-in-the-Loop Design**
   - Where humans should intervene: verification, approval, exception handling
   - Designing for oversight: traceability, audit trails, decision logs
   - The "engineering in the loop" paradigm

5. **Evaluation of Agent Systems**
   - Why evaluation is harder than for classical ML
   - Metrics: task completion rate, correctness, efficiency, cost
   - Benchmark suites (AgentBench, WebArena)
   - Engineering-specific evaluation: does the output meet code requirements?

6. **Prompt/Harness Engineering Beyond Chat**
   - System prompts: setting behavior and constraints
   - Structured prompts: templates, variables, conditionals
   - Prompt versioning and testing
   - Prompt as code: treating prompts as software artifacts

7. **Engineering Responsibility in Agentic Systems**
   - Accountability: who is responsible when an agent makes an error?
   - Documentation: prompts, data sources, assumptions, tool calls
   - Independent checks: redundancy for safety-critical outputs
   - NIST AI RMF and ASCE policy guidance (tie back to Topic 00)

8. **Conclusion**

---

### Topic 19: The Future — Limitations, Embodied Intelligence, and AI in Civil Engineering

**Purpose:** Critical synthesis of where GenAI stands today, its fundamental limitations, and a forward-looking vision for AI in civil engineering practice.

**Sections:**

1. **Introduction: Taking Stock**
   - What we've covered: from classical ML to agentic workflows
   - The current state of AI: impressive but incomplete

2. **Fundamental Limitations of Current GenAI** *(author's critical perspective)*
   - **Token-driven intelligence**: the entire GenAI paradigm — from LLMs to agentic workflows — operates through text tokens. This is a profound architectural constraint: no direct sensorimotor grounding, no physical-world interaction, no embodied experience. Everything is mediated through language.
   - **No survival mechanism**: biological intelligence is driven by survival — an active, pursuit-like learning imperative. Current AI has no equivalent. It does not *need* to learn; it is trained. This absence of intrinsic drive may be a fundamental barrier to human-level competence.
   - **No intrinsic motivation**: learning is entirely externally supervised (next-token prediction, RLHF, reward models). There is no self-directed curiosity, no goal formation, no autonomous problem identification.
   - **Static knowledge**: training is a one-time event. Models do not continuously learn from experience in deployment. Knowledge is frozen at training time.
   - **Simulation vs. reality**: models trained on human-generated data inherit human blind spots, biases, and gaps. They cannot discover what humans have not yet recorded.
   - **Reasoning vs. pattern matching**: the ongoing debate — do LLMs "understand" or merely "predict"? Evidence suggests the latter, with emergent behaviors that *resemble* reasoning but lack causal grounding.

3. **The Gap Toward Embodied Intelligence**
   - What embodied intelligence means: perception → action → learning loop in physical environments
   - Why language alone is insufficient for physical-world competence
   - Current approaches: robotics + LLMs, vision-language-action models
   - The challenge: grounding symbols in physical reality

4. **LeCun's Vision and Its Current Limits**
   - JEPA (Joint Embedding Predictive Architecture): world models through self-supervised video learning
   - The objective: learning physics and causality from observation
   - Current limitations: still early, video-based self-supervision is nascent
   - Comparison with autoregressive LLMs: prediction vs. understanding
   - LeCun's lectures and resources (reuse existing Topic 18/22 content)

5. **Neuro-Symbolic Integration**
   - Combining statistical learning with symbolic reasoning (tie back to Topic 16 GOFAI)
   - Why hybrid systems may be necessary for engineering-grade AI
   - Current frameworks: LogicTensorNetworks, DeepProbLog
   - The challenge: differentiable logic, constraint satisfaction

6. **AI in Civil Engineering: A Realistic Vision**
   - **Design phase**: highly amenable to GenAI and agentic workflows
     - Language-driven: design codes, modeling specifications, analysis reports are all text/structured data
     - AI-assisted (not fully automated): engineers in the loop, accelerated iteration
     - Concrete opportunities: code-compliant design generation, parametric exploration, documentation automation
   - **Beyond design** (construction, monitoring, retrofitting): much harder
     - Physical-world interaction requires embodied intelligence
     - Systems-level automation demands stronger, more reliable AI than current GenAI
     - Sensorimotor grounding, real-time decision-making, safety-critical verification
   - **The path forward**: hybrid systems combining classical ML (predictable, verifiable) with GenAI (flexible, generative) under engineering oversight

7. **Scaling, Compute, and Sustainability**
   - Scaling laws: do they continue indefinitely?
   - Energy and compute costs of training and inference
   - Open vs. closed models: accessibility and democratization
   - Edge AI: running models on-site, in the field

8. **AI Safety, Alignment, and Governance**
   - Alignment problem: ensuring AI objectives match human values
   - Safety in engineering contexts: verification, redundancy, fail-safes
   - Regulatory landscape: EU AI Act, US executive orders, professional society guidance
   - The engineer's role: not just users, but shapers of AI policy

9. **Conclusion: AI as the Fourth Pillar**
   - Revisiting Topic 00: AI and computation as the fourth pillar of engineering
   - What students should take away: literacy, critical judgment, responsible practice
   - The field is moving fast — the concepts here are foundations, not endpoints

---

## Content Reuse Map

| Existing File | Content | Target Topic |
|---|---|---|
| `Topic15.tex` / `Topic17.tex` | NLP history, transformer math, tokenization, embeddings, prompt engineering, RAG, CoT | Topics 15, 16 |
| `Topic16.tex` / `Topic20.tex` | GOFAI, expert systems, neuro-symbolic integration | Topic 16 (section 2), Topic 19 (section 5) |
| `Topic18.tex` / `Topic22.tex` | LeCun video links and resources | Topic 19 (section 4) |
| `Topic13.tex` | Empty shell — to be written | Topic 13 |
| `Topic14.tex` | Empty shell — to be written | Topic 14 |

## Writing Style Guide (Consistent with Topics 01–12)

- **Document class**: `\documentclass[12pt]{article}` with `\usepackage{ceai}`
- **Spacing**: `\doublespacing`
- **Structure**: `\section{}`, `\subsection{}`, `\subsubsection{}`
- **Learning objectives**: bulleted list at the start of each topic
- **Math**: high-level, intuitive, with geometric interpretation where possible
- **Figures**: `\includegraphics` with descriptive captions, courtesy attributions
- **Engineering applications**: woven into each major section
- **Conclusion**: summary of key takeaways
- **Bibliography**: `\bibliographystyle{unsrturl}`, `.bib` file in `TopicChapters/`

## Implementation Order

1. **Topic 13** — DNN Foundations & Architectures (new content, highest priority)
2. **Topic 14** — Generative Deep Learning (new content)
3. **Topic 15** — NLP to LLMs (reorganize existing Topic 15/17 content)
4. **Topic 16** — LLMs in Practice (reorganize + extend existing content)
5. **Topic 17** — AI Agents (new content)
6. **Topic 18** — Agentic Workflows (new content)
7. **Topic 19** — Future & Limitations (new content, synthesizes everything)
