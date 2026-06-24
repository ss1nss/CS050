import pandas as pd

import glob

import os

 

# ===== Settings =====

GROUP_KEY = "Loan Reference"   # group-by column

TEXT_POSITIONS = [0, 5]        # A=0, F=5 -> must remain text

DATE_POSITIONS = [6, 8, 13]    # G=6, I=8, N=13 (0-based)

# ====================

 

folder = r"C:\Users" # replace wherever your files/folders are located

 

# Get first file | add extensions

files = glob.glob(os.path.join(folder, "*.xlsx")) + \

        glob.glob(os.path.join(folder, "*.xls")) + \

        glob.glob(os.path.join(folder, "*.csv"))

if not files:

    raise FileNotFoundError("No matching files found in the folder.")

file_path = files[0]

 

# Read all columns as strings to preserve leading zeros and avoid type inference

if file_path.endswith((".xls", ".xlsx")):

    df = pd.read_excel(file_path, dtype=str)

elif file_path.endswith(".csv"):

    df = pd.read_csv(file_path, dtype=str)

else:

    raise ValueError(f"Unsupported file type: {file_path}")

 

# Ensure group key exists

if GROUP_KEY not in df.columns:

    raise KeyError(f"Column '{GROUP_KEY}' not found. Available columns: {list(df.columns)}")

 

# Resolve names from positions (A, F for text; G, I, N for dates)

def names_from_positions(positions, columns):

    names = []

    for pos in positions:

        if pos < 0 or pos >= len(columns):

            raise IndexError(f"Position {pos} out of range (total columns: {len(columns)}).")

        names.append(columns[pos])

    return names

 

text_cols = names_from_positions(TEXT_POSITIONS, df.columns)

date_cols = names_from_positions(DATE_POSITIONS, df.columns)

 

# Treat GROUP_KEY as text as well

if GROUP_KEY not in text_cols:

    text_cols.append(GROUP_KEY)

 

# Prepare numeric conversion for non-text & non-date columns

df_num = df.copy()

numeric_candidates = [c for c in df.columns if c not in text_cols and c not in date_cols]

 

for col in numeric_candidates:

    series = df_num[col].str.replace(",", "", regex=False)

    df_num[col] = pd.to_numeric(series, errors="coerce")

 

# Build aggregation: sum numeric, take first for others

agg_dict = {}

for col in df.columns:

    if col == GROUP_KEY:

        continue

    if col in numeric_candidates and pd.api.types.is_numeric_dtype(df_num[col]):

        agg_dict[col] = "sum"

    else:

        agg_dict[col] = "first"

 

# Group and aggregate

result = df_num.groupby(GROUP_KEY, as_index=False).agg(agg_dict)

 

# Restore text columns from original df (leading zeros, alphanumerics)

for col in text_cols:

    if col == GROUP_KEY:

        continue

    if col in result.columns:

        first_values = df.groupby(GROUP_KEY, as_index=True)[col].first()

        result[col] = result[GROUP_KEY].map(first_values)

 

# Normalize date columns -> strings "MM/DD/YYYY"

for col in date_cols:

    if col in result.columns:

        dt = pd.to_datetime(result[col], errors="coerce")

        result[col] = dt.dt.strftime("%m/%d/%Y").fillna("")

 

# Output (same branching as your original)

output_path = os.path.join(folder, "output.xlsx" if file_path.endswith((".xls", ".xlsx")) else "output.csv")

if output_path.endswith(".xlsx"):

    result.to_excel(output_path, index=False)   # pandas writes strings as text cells

else:

    result.to_csv(output_path, index=False)

 

print("Aggregated file saved to:", output_path)