# SKILL: Lecture Note to Custom Beamer Slide Generator

## Description
This skill converts academic lecture notes (LaTeX, PDF, or text) into a comprehensive, long-form Beamer slide deck. It utilizes specific user-provided style files (`.sty`) to apply semantic formatting and follows a rigorous three-phase generation process to ensure depth, accuracy, and valid syntax. When the input is a TeX lecture source, the workflow must write the generated Beamer source to a real file on disk named `slides/TopicXX-slides.tex`; returning LaTeX only in chat is not sufficient.

## Input Requirements
1.  **Source Content:** The lecture notes, preface, or chapter text to be converted (e.g., `TopicChapters/Topic13.tex`).
2.  **Style Definition:** Use the local style file at `slides/ceai-beamer.sty` for the Beamer theme and semantic boxes.
3.  **Template/Metadata:** (Optional) A template file containing title, author, and institute details.
4.  **TeX Source Rule:** If the source content is a `.tex` lecture file, derive the matching output name (e.g., `TopicChapters/Topic13.tex` → `slides/Topic13-slides.tex`) and write the generated Beamer source file to that path in the workspace.

## Processing Instructions

### 1. Analysis Phase
* **Analyze Source Content:** Read the full text. Do not summarize heavily; aim to preserve the logical flow and specific details.
* **Analyze Style Definitions:** Parse `slides/ceai-beamer.sty` to identify custom environments (especially `tcolorbox` definitions: `conceptbox`, `examplebox`, `warningbox`) and convenience macros (`\ConceptFrame`, `\BulletFrame`, `\bhref`) to use for semantic highlighting.
* **Evidence Planning:** Identify statements that warrant external corroboration (definitions, historical claims, statistics, formal terms). For each, plan a credible citation source.

### 2. Three-Phase Generation Process
To create the final deck, follow these three distinct conceptual phases:

* **Phase A: Structure & Basic Content (The "36–50 Slide" Target)**
    * Map the source text to a sequence of approximately 36–50 slides, depending on source length and density.
    * Identify the main bullet points for each slide.
    * Ensure the narrative arc matches a standard "long class" or full chapter coverage.
    * **Multi-Part Handling:** If the source is exceptionally long (e.g., >60 slides needed), split into parts: `slides/TopicXX-slides-part01.tex`, `slides/TopicXX-slides-part02.tex`, etc. Each part should be independently compilable with its own preamble and title page.

* **Phase B: Detail Expansion & Refinement**
    * *Self-Correction/Expansion:* Take the basic bullets from Phase A and expand them into **complete sentences** or detailed sub-bullets.
    * *Completeness Check:* Compare against the source text to ensure no key technical details were missed.
    * *Overflow Handling:* If a slide becomes too text-heavy (too many sub-bullets), split it into multiple slides. Use the title format: `Title` followed by `Title (Continued...)`.

* **Phase C: Visual Augmentation**
    * Identify complex concepts, flows, or systems that require visualization.
    * **Create Extra Slides:** Insert new slides specifically for these visuals.
    * **Figure-First Rule:** When a source figure is referenced in lecture notes, create a real `figure` environment with `\includegraphics{<filename>}`. The `ceai-beamer.sty` already sets `\graphicspath{{../figs/}{./figs/}}`, so use only the bare filename (e.g., `Topic13fig01.png`) — do NOT prepend `../figs/` or `figs/`.
    * **No Placeholders:** Never use `[Figure Placeholder]` text. If the image file is unavailable locally, still emit the `\includegraphics` with the correct filename so it resolves when the file is present.

### 3. Evidence and Citation Augmentation
* **Scope:** Provide corroborating citations for definitions, historical claims, and factual assertions that are not purely conceptual.
* **Source Quality:** Prefer .gov and .edu sources; Wikipedia is acceptable for general definitions if no primary sources are available. Avoid blogs and low-credibility sources.
* **Citation Placement:** Use the established `\source{}` macro pattern. Define it in the preamble as:
  ```latex
  \newcommand{\source}[1]{\vspace{0.4em}{\tiny\color{gray}Source: #1\par}}
  ```
  Then use it at the bottom of frames: `\source{\href{https://example.com}{Descriptive Label}}`.
