
import pandas as pd

# Load the EV dataset
file_path = "electric_vehicles_spec_2025.csv"
df = pd.read_csv(file_path)

# Display basic dataset information
print("\n===== DATASET SHAPE =====")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())


print("\n===== MISSING VALUE PERCENTAGES =====")
missing_percent = (df.isnull().sum() / len(df) * 100).round(2)
print(missing_percent[missing_percent > 0].sort_values(ascending=False))

print("\n===== NUMERICAL DATA SUMMARY =====")
print(df.describe().round(2).to_string())

print("\n===== CARGO VOLUME EXAMPLES =====")
print(df["cargo_volume_l"].dropna().unique()[:20])

print("\n===== VEHICLES PER BRAND =====")
print(df["brand"].value_counts().head(10))

print("\n===== CATEGORICAL COLUMN VALUES =====")
for col in ["battery_type", "drivetrain", "segment", "car_body_type"]:
    print(f"\n{col}:")
    print(df[col].value_counts().head(10).to_string())
