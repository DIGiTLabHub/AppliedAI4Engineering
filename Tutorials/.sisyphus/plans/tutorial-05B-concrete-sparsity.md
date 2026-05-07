# Tutorial 05B: Concrete Strength — When Data Is Sparse

## TL;DR
> **Summary**: Create Tutorial05B.tex that guides students through OpenCode-based EDA of the UCI Concrete Compressive Strength dataset, confronting the fundamental challenge of sparse longitudinal data where each mixture-time combination may have only one observation.
> **Deliverables**: Tutorial05B.tex (LaTeX file), concrete-EDA.py (Python EDA script), concrete-sparsity-skill.md (Markdown SKILL artifact)
> **Effort**: Medium
> **Parallel**: YES - 2 waves
> **Critical Path**: Data exploration → sparsity discovery → physics discussion → SKILL creation

## Context
### Original Request
Create Tutorial 05B following Tutorial 05A (OpenCode basics). Students use OpenCode TUI to explore the UCI Concrete dataset and confront data sparsity challenges in supervised regression where time is a physical process, not just another feature.

### Interview Summary
- **Environment**: OpenCode TUI (Windows/WSL or Mac/iTerm2)
- **Depth**: Discussion only — no model implementation
- **Final artifact**: Markdown (.md) SKILL file capturing empirical knowledge
- **Key tension**: Age as feature vs. age as physical curing process

### Pedagogical Context — From Vibe Programming to Agentic Workflow
Previous ML/AI learning in this course relied on Google Colab with the built-in Gemini assistant. That workflow is easy to use and gives students a sense of ``vibe programming'' — type a question, get an answer, move on. The agent handles everything behind the scenes: installing libraries, running code, displaying results. Students are not bothered by the low-level mechanics, but they also don't see how those mechanics fit into knowledge discovery.

Tutorial 05B marks a deliberate shift. By switching to OpenCode, students encounter a **highly productive AI-agentic, human-in-the-loop workflow** where:
- **Tool calling is visible and explicit.** Students see the agent read files, run shell commands, and produce output — they watch the knowledge discovery process unfold step by step.
- **Low-level mechanics are still hidden, but now they are *accountable*.** Students don't need to `pip install pandas` themselves, but they are aware that an agent is doing it on their behalf — and that this agent is ``in flight'' with their exploration. This builds meta-cognitive awareness of what the agent is doing and why.
- **Students learn to direct, not just ask.** The tutorial teaches students to formulate structured prompts that guide the agent through systematic exploration, rather than vague ``tell me about this data'' requests. This is the transition from chat-based AI to agentic workflow.
- **The SKILL artifact captures empirical knowledge.** After exploring the data, students create a reusable Markdown skill that codifies what they learned — transforming a one-off exploration into reusable expertise for future sparse longitudinal datasets.

This shift is the core learning objective of Tutorial 05B: students should appreciate that working with an AI coding agent is not just about getting answers faster — it is about developing a new way of thinking about how tools, data, and domain knowledge interact in the discovery process.

### Metis Review (gaps addressed)
- **Scope guardrail**: Explicitly exclude model implementation, cross-validation
- **Student guidance**: Provide concrete OpenCode prompts students should type
- **SKILL template**: Define exact structure for the Markdown artifact
- **Data path**: Use relative path from tutorial project directory
- **Prerequisites**: Students must have completed Tutorial 05A (OpenCode installed)

## Work Objectives
### Core Objective
Create a tutorial that teaches students to use OpenCode for exploratory data analysis on sparse longitudinal data, confronting the gap between statistical supervision and physical reality.

### Deliverables
1. **Tutorial05B.tex** — LaTeX tutorial document (ceai.sty style)
2. **concrete-EDA.py** — Python script with EDA experiments students run via OpenCode
3. **concrete-sparsity-skill.md** — Markdown SKILL artifact template

### Definition of Done (verifiable conditions)
- [ ] Tutorial05B.tex compiles without errors (`pdflatex Tutorial05B.tex`)
- [ ] All figure references resolved (tikz diagrams, no external images needed)
- [ ] concrete-EDA.py runs without errors (`python concrete-EDA.py`)
- [ ] concrete-sparsity-skill.md is valid Markdown with clear structure
- [ ] All file paths use relative references (no absolute paths)
- [ ] Tutorial references Tutorial 05A for OpenCode basics

### Must Have
- Data exploration experiments that reveal sparsity (96.2% unique combos)
- Age distribution analysis showing imbalance (41% at 28 days)
- Growth curve discovery (181 multi-age mixtures)
- Discussion of why age ≠ ordinary feature
- SKILL artifact template with concrete structure

