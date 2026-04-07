# Tutorial TeX to Colab Notebook Skill

## Purpose
Convert a LaTeX tutorial (same overall style as course tutorials) into a Google Colab ready notebook document where all prose becomes markdown paragraphs and all code examples become fenced Python blocks.

## Conversion Rules
- Preserve all text content and ordering from the source LaTeX (do not add or omit content).
- Convert LaTeX sectioning to markdown headings: title -> `#`, section -> `##`, subsection -> `###`, subsubsection -> `####`.
- Convert `itemize` to markdown bullet lists.
- Convert `lstlisting` code examples to fenced code blocks labeled `python`.
- Keep inline math in LaTeX form (e.g., `$...$`).
- Keep URLs as plain text or markdown links (no LaTeX commands).
- After the initial Introduction text, insert one Colab configuration code block.

## Colab Configuration Block (Template)
Insert this once after the Introduction section. Replace placeholders to match the tutorial needs.

```python
# Colab setup
import os
import datetime as dt

# Core libraries used later (adjust to tutorial requirements)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

# Optional dependencies (uncomment if needed)
# !pip -q install openpyxl
# !pip -q install scikit-learn
```

## Output Structure Template
Use this skeleton to build the notebook markdown in the same order as the source LaTeX.

````markdown
# <Tutorial Title>

## Introduction
<intro paragraphs...>

```python
<colab config block here>
```

## <Section Title>
<section paragraphs...>

### <Subsection Title>
<subsection paragraphs...>

```python
<code from lstlisting>
```

#### <Subsubsection Title>
<subsubsection paragraphs...>

```python
<code from lstlisting>
```
````

## Notes for Common LaTeX Elements
- `\title{...}` becomes the `#` heading at the top.
- `\section*{...}` becomes a `##` heading (still include in order).
- `\textbf{...}` becomes `**...**`.
- `\texttt{...}` becomes `` `...` ``.
- `\url{...}` becomes a plain URL or `[text](url)`.
- If a `lstlisting` has a caption, place the caption as a plain line above the code block.
