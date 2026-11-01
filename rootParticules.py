import uproot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Abrir el archivo ROOT
file = uproot.open("example.root")

# Mostrar los objetos disponibles
print("Objetos del archivo ROOT:")
print(file.keys())

# Inspeccionar los árboles disponibles
for key in file.keys():
    obj = file[key]

# Select the events tree
tree = file["events"]

print("\nNumber of entries:", tree.num_entries)
print("\nAvailable branches:")
print(tree.keys())

# Convert ROOT tree into Pandas DataFrame
df = tree.arrays(library="pd")

print("\nFirst rows:")
print(df.head())

print("\nDataFrame information:")
df.info()

print("\nStatistical description:")
print(df.describe())

# inspeccion de datos

print("\nMissing values:")
print(df.isna().sum())

print("\nData types:")
print(df.dtypes)

print("\nNumber of unique events:")
print(df["event_id"].nunique())


# Ecuaciones de las particulas
# Total momentum:
# p = sqrt(px^2 + py^2 + pz^2)

df["p"] = np.sqrt(
    df["px"]**2 +
    df["py"]**2 +
    df["pz"]**2
)

# Transverse mass:
# mt = sqrt(mass^2 + pt^2)

df["mt"] = np.sqrt(
    df["mass"]**2 +
    df["pt"]**2
)

# Relativistic energy (natural units: c = 1):
# E = sqrt(p^2 + mass^2)

df["E"] = np.sqrt(
    df["p"]**2 +
    df["mass"]**2
)



# Normalized momentum components
# Avoid division by zero

p_safe = df["p"].replace(0, np.nan)

df["px_norm"] = df["px"] / p_safe
df["py_norm"] = df["py"] / p_safe
df["pz_norm"] = df["pz"] / p_safe

# Logarithm of transverse momentum
# pt must be positive

df["log_pt"] = np.log(
    df["pt"].where(df["pt"] > 0)
)

# Absolute pseudorapidity

df["abs_eta"] = df["eta"].abs()

#Evento de agregacion

event_summary = df.groupby("event_id").agg(
    total_pT=("pt", "sum"),
    mean_pT=("pt", "mean"),
    total_charge=("charge", "sum"),
    total_energy=("E", "sum"),
    mean_energy=("E", "mean"),
    particle_count=("pt", "count"),
    total_weight=("weight", "sum")
)

print("\nEvent-level summary:")
print(event_summary.head())

print("\nEvent summary statistics:")
print(event_summary.describe())

#Revision de concistencia fisicas


# Check transverse momentum:
# pt = sqrt(px^2 + py^2)

pt_check = np.sqrt(
    df["px"]**2 +
    df["py"]**2
)

print("\nMaximum difference in pt:")
print(np.max(np.abs(df["pt"] - pt_check)))

# Check normalized momentum:
# px_norm^2 + py_norm^2 + pz_norm^2 = 1

norm_check = (
    df["px_norm"]**2 +
    df["py_norm"]**2 +
    df["pz_norm"]**2
)

print("\nMean normalized momentum magnitude squared:")
print(norm_check.mean())

# Check missing values after feature engineering

print("\nMissing values after feature engineering:")
print(df.isna().sum())


# Graficos y Histogramas

features = [
    "p",
    "pt",
    "mt",
    "E",
    "log_pt",
    "abs_eta"
]

df[features].hist(
    bins=40,
    figsize=(12, 8)
)

plt.suptitle("Distributions of engineered physics features")
plt.tight_layout()
plt.savefig("feature_histograms.png", dpi=300)
plt.show()


# ============================================================
# 8. 2D CORRELATION ANALYSIS
# ============================================================

correlation_features = [
    "p",
    "pt",
    "mt",
    "E",
    "log_pt",
    "abs_eta",
    "px_norm",
    "py_norm",
    "pz_norm"
]

correlations = df[correlation_features].corr()

plt.figure(figsize=(12, 9))

sns.heatmap(
    correlations,
    annot=True,
    cmap="coolwarm",
    center=0,
    fmt=".2f"
)

plt.title("Correlation matrix of engineered features")
plt.tight_layout()
plt.savefig("feature_correlations.png", dpi=300)
plt.show()


# ============================================================
# 9. 2D SCATTER PLOTS
# ============================================================

plt.figure(figsize=(8, 6))

plt.scatter(
    df["pt"],
    df["E"],
    alpha=0.4,
    s=10
)

plt.xlabel("Transverse momentum (pt)")
plt.ylabel("Energy (E)")
plt.title("Transverse momentum vs Energy")

plt.tight_layout()
plt.savefig("pt_vs_energy.png", dpi=300)
plt.show()


plt.figure(figsize=(8, 6))

plt.scatter(
    df["eta"],
    df["pt"],
    alpha=0.4,
    s=10
)

plt.xlabel("Pseudorapidity (eta)")
plt.ylabel("Transverse momentum (pt)")
plt.title("Pseudorapidity vs Transverse momentum")

plt.tight_layout()
plt.savefig("eta_vs_pt.png", dpi=300)
plt.show()


# ============================================================
# 10. SAVE RESULTS
# ============================================================

df.to_csv(
    "events_with_features.csv",
    index=False
)

event_summary.to_csv(
    "event_summary.csv"
)

print("\nAnalysis completed successfully!")

print("\nGenerated files:")
print("- events_with_features.csv")
print("- event_summary.csv")
print("- feature_histograms.png")
print("- feature_correlations.png")
print("- pt_vs_energy.png")
print("- eta_vs_pt.png")