### Must NOT Have (guardrails)
- No model implementation (no sklearn, no training loops)
- No cross-validation or hyperparameter tuning
- No external image files (all figures via tikz or code-generated)
- No Jupyter notebook format (OpenCode TUI only)
- No absolute file paths

## Verification Strategy
> ZERO HUMAN INTERVENTION - all verification is agent-executed.
- Test decision: tests-after (Python script validation)
- QA policy: Every task has agent-executed scenarios
- Evidence: .sisyphus/evidence/task-{N}-{slug}.{ext}

## Execution Strategy
### Parallel Execution Waves

**Wave 1**: Foundation tasks
- Create Python EDA script
- Create SKILL artifact template
- Draft tutorial skeleton

**Wave 2**: Integration tasks
- Complete tutorial with references to experiments
- Add tikz diagrams for data structure visualization
- Final review and compilation check

### Dependency Matrix (full, all tasks)
- T1 (EDA script) → T3, T4, T5 (tutorial sections reference it)
- T2 (SKILL template) → T6 (tutorial includes it)
- T3, T4, T5, T6 all depend on T1, T2 for content
- T7 (final review) depends on all above

### Agent Dispatch Summary (wave → task count → categories)
- Wave 1: 3 tasks (build, explore, unspecified-low)
- Wave 2: 4 tasks (build, unspecified-low)

## TODOs
> Implementation + Test = ONE task. Never separate.
> EVERY task MUST have: Agent Profile + Parallelization + QA Scenarios.

- [ ] 1. Create Python EDA Script (concrete-EDA.py)

  **What to do**: Create a Python script that performs exploratory data analysis on the UCI Concrete dataset. The script should:
  1. Load `UCI-Concrete Data/Concrete_Data_CSV.csv` (handle BOM character)
  2. Drop the single row with all-missing values
  3. Compute and print: total rows, column names, basic statistics for each numeric column
  4. Analyze Age distribution: unique ages, count per age, percentage of total
  5. Count unique mixture designs (7 components as tuple)
  6. Identify growth curve data: mixtures with multiple age measurements
  7. Compute sparsity ratio: unique mixture-age combos / total rows
  8. Compute correlation matrix between all features and strength
  9. Identify outliers in strength using IQR method
  10. Print all results to stdout with clear section headers

  **Must NOT do**: No model training, no sklearn imports, no plotting (stdout only)

  **Recommended Agent Profile**:
  - Category: `build` - Reason: Python script creation
  - Skills: [] - No specialized skills needed
  - Omitted: [] - None

  **Parallelization**: Can Parallel: NO | Wave 1 | Blocks: T3-T6 | Blocked By: nothing

  **References**:
  - Data: `UCI-Concrete Data/Concrete_Data_CSV.csv` - 11 columns, 1031 rows, BOM character in first column name
  - Pattern: Use `pandas.read_csv()` with `encoding='utf-8-sig'` to handle BOM
  - Output: Print to stdout with clear section headers (e.g., "=== Age Distribution ===")

  **Acceptance Criteria** (agent-executable only):
  - [ ] Script runs without errors: `python concrete-EDA.py`
  - [ ] Output includes all 10 analysis sections with clear headers
  - [ ] Sparsity ratio printed as percentage (96.2%)
  - [ ] Age distribution shows all 14 unique ages with counts and percentages
  - [ ] Growth curve data count printed (181 mixtures)

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Script runs successfully
    Tool: Bash
    Steps: cd /Users/chenzhiq/MyProjects/CoursesDev/AppliedAI4Engineering/Tutorials && python concrete-EDA.py
    Expected: Exit code 0, output contains all section headers
    Evidence: .sisyphus/evidence/task-1-run.txt

  Scenario: BOM handling works
    Tool: Bash
    Steps: python -c "import pandas as pd; df = pd.read_csv('UCI-Concrete Data/Concrete_Data_CSV.csv', encoding='utf-8-sig'); print(df.columns[0])"
    Expected: First column name is 'Cement (component 1)(kg in a m^3 mixture)' without BOM prefix
    Evidence: .sisyphus/evidence/task-1-bom.txt
  ```

  **Commit**: NO

- [ ] 2. Create SKILL Artifact Template (concrete-sparsity-skill.md)

  **What to do**: Create a Markdown file that serves as a reusable SKILL artifact. Structure:
  1. Title: "Concrete Sparsity Exploration Skill"
  2. Purpose: When to use this skill (sparse longitudinal data with physical time dimension)
  3. Key observations: The 4 challenges (supervised setting exists, time ≠ feature, sparse per mixture, age imbalance)
  4. Exploration checklist: Step-by-step OpenCode prompts students should use
  5. Discussion questions: Prompts for class discussion
  6. What to try next: Suggest modeling approaches without implementing
  7. References: Link to dataset readme and original papers

  **Must NOT do**: No code implementation, no data analysis results embedded

  **Recommended Agent Profile**:
  - Category: `quick` - Reason: Markdown file creation
  - Skills: [] - No specialized skills needed
  - Omitted: [] - None

  **Parallelization**: Can Parallel: YES | Wave 1 | Blocks: T6 | Blocked By: nothing

  **References**:
  - Pattern: Follow ceai.sty style for consistency with other tutorials
  - Content: Use findings from concrete-EDA.py analysis
  - Format: Markdown with clear sections, bullet points, code blocks for OpenCode prompts

  **Acceptance Criteria** (agent-executable only):
  - [ ] File exists at `concrete-sparsity-skill.md`
  - [ ] Contains all 7 required sections
  - [ ] OpenCode prompts are concrete and actionable
  - [ ] No code implementation included
  - [ ] Valid Markdown (no syntax errors)

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: File is valid Markdown
    Tool: Bash
    Steps: cat concrete-sparsity-skill.md | head -50
    Expected: File readable, sections clearly marked
    Evidence: .sisyphus/evidence/task-2-markdown.txt

  Scenario: All sections present
    Tool: Bash
    Steps: grep -c "^## " concrete-sparsity-skill.md
    Expected: At least 7 section headers found
    Evidence: .sisyphus/evidence/task-2-sections.txt
  ```

  **Commit**: NO

