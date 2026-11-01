
import pandas as pd
import numpy as np


# CREAR TRES DATAFRAMES


# Dataset 1
data1 = {
    "age": [22, 35, 45],
    "income": [18000, 32000, 45000],
    "city": ["Madrid", "Sevilla", "Barcelona"],
    "education": ["Bachelor", "Master", "PhD"]
}

df1 = pd.DataFrame(data1)


# Dataset 2
data2 = {
    "age": [28, 52, 61],
    "income": [25000, 50000, 38000],
    "city": ["Valencia", "Madrid", "Santiago"],
    "has_car": ["yes", "no", "yes"]
}

df2 = pd.DataFrame(data2)


# Dataset 3
data3 = {
    "age": [19, 40, 67],
    "income": [15000, 41000, 29000],
    "city": ["A Coruña", "Sevilla", "Madrid"],
    "education": ["Bachelor", "Master", "Bachelor"],
    "has_car": ["no", "yes", "no"],
    "country": ["Spain", "Spain", "Spain"]
}

df3 = pd.DataFrame(data3)


# GUARDAR DATAFRAMES COMO CSV FILES


df1.to_csv("people_part1.csv", index=False)
df2.to_csv("people_part2.csv", index=False)
df3.to_csv("people_part3.csv", index=False)

print("Three CSV files created successfully.")


#  CARGAR CSV FILES


part1 = pd.read_csv("people_part1.csv")
part2 = pd.read_csv("people_part2.csv")
part3 = pd.read_csv("people_part3.csv")



# INSPECCIONAR DATAFRAMES


print("\n========== DATASET 1 ==========")
print(part1)
print(part1.info())

print("\n========== DATASET 2 ==========")
print(part2)
print(part2.info())

print("\n========== DATASET 3 ==========")
print(part3)
print(part3.info())


# Inspect column names
print("\nColumns in each dataset:")

print("Part 1:", part1.columns.tolist())
print("Part 2:", part2.columns.tolist())
print("Part 3:", part3.columns.tolist())



# CONCATENAR DATAFRAMES VERTICALMENTE


merged = pd.concat(
    [part1, part2, part3],
    ignore_index=True,
    sort=False
)

print("\n========== CONCATENATED DATASET ==========")
print(merged)

print("\nShape:", merged.shape)

print("\nData types:")
print(merged.dtypes)

print("\nMissing values:")
print(merged.isna().sum())


# ESTANDARIZAR LOS NOMBRE DE LAS COLUMNAS 


merged.columns = (
    merged.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)



# ESTANDARIZAR LOS VALORES NUMERICOS

for col in ["age", "income"]:
    if col in merged.columns:
        merged[col] = pd.to_numeric(
            merged[col],
            errors="coerce"
        )


# Replace negative values with NaN
for col in ["age", "income"]:
    if col in merged.columns:
        merged.loc[merged[col] < 0, col] = np.nan


#  TRATAR LOS NUMEROS FALTANTES

for col in ["age", "income"]:
    if col in merged.columns:
        median_value = merged[col].median()

        if pd.notna(median_value):
            merged[col] = merged[col].fillna(median_value)


#TRATAR LAS CATEGORIAS FALTANTES

categorical_cols = merged.select_dtypes(
    include=["object", "category"]
).columns

for col in categorical_cols:

    mode_values = merged[col].mode()

    if not mode_values.empty:
        merged[col] = merged[col].fillna(mode_values[0])


#INSPECCION FINAL

print("\n========== CLEANED DATASET ==========")

print(merged)

print("\nFinal shape:")
print(merged.shape)

print("\nFinal data types:")
print(merged.dtypes)

print("\nMissing values:")
print(merged.isna().sum())


# GUARDAR EN UN ARCHIVO CSV

merged.to_csv("people_merged.csv", index=False)

print("\nFinal dataset saved as people_merged.csv")
