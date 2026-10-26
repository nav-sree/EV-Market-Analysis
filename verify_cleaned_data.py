
import pandas as pd

file_path = "outputs/ev_data_cleaned.csv"
df = pd.read_csv(file_path)

print("===== CLEANED DATASET VERIFICATION =====")
print("Dataset shape:", df.shape)

print("\n===== FIRST 5 VEHICLES =====")
print(df[["brand", "model", "battery_capacity_kWh", "range_km"]].head().to_string(index=False))

print("\n===== RANGE AND BATTERY SUMMARY =====")
print(
    df[["battery_capacity_kWh", "range_km", "efficiency_wh_per_km"]]
    .describe()
    .round(2)
    .to_string()
)

print("\n===== TOP 10 BRANDS =====")
print(df["brand"].value_counts().head(10).to_string())

print("\n===== BODY TYPE COUNTS =====")
print(df["car_body_type"].value_counts().to_string())

print("\nVerification complete!")