- [ ] 3. Create Tutorial Skeleton (Tutorial05B.tex)

  **What to do**: Create the LaTeX tutorial document skeleton with:
  1. Title, author, date (consistent with Tutorial 05A)
  2. Overview box (AI Agentic Workflow context)
  3. What you will do today (4-5 items)
  4. Section 1: The Concrete Dataset (description, columns, engineering context)
  5. Section 2: Why This Data Is Challenging (sparsity, age imbalance, physics vs features)
  6. Section 3: Exploring with OpenCode (step-by-step experiments)
  7. Section 4: What We Learned (summary of findings)
  8. Section 5: Creating Your SKILL (instructions for concrete-sparsity-skill.md)
  9. References section

  **Must NOT do**: No tikz diagrams yet (handled in T4), no Python code embedded (referenced)

  **Recommended Agent Profile**:
  - Category: `build` - Reason: LaTeX file creation
  - Skills: [] - No specialized skills needed
  - Omitted: [] - None

  **Parallelization**: Can Parallel: NO | Wave 1 | Blocks: T5, T7 | Blocked By: nothing

  **References**:
  - Style: `Tutorial05A-OpenCode-AI-Coding-Agent.tex` - use same ceai.sty, box styles, listings
  - Data path: `UCI-Concrete Data/Concrete_Data_CSV.csv` (relative)
  - EDA script: `concrete-EDA.py` (referenced, not embedded)

  **Acceptance Criteria** (agent-executable only):
  - [ ] File compiles: `pdflatex Tutorial05B.tex`
  - [ ] All section headers present (5 main sections)
  - [ ] References Tutorial 05A for OpenCode basics
  - [ ] No undefined commands or packages

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: LaTeX compiles
    Tool: Bash
    Steps: cd /Users/chenzhiq/MyProjects/CoursesDev/AppliedAI4Engineering/Tutorials && pdflatex -interaction=nonstopmode Tutorial05B.tex
    Expected: Exit code 0, no errors in log
    Evidence: .sisyphus/evidence/task-3-compile.log
  ```

  **Commit**: NO

- [ ] 4. Add TikZ Diagrams for Data Structure

  **What to do**: Create tikz diagrams that visualize:
  1. Age distribution bar chart (14 unique ages, heights proportional to count)
  2. Sparsity visualization: show how few mixture-age combos have multiple observations
  3. The "growth curve" concept: same mixture, different ages, different strengths

  **Must NOT do**: No external image files, no plot generation

  **Recommended Agent Profile**:
  - Category: `build` - Reason: LaTeX tikz diagram creation
  - Skills: [] - No specialized skills needed
  - Omitted: [] - None

  **Parallelization**: Can Parallel: NO | Wave 2 | Blocks: T7 | Blocked By: T3

  **References**:
  - Pattern: `Tutorial05A-OpenCode-AI-Coding-Agent.tex` lines 103-118 (tikz flowchart pattern)
  - Data: Age distribution from concrete-EDA.py analysis
  - Style: Use ceaiLightBlue, blue!70!black arrows, consistent with 05A

  **Acceptance Criteria** (agent-executable only):
  - [ ] All 3 diagrams compile without errors
  - [ ] Age bar chart shows correct heights for all 14 ages
  - [ ] Sparsity diagram clearly shows 96.2% ratio
  - [ ] Growth curve diagram illustrates the concept

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: TikZ diagrams compile
    Tool: Bash
    Steps: cd /Users/chenzhiq/MyProjects/CoursesDev/AppliedAI4Engineering/Tutorials && pdflatex -interaction=nonstopmode Tutorial05B.tex
    Expected: Exit code 0, no tikz errors
    Evidence: .sisyphus/evidence/task-4-tikz.log
  ```

  **Commit**: NO

