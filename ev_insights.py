
import pandas as pd
from pathlib import Path

# Load the cleaned dataset
df = pd.read_csv("outputs/ev_data_cleaned.csv")

# Create the output folder
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

report = []

def add_section(title, content):
    report.append("\n" + "=" * 65)
    report.append(title)
    report.append("=" * 65)
    report.append(content)

# 1. Top 10 models by driving range
top_range = df.nlargest(10, "range_km")[
    ["brand", "model", "range_km", "battery_capacity_kWh"]
]
add_section("TOP 10 EV MODELS BY LISTED RANGE",
            top_range.to_string(index=False))

# 2. Top 10 models by energy efficiency
# Lower Wh/km means less energy consumed per kilometre.
top_efficiency = df.nsmallest(10, "efficiency_wh_per_km")[
    ["brand", "model", "efficiency_wh_per_km", "range_km"]
]
add_section("TOP 10 MODELS BY ENERGY EFFICIENCY",
            top_efficiency.to_string(index=False))

# 3. Top 10 models by fast-charging power
top_charging = df.nlargest(10, "fast_charging_power_kw_dc")[
    ["brand", "model", "fast_charging_power_kw_dc", "battery_capacity_kWh"]
]
add_section("TOP 10 MODELS BY FAST-CHARGING POWER",
            top_charging.to_string(index=False))

# 4. Average range and battery capacity by drivetrain
drivetrain_summary = (
    df.groupby("drivetrain")
    .agg(
        model_count=("model", "size"),
        average_range_km=("range_km", "mean"),
        average_battery_kWh=("battery_capacity_kWh", "mean"),
        average_efficiency_Wh_km=("efficiency_wh_per_km", "mean")
    )
    .round(2)
)
add_section("COMPARISON BY DRIVETRAIN",
            drivetrain_summary.to_string())

# 5. Relationship between battery capacity and range
correlation = df["battery_capacity_kWh"].corr(df["range_km"])
add_section(
    "BATTERY CAPACITY AND RANGE",
    f"Pearson correlation: {correlation:.3f}\n"
    "Correlation describes association, not causation."
)

# 6. Dataset overview
overview = (
    f"Number of listed vehicle records: {len(df)}\n"
    f"Number of brands: {df['brand'].nunique()}\n"
    f"Average listed range: {df['range_km'].mean():.2f} km\n"
    f"Average battery capacity: "
    f"{df['battery_capacity_kWh'].mean():.2f} kWh\n"
    f"Average energy consumption: "
    f"{df['efficiency_wh_per_km'].mean():.2f} Wh/km\n"
    f"Most common body type: "
    f"{df['car_body_type'].mode().iloc[0]}"
)
add_section("DATASET OVERVIEW", overview)

# Save the report
report_path = output_dir / "ev_insights_report.txt"
report_path.write_text("\n".join(report), encoding="utf-8")

# Display results in the terminal
print("\n".join(report))
print(f"\nReport saved successfully: {report_path}")
