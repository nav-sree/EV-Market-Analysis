
import pandas as pd
from pathlib import Path

# Project paths
input_file = Path("electric_vehicles_spec_2025.csv")
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

# Load the original dataset
df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)

# Remove unnecessary spaces from text values
text_columns = df.select_dtypes(include=["object", "str"]).columns

for col in text_columns:
    df[col] = df[col].str.strip()

# Handle the missing model name without deleting its row
df["model"] = df["model"].fillna("Unknown")

# Convert cargo volume to a numeric column where possible.
# Keep the original values because some entries use other units.
df["cargo_volume_l_numeric"] = pd.to_numeric(
    df["cargo_volume_l"], errors="coerce"
)

# Preserve remaining missing values rather than guessing replacements.
# No duplicate rows were found during inspection.

# Save the cleaned dataset
output_file = output_dir / "ev_data_cleaned.csv"
df.to_csv(output_file, index=False)

print("\n===== CLEANING SUMMARY =====")
print("Original rows:", 478)
print("Cleaned dataset shape:", df.shape)
print("Duplicate rows:", df.duplicated().sum())
print("\nRemaining missing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

print("\nCargo volume entries needing review:",
      df["cargo_volume_l_numeric"].isna().sum())

print("\nCleaned dataset saved to:", output_file)