- [ ] 5. Complete Tutorial Content

  **What to do**: Fill in the tutorial with:
  1. Concrete OpenCode prompts students should type
  2. Expected output from concrete-EDA.py (show sample output)
  3. Discussion questions at each section
  4. Instructions for creating concrete-sparsity-skill.md
  5. References to Tutorial 05A for OpenCode basics
  6. Links to dataset readme and original papers

  **Must NOT do**: No model implementation details, no sklearn code

  **Recommended Agent Profile**:
  - Category: `build` - Reason: LaTeX content completion
  - Skills: [] - No specialized skills needed
  - Omitted: [] - None

  **Parallelization**: Can Parallel: NO | Wave 2 | Blocks: T7 | Blocked By: T3, T4

  **References**:
  - Style: `Tutorial05A-OpenCode-AI-Coding-Agent.tex` - use same box styles, listings
  - Data: Findings from concrete-EDA.py analysis
  - SKILL: `concrete-sparsity-skill.md` (referenced)

  **Acceptance Criteria** (agent-executable only):
  - [ ] All sections have concrete OpenCode prompts
  - [ ] Sample output shown for each experiment
  - [ ] Discussion questions included
  - [ ] Tutorial compiles without errors

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Full tutorial compiles
    Tool: Bash
    Steps: cd /Users/chenzhiq/MyProjects/CoursesDev/AppliedAI4Engineering/Tutorials && pdflatex -interaction=nonstopmode Tutorial05B.tex
    Expected: Exit code 0, no errors
    Evidence: .sisyphus/evidence/task-5-full-compile.log
  ```

  **Commit**: NO

- [ ] 6. Final Review and Compilation Check

  **What to do**: 
  1. Run pdflatex twice to resolve all references
  2. Check for undefined references, missing figures
  3. Verify all file paths are relative
  4. Ensure consistent styling with Tutorial 05A
  5. Create a PDF and verify it renders correctly

  **Must NOT do**: No content changes unless errors found

  **Recommended Agent Profile**:
  - Category: `quick` - Reason: Review and verification
  - Skills: [] - No specialized skills needed
  - Omitted: [] - None

  **Parallelization**: Can Parallel: NO | Wave 2 | Blocks: nothing | Blocked By: T5

  **References**:
  - Pattern: `Tutorial05A-OpenCode-AI-Coding-Agent.tex` - use same ceai.sty, box styles
  - All files: Tutorial05B.tex, concrete-EDA.py, concrete-sparsity-skill.md

  **Acceptance Criteria** (agent-executable only):
  - [ ] Tutorial05B.pdf exists and is valid
  - [ ] No warnings in LaTeX log
  - [ ] All file paths relative
  - [ ] Consistent with Tutorial 05A styling

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: PDF generated
    Tool: Bash
    Steps: ls -la /Users/chenzhiq/MyProjects/CoursesDev/AppliedAI4Engineering/Tutorials/Tutorial05B.pdf
    Expected: File exists, size > 0
    Evidence: .sisyphus/evidence/task-6-pdf-exists.txt
  ```

  **Commit**: YES | Message: `docs(tutorial): add Tutorial 05B on concrete sparsity exploration` | Files: Tutorial05B.tex, concrete-EDA.py, concrete-sparsity-skill.md

## Final Verification Wave (MANDATORY — after ALL implementation tasks)
> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.
> **Do NOT auto-proceed after verification. Wait for user's explicit approval before marking work complete.**
> **Never mark F1-F4 as checked before getting user's okay.** Rejection or user feedback -> fix -> re-run -> present again -> wait for okay.
- [ ] F1. Plan Compliance Audit — oracle
- [ ] F2. Code Quality Review — unspecified-high
- [ ] F3. Real Manual QA — unspecified-high (+ playwright if UI)
- [ ] F4. Scope Fidelity Check — deep

## Commit Strategy
- Single commit after all tasks complete
- Message: `docs(tutorial): add Tutorial 05B on concrete sparsity exploration`
- Files: Tutorial05B.tex, concrete-EDA.py, concrete-sparsity-skill.md

## Success Criteria
- Tutorial compiles and renders correctly
- Students can follow OpenCode prompts without confusion
- SKILL artifact is reusable for similar sparse longitudinal datasets
- No model implementation (discussion only)
- Consistent with Tutorial 05A style and prerequisites
