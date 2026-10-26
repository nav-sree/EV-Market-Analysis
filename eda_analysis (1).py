
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load cleaned dataset
df = pd.read_csv("outputs/ev_data_cleaned.csv")

# Create folder for charts
chart_dir = Path("outputs/charts")
chart_dir.mkdir(parents=True, exist_ok=True)

# Set a professional chart style
sns.set_theme(style="whitegrid", context="notebook")

print("Dataset loaded:", df.shape)
print("Creating EV analysis charts...")

# Chart 1: Top 10 brands by number of listed models
top_brands = df["brand"].value_counts().head(10)

plt.figure(figsize=(11, 6))
sns.barplot(x=top_brands.values, y=top_brands.index)
plt.title("Top 10 Brands by Number of Listed EV Models",
          fontsize=15, weight="bold")
plt.xlabel("Number of EV Models")
plt.ylabel("Brand")
plt.tight_layout()
plt.savefig(chart_dir / "top_10_brands.png", dpi=300)
plt.close()

# Chart 2: Distribution of driving range
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="range_km", bins=25, kde=True)
plt.title("Distribution of Electric Vehicle Driving Range",
          fontsize=15, weight="bold")
plt.xlabel("Listed Driving Range (km)")
plt.ylabel("Number of Models")
plt.tight_layout()
plt.savefig(chart_dir / "ev_range_distribution.png", dpi=300)
plt.close()

# Chart 3: Battery capacity versus driving range
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="battery_capacity_kWh",
    y="range_km",
    hue="drivetrain",
    alpha=0.8
)
plt.title("Battery Capacity vs Driving Range",
          fontsize=15, weight="bold")
plt.xlabel("Battery Capacity (kWh)")
plt.ylabel("Listed Driving Range (km)")
plt.tight_layout()
plt.savefig(chart_dir / "battery_vs_range.png", dpi=300)
plt.close()

# Chart 4: Models by body type
body_counts = df["car_body_type"].value_counts()

plt.figure(figsize=(11, 6))
sns.barplot(x=body_counts.values, y=body_counts.index)
plt.title("Number of EV Models by Body Type",
          fontsize=15, weight="bold")
plt.xlabel("Number of Models")
plt.ylabel("Body Type")
plt.tight_layout()
plt.savefig(chart_dir / "ev_body_types.png", dpi=300)
plt.close()

print("\nAll four charts created successfully!")
print("Chart folder:", chart_dir.resolve())

for chart in sorted(chart_dir.glob("*.png")):
    print("-", chart.name)
