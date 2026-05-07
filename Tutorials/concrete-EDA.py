#!/usr/bin/env python3
"""
Concrete Sparsity Exploration Script
=====================================
Exploratory data analysis for the UCI Concrete Compressive Strength dataset.
Designed for use with OpenCode TUI — students type this command:
    python concrete-EDA.py

This script performs 10 analysis steps and prints results to stdout.
No model training, no plotting, no sklearn.
"""

import pandas as pd
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
DATA_PATH = SCRIPT_DIR / "UCI-Concrete Data" / "Concrete_Data_CSV.csv"


def load_data():
    """Load CSV, handle BOM, drop fully-missing row, strip quotes from column names."""
    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")
    # CSV has single quotes wrapped around every column name — strip them
    # Also strip trailing/leading whitespace (e.g., "strength(MPa, megapascals) ")
    df.columns = df.columns.str.strip("'").str.strip()
    feature_cols = df.columns[:-3]  # exclude derived columns: strength, fc28, NSC
    df = df.dropna(subset=feature_cols, how="all").reset_index(drop=True)
    return df


def print_header(title):
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


# ---------------------------------------------------------------------------
# 1. Basic Info
# ---------------------------------------------------------------------------
def basic_info(df):
    print_header("1. BASIC DATASET INFO")
    print(f"  Rows: {len(df)}")
    print(f"  Columns ({len(df.columns)}):")
    for i, col in enumerate(df.columns, 1):
        print(f"    {i:2d}. {col}")
    print(f"\n  Data types:")
    for col in df.columns:
        print(f"    {col:40s} {df[col].dtype}")


# ---------------------------------------------------------------------------
# 2. Basic Statistics
# ---------------------------------------------------------------------------
def basic_stats(df):
    print_header("2. BASIC STATISTICS (Numeric Columns)")
    numeric = df.select_dtypes(include=["number"])
    # Show only the 9 core columns (7 components + Age + Strength)
    core = numeric.columns[:-2]  # exclude fc28 and NSC
    stats = numeric[core].describe()
    print(stats.round(2).to_string())


# ---------------------------------------------------------------------------
# 3. Age Distribution
# ---------------------------------------------------------------------------
def age_distribution(df):
    print_header("3. AGE DISTRIBUTION")
    age_counts = df["Age (day)"].value_counts().sort_index()
    total = len(df)
    print(f"  Total rows: {total}")
    print(f"  Unique ages: {len(age_counts)}")
    print(f"  {'Age (days)':<12} {'Count':>8} {'%':>8} {'Bar'}")
    print(f"  {'-' * 50}")
    for age, count in age_counts.items():
        pct = count / total * 100
        bar_len = int(pct / 2)  # scale bar
        bar = "#" * bar_len
        print(f"  {age:<12} {count:>8} {pct:>6.1f}%  {bar}")


# ---------------------------------------------------------------------------
# 4. Unique Mixtures
# ---------------------------------------------------------------------------
def unique_mixtures(df):
    print_header("4. UNIQUE MIXTURE DESIGNS")
    mixture_cols = df.columns[:7]  # 7 components
    df["mixture_id"] = df[mixture_cols].apply(tuple, axis=1)
    n_unique = df["mixture_id"].nunique()
    print(f"  Total rows: {len(df)}")
    print(f"  Unique mixtures: {n_unique}")
    print(f"  Avg rows per mixture: {len(df) / n_unique:.2f}")
    print(f"  Max rows per mixture: {df['mixture_id'].value_counts().max()}")

    # Zero-inflated components
    print(f"\n  Zero-inflated components (fraction of zeros):")
    for col in mixture_cols:
        frac_zero = (df[col] == 0).mean()
        print(f"    {col:25s} {frac_zero:.1%}")


# ---------------------------------------------------------------------------
# 5. Growth Curve Data
# ---------------------------------------------------------------------------
def growth_curves(df):
    print_header("5. GROWTH CURVE DATA")
    mixture_cols = df.columns[:7]
    df["mixture_id"] = df[mixture_cols].apply(tuple, axis=1)

    multi_age = df.groupby("mixture_id")["Age (day)"].nunique()
    n_single = (multi_age == 1).sum()
    n_multi = (multi_age > 1).sum()
    n_total = multi_age.sum()

    print(f"  Mixtures with 1 age:   {n_single} ({n_single / len(multi_age):.1%})")
    print(f"  Mixtures with 2+ ages: {n_multi} ({n_multi / len(multi_age):.1%})")
    print(f"  Total growth curve rows: {df[df['mixture_id'].isin(multi_age[multi_age > 1].index)].shape[0]}")

    # Show top 5 mixtures by age count
    print(f"\n  Top 5 mixtures by number of age measurements:")
    top5 = multi_age[multi_age > 1].nlargest(5)
    for mid, age_count in top5.items():
        sample = df[df["mixture_id"] == mid]
        ages = sorted(sample["Age (day)"].unique())
        strengths = sample.sort_values("Age (day)")["Concrete compressive strength(MPa, megapascals)"].values
        print(f"    Ages: {ages}  Strengths: {strengths.round(2).tolist()}")


