# Concrete Sparsity Exploration Skill

## Purpose

Use this skill when encountering **sparse longitudinal datasets** where:
- Each entity (mixture, patient, batch) has only 1-3 observations across time
- Time has physical meaning (not just a categorical feature)
- The dataset appears to support supervised regression but is extremely thin per entity-time pair

This skill captures empirical knowledge gained from exploring the UCI Concrete Compressive Strength dataset, where 96% of (entity, time) combinations appear only once.

## Key Observations

### 1. Supervised Setting Exists — But With Caveats
The dataset provides features (7 components) and a target (strength), with Age as an input. This creates a supervised regression problem. However, treating Age as just another feature ignores the physics of concrete curing.

### 2. Time Is Not an Ordinary Feature
Concrete strength evolves according to chemical curing processes. A specific mixture will have a predictable strength at different times — this is a growth curve. Age cannot be treated like Cement or Water because:
- Age is ordered and has a known functional relationship (logarithmic curing)
- The same mixture tested at different ages is NOT an independent data point in the statistical sense
- There is only one "true" strength curve per mixture

### 3. Extreme Sparsity Per Entity-Time Pair
For the concrete dataset:
- 1,031 total rows
- 992 unique (mixture, age) combinations
- **96.2% sparsity ratio** — nearly every row is its own unique combination
- Most mixtures have only 1-3 age measurements
- Some mixtures have up to 8 age measurements (rare)

### 4. Severe Age Imbalance
- 41% of data is at 28 days
- 13% at 3 days, 12% at 7 days
- Only 0.19% at 1 day
- Long-term data (180+ days) is very sparse

## Exploration Checklist

Use these OpenCode prompts to systematically explore sparse longitudinal data:

### Step 1: Basic Dataset Overview
```
Load the CSV file at [path]. Report:
- Total rows and columns
- Column names with descriptions
- Data types for each column
- Any obvious missing values
```

### Step 2: Age/Time Distribution
```
Analyze the distribution of the Age column:
- How many unique values?
- Count and percentage for each unique age
- Show a visual bar representation
- Identify the dominant age(s)
```

### Step 3: Entity Uniqueness
```
Treat the 7 mixture components as a single identifier.
Report:
- How many unique mixture designs exist?
- Average rows per unique mixture
- Maximum rows per mixture
- What fraction of mixtures have only 1 observation?
```

### Step 4: Growth Curve Discovery
```
Find mixtures that have measurements at multiple ages.
For each such mixture:
- List the ages measured
- List the corresponding strengths
- Show how strength changes with age
Report:
- How many mixtures have multi-age data?
- What fraction of total rows are growth curve data?
```

### Step 5: Sparsity Analysis
```
Create a unique identifier for each (mixture, age) combination.
Report:
- How many unique (mixture, age) combos exist?
- Sparsity ratio: unique combos / total rows
- How many combos have exactly 1 observation?
- How many have 2+ observations?
- What is the maximum observations per combo?
```

### Step 6: Feature-Target Relationships
```
Compute the correlation between each feature and the target strength.
Report:
- Strongest positive predictor
- Strongest negative predictor
- Any surprising correlations
```

### Step 7: Outlier Detection
```
Use the IQR method to detect outliers in the target variable.
Report:
- Number of outliers
- Details of outlier observations
- Strength distribution summary (min, max, mean, median, 70th percentile)
```

### Step 8: Data Imbalance Summary
```
Group observations into time bins:
- Early (1-7 days)
- Standard (8-28 days)
- Medium (29-90 days)
- Long (91-180 days)
- Very Long (181+ days)
Report the count and percentage in each bin.
```

## Discussion Questions

After completing the exploration, consider:

1. **Why does treating Age as an ordinary feature fail?**
   - What physical process does Age represent?
   - Why can't we simply add more Age samples for the same mixture?

2. **What does 96% sparsity mean for modeling?**
   - Can we trust a model trained on mostly unique observations?
   - What happens when we try to generalize to unseen mixtures?

3. **How does the 28-day concentration affect learning?**
   - Will the model learn general curing behavior or just 28-day patterns?
   - What predictions are most uncertain?

4. **What would make this dataset more useful?**
   - More mixtures? More ages per mixture? Both?
   - How many observations per mixture would be "enough"?

## What to Try Next

When encountering similar sparse longitudinal data, consider these approaches:

### Without Implementation
- **Log-transform Age**: Concrete curing follows logarithmic time dependence. Try exploring strength vs. log(Age).
- **Group by Mixture**: Analyze strength trajectories within each mixture group.
- **Physics-Informed Features**: Use water-to-cement ratio, cement equivalent, or other domain-derived features.
- **Hierarchical Modeling**: Treat mixtures as random effects with a shared curing curve.
- **Transfer Learning**: Learn from mixtures with rich age data and transfer to sparse mixtures.

### Evaluation Considerations
- Standard train/test split may leak information (same mixture in both sets)
- Consider splitting by mixture, not by row
- Evaluate separately on different age ranges

## References

- **Dataset**: UCI Concrete Compressive Strength
  - Original source: Prof. I-Cheng Yeh, Chung-Hua University, Taiwan
  - Readme: `UCI-Concrete Data/Concrete_Readme.txt`
  - CSV: `UCI-Concrete Data/Concrete_Data_CSV.csv`

- **Key Paper**:
  I-Cheng Yeh, "Modeling of strength of high performance concrete using artificial neural networks," *Cement and Concrete Research*, Vol. 28, No. 12, pp. 1797-1808 (1998).

- **Engineering Standard**:
  ACI 209.2R-08 — Strength development model for concrete