* **Minimum Coverage:** Aim for at least one credible citation per major subsection when the content contains factual claims.
* **No Fabrication:** Do not invent citations. Only include links that are directly relevant and verifiable.

### 4. Verification Step (Crucial)
Before outputting the final code, perform a syntax integrity check:
* **Brace Balance:** Verify that every opening brace `{` has a corresponding closing brace `}`.
* **Environment Balance:** Ensure every `\begin{...}` has a matching `\end{...}`.
* **Artifact Removal:** Scan for and remove any AI processing tags such as `<antThinking>`, `</antThinking>`, or `[OUTPUT NOT AVAILABLE]`.
* **Style Check:** Ensure custom boxes (e.g., `conceptbox`) are used correctly according to the `.sty` definition.
* **Citation Check:** Verify that every citation is reachable and relevant to the associated statement.
* **Output File Check:** Verify that the generated Beamer source has been written to the required `slides/TopicXX-slides.tex` path when the input is a TeX lecture source.

### 5. Formatting & Styling
* **Semantic Boxing:** Use specific boxes defined in the `.sty` (e.g., `conceptbox` for definitions, `examplebox` for engineering applications, `warningbox` for limitations/pitfalls) instead of generic lists.
* **Text Alignment:** Use `\usepackage{ragged2e}` and apply `\justifying` globally via:
  ```latex
  \AtBeginEnvironment{frame}{\justifying}
  ```
  This eliminates the need to repeat `\justifying` inside every frame. Individual frames can still override if needed.
* **Preamble:** Ensure all necessary packages are loaded. The `ceai-beamer.sty` already loads `amsmath`, `amsfonts`, `amssymb`, `graphicx`, `tikz`, `tcolorbox`, `booktabs`, `array`, `bm`, `pgfpages`, and `etoolbox`. Only add packages not covered by the style file.
* **Document Class:** Use `\documentclass[10pt]{beamer}` or `\documentclass[12pt]{beamer}`. Do NOT use the `german` option unless the content is in German.
* **Citation Styling:** Keep citations compact using the `\source{}` macro and avoid visual clutter.
* **Missing-Figure Handling:** If image files are unavailable locally, keep the original `\includegraphics{...}` with the bare filename; do not use text placeholders.

### 6. Handout Generation
* **Automatic:** After the slide PDF is produced, call the local tool `skills/slides2handout.py` to generate a handout PDF.
* **Default:** Use the same input slide PDF and write a sibling file named with a `-handout` suffix (e.g., `Topic13-slides.pdf` → `Topic13-slides-handout.pdf`).
* **Tool Invocation:** Run `python3 skills/slides2handout.py <slides.pdf> <slides-handout.pdf>` using default layout parameters unless the user requests overrides.
* **Dependencies:** The script requires `pypdf` and `reportlab`. If missing, install via `pip install pypdf reportlab`.

### 7. Compilation (Slides PDF)
* **Style File:** Always include `\usepackage{ceai-beamer}` in the preamble, relying on `slides/ceai-beamer.sty`.
* **Source Filename Rule:** The generated Beamer source file must be named `slides/TopicXX-slides.tex` (for example, `slides/Topic13-slides.tex`).
* **Materialization Rule:** Given a TeX source file, do not stop after producing a LaTeX snippet in the response. You must create or overwrite the corresponding `slides/TopicXX-slides.tex` file in the workspace before compilation.
* **Build Output:** Compile the generated `.tex` into a `*-slides.pdf` using local `pdflatex` or `lualatex`.
* **Compilation Retries:** Run the compiler **at least twice** to resolve cross-references, TOC entries, and navigation. Typical sequence:
  ```bash
  cd slides && pdflatex TopicXX-slides.tex && pdflatex TopicXX-slides.tex
  ```