# ---------------------------------------------------------------------------
# 6. Sparsity Analysis
# ---------------------------------------------------------------------------
def sparsity_analysis(df):
    print_header("6. SPARSITY ANALYSIS")
    mixture_cols = df.columns[:7]
    df["mixture_id"] = df[mixture_cols].apply(tuple, axis=1)
    df["combo_id"] = df.apply(lambda row: row["mixture_id"] + (str(row["Age (day)"]),), axis=1)

    n_total = len(df)
    n_unique_combos = df["combo_id"].nunique()
    sparsity = (n_unique_combos / n_total) * 100

    print(f"  Total rows: {n_total}")
    print(f"  Unique mixture-age combos: {n_unique_combos}")
    print(f"  Sparsity ratio: {sparsity:.1f}%")
    print(f"  Interpretation: {100 - sparsity:.1f}% of data points are unique observations")

    # Breakdown
    combo_counts = df["combo_id"].value_counts()
    print(f"\n  Combos with 1 observation: {(combo_counts == 1).sum()}")
    print(f"  Combos with 2 observations: {(combo_counts == 2).sum()}")
    print(f"  Combos with 3+ observations: {(combo_counts >= 3).sum()}")
    print(f"  Max observations per combo: {combo_counts.max()}")


# ---------------------------------------------------------------------------
# 7. Correlation Matrix
# ---------------------------------------------------------------------------
def correlation_matrix(df):
    print_header("7. CORRELATION MATRIX (with Strength)")
    core = df.columns[:9]  # 7 components + Age + Strength
    corr = df[core].corr()
    strength_corr = corr["Concrete compressive strength(MPa, megapascals)"].drop("Concrete compressive strength(MPa, megapascals)")
    print(f"\n  {'Feature':<30} {'Correlation':>12}")
    print(f"  {'-' * 45}")
    for feat, val in strength_corr.items():
        print(f"  {feat:<30} {val:>12.3f}")
    print(f"\n  Strongest positive: Cement ({strength_corr['Cement (component 1)(kg in a m^3 mixture)']:.3f})")
    print(f"  Strongest negative: Water ({strength_corr['Water  (component 4)(kg in a m^3 mixture)']:.3f})")


# ---------------------------------------------------------------------------
# 8. Outlier Detection
# ---------------------------------------------------------------------------
def outlier_detection(df):
    print_header("8. OUTLIER DETECTION (IQR Method)")
    strength_col = "Concrete compressive strength(MPa, megapascals)"
    q1 = df[strength_col].quantile(0.25)
    q3 = df[strength_col].quantile(0.75)
    iqr = q3 - q1
    upper = q3 + 1.5 * iqr
    lower = q1 - 1.5 * iqr

    print(f"  Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
    print(f"  Lower bound: {lower:.2f}, Upper bound: {upper:.2f}")

    outliers = df[(df[strength_col] < lower) | (df[strength_col] > upper)]
    print(f"\n  Number of outliers: {len(outliers)}")
    if len(outliers) > 0:
        print(f"\n  {'Strength':>10} {'Age':>6} {'Cement':>10}")
        for _, row in outliers.sort_values(strength_col, ascending=False).iterrows():
            print(f"  {row[strength_col]:>10.2f} {int(row['Age (day)']):>6} {row['Cement (component 1)(kg in a m^3 mixture)']:>10.1f}")

    # Strength distribution summary
    print(f"\n  Strength distribution:")
    print(f"    Min:   {df[strength_col].min():.2f} MPa")
    print(f"    Max:   {df[strength_col].max():.2f} MPa")
    print(f"    Mean:  {df[strength_col].mean():.2f} MPa")
    print(f"    Median:{df[strength_col].median():.2f} MPa")
    pct_70 = df[strength_col].quantile(0.7)
    print(f"    70th percentile: {pct_70:.2f} MPa (70% of data below this)")


# ---------------------------------------------------------------------------
# 9. Missing Values
# ---------------------------------------------------------------------------
def missing_values(df):
    print_header("9. MISSING VALUES")
    missing = df.isnull().sum()
    total_missing = missing.sum()
    if total_missing == 0:
        print("  No missing values detected.")
    else:
        print(f"  Total missing: {total_missing}")
        for col, count in missing[missing > 0].items():
            print(f"    {col}: {count}")


# ---------------------------------------------------------------------------
# 10. Data Imbalance Summary
# ---------------------------------------------------------------------------
def imbalance_summary(df):
    print_header("10. DATA IMBALANCE SUMMARY")
    age_counts = df["Age (day)"].value_counts().sort_index()
    total = len(df)

    # Group ages into bins
    bins = [(0, 7, "Early (1-7 days)"),
            (8, 28, "Standard (8-28 days)"),
            (29, 90, "Medium (29-90 days)"),
            (91, 180, "Long (91-180 days)"),
            (181, 365, "Very Long (181-365 days)")]

    print(f"  {'Bin':<25} {'Count':>8} {'%':>8}")
    print(f"  {'-' * 45}")
    for lo, hi, label in bins:
        count = ((df["Age (day)"] >= lo) & (df["Age (day)"] <= hi)).sum()
        print(f"  {label:<25} {count:>8} {count/total*100:>7.1f}%")

    print(f"\n  Key insight: Most data is concentrated at 28 days (~41%).")
    print(f"  This means models may overfit to the 28-day regime and")
    print(f"  perform poorly on other curing times.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("  CONCRETE COMPRESSIVE STRENGTH — SPARSITY EXPLORATION")
    print("=" * 60)
    print(f"\n  Data file: {DATA_PATH}")
    print(f"  Using encoding: utf-8-sig (handles BOM)")

    df = load_data()
    print(f"  After cleaning: {len(df)} rows")

    basic_info(df)
    basic_stats(df)
    age_distribution(df)
    unique_mixtures(df)
    growth_curves(df)
    sparsity_analysis(df)
    correlation_matrix(df)
    outlier_detection(df)
    missing_values(df)
    imbalance_summary(df)

    print(f"\n{'=' * 60}")
    print("  EXPLORATION COMPLETE")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
