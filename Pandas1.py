
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Cargar los datos

df = pd.read_csv("people_data_large.csv")

print("\n========== ORIGINAL DATASET ==========")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nDataset information:")
df.info()

print("\nDescriptive statistics:")
print(df.describe(include="all"))


#Limpiar los valores invalidos

df.replace(
    ["-", "unknown", "Unknown", "UNKNOWN", ""],
    np.nan,
    inplace=True
)


df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nMissing values before cleaning:")
print(df.isna().sum())


#convertir las variables numericas

numeric_candidates = ["age", "income"]

for col in numeric_candidates:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")


if "age" in df.columns:
    df.loc[df["age"] < 0, "age"] = np.nan

if "income" in df.columns:
    df.loc[df["income"] < 0, "income"] = np.nan


#Arreglar los datos faltantes


numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    median_value = df[col].median()

    if pd.notna(median_value):
        df[col] = df[col].fillna(median_value)


categorical_cols = df.select_dtypes(
    include=["object", "category"]
).columns

for col in categorical_cols:
    mode_values = df[col].mode()

    if not mode_values.empty:
        df[col] = df[col].fillna(mode_values[0])

print("\nMissing values after cleaning:")
print(df.isna().sum())


#Categoria de los valores


if "city" in df.columns:
    df["city_code"], city_labels = pd.factorize(df["city"])

    print("\nCity encoding:")
    print(dict(enumerate(city_labels)))


one_hot_cols = [
    col for col in ["has_car", "education"]
    if col in df.columns
]

if one_hot_cols:
    df = pd.get_dummies(
        df,
        columns=one_hot_cols,
        dtype=int
    )

print("\nDataset after encoding:")
print(df.head())


#Crear nuevos valores

if "age" in df.columns and "income" in df.columns:

    
    df["income_per_age"] = (
        df["income"] / df["age"].replace(0, np.nan)
    )

    df["is_senior"] = (df["age"] > 60).astype(int)

  
    df["log_income"] = np.log1p(df["income"])




#Correlacion de matrices

numeric_df = df.select_dtypes(include=np.number)

correlation = numeric_df.corr()

print("\nCorrelation matrix:")
print(correlation)


#histigramas

for col in ["age", "income"]:
    if col in df.columns:

        plt.figure(figsize=(8, 5))

        plt.hist(
            df[col].dropna(),
            bins=30,
            edgecolor="black"
        )

        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.title(f"Distribution of {col}")

        plt.tight_layout()
        plt.show()


#Scattering plot: AGE VS INCOME


if "age" in df.columns and "income" in df.columns:

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df["age"],
        df["income"],
        alpha=0.4
    )

    plt.xlabel("Age")
    plt.ylabel("Income")
    plt.title("Age vs Income")

    plt.tight_layout()
    plt.show()


# ============================================================
# 11. HEXBIN PLOT: AGE VS INCOME
# ============================================================

if "age" in df.columns and "income" in df.columns:

    plt.figure(figsize=(8, 5))

    plt.hexbin(
        df["age"],
        df["income"],
        gridsize=30,
        cmap="viridis",
        mincnt=1
    )

    plt.colorbar(label="Number of observations")

    plt.xlabel("Age")
    plt.ylabel("Income")
    plt.title("Age vs Income: Hexbin")

    plt.tight_layout()
    plt.show()


# ============================================================
# 12. CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(12, 9))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    center=0
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


# ============================================================
# 13. SAVE CLEANED DATASET
# ============================================================

df.to_csv("people_data_cleaned.csv", index=False)

print("\n========== FINAL DATASET ==========")
print("Shape:", df.shape)
print(df.head())

print("\nCleaned dataset saved as people_data_cleaned.csv")