* **Tool Availability:** If neither `pdflatex` nor `lualatex` exists in the environment, ask for permission before installing a LaTeX toolchain.

## Output Structure
The workflow must create and verify real output files in the workspace. For a TeX lecture source, the minimum required artifacts are:
1.  A generated Beamer source file written to `slides/TopicXX-slides.tex`.
2.  That source file must be a complete, compilable LaTeX document containing:
    * Preamble (with `\documentclass`, `\usepackage{ceai-beamer}`, `\usepackage{ragged2e}`, `\AtBeginEnvironment{frame}{\justifying}`, `\newcommand{\source}[1]{...}`).
    * Metadata (Title, Author, Date).
    * `\begin{document}`.
    * Front matter (Title page, TOC).
    * The generated slides (Frames), including citations as required.
    * `\end{document}`.
3.  A compiled `*-slides.pdf` produced via `pdflatex` or `lualatex` (run at least twice).
4.  A handout PDF generated via `skills/slides2handout.py` from the produced slide PDF, unless the user explicitly says not to generate the handout.
5.  The response should reference the created file paths, but path references do not replace the requirement to write the files.

## Example Interaction

**User:**
"Generate slides for Topic 13. Use `ceai-beamer.sty`."

**AI Response:**
(Internal thought process: Read TopicChapters/Topic13.tex → Map to ~40 slides → Expand to full sentences → Write `slides/Topic13-slides.tex` → Verify braces → Compile PDF twice → Generate handout)

```latex
\documentclass[10pt]{beamer}
\usepackage{ceai-beamer}
\usepackage{ragged2e}
\AtBeginEnvironment{frame}{\justifying}

\title[Topic 13: Deep Neural Networks]{CE 488/5588: Applied AI\\Topic 13: Deep Neural Networks --- Foundations \& Architectures}
\author{}
\date{}

\newcommand{\source}[1]{\vspace{0.4em}{\tiny\color{gray}Source: #1\par}}

\begin{document}

\begin{frame}[plain]
  \titlepage
\end{frame}

\begin{frame}{Lecture Roadmap}
  \tableofcontents
\end{frame}

\section{Why Deep Learning Works Now}

\begin{frame}{From Classical ML to Deep Learning}
  Topics 1--12 covered classical machine learning: regression, classification, SVMs, and clustering. These are data-driven, small-to-medium-scale models that function as reusable, well-characterized operators.

  Starting here, we enter the post-2020 era: deep neural networks that learn hierarchical representations, foundation models trained on web-scale corpora, and generative systems that create rather than classify.

  \begin{conceptbox}{The Key Question}
    Neural networks have existed since the 1980s. What changed in 2012 that made them suddenly practical?
  \end{conceptbox}
\end{frame}

\begin{frame}{The Perceptron Model}
  The perceptron represents the simplest form of a neural network unit.

  \begin{conceptbox}{Definition}
    A perceptron takes a vector of real-valued inputs, calculates a linear combination of these inputs, and outputs a 1 if the result exceeds some threshold.
  \end{conceptbox}

  \begin{itemize}
    \item It mimics the activation of a biological neuron.
    \item \textbf{Limitation:} Single perceptrons can only solve linearly separable problems (e.g., they cannot solve XOR).
  \end{itemize}

  \source{\href{https://en.wikipedia.org/wiki/Perceptron}{Wikipedia: Perceptron}}
\end{frame}

\begin{frame}{Visualizing the Convolution Operation}
  \begin{figure}
    \centering
    \includegraphics[width=0.6\textwidth]{Topic13fig02.png}
    \caption{The convolution operation: a $3 \times 3$ filter slides across the input.}
  \end{figure}

  The filter weights are learned during training, not hand-crafted.
\end{frame}

\end{document}
```
