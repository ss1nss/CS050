import os

import shutil

from datetime import datetime

import pandas as pd

 

SUPPORTED_EXT = (".csv", ".xlsx", ".xls")

 

BULK_DIR = r"C:\Users" # replace with wherever original terms are located

MIGRATION_DIR = r"C:\Users" # replace with wherever new terms are located

OUTPUT_DIR = r"C:\Users" # replace with wherever you want outputs located

ARCHIVE_DIR = r"C:\Users" # # replace with wherever your history should be located (both imput files)

 

# Each tuple is: (BulkColumnToOverwrite, MigrationColumnToCopyFrom)

# Use Excel letters: "P", "AA", etc.  OR  1-based numbers as strings: "16" (which is P)

# To disable all replacements, set REPLACEMENTS = []

# modular to add/remove more columns as needed

REPLACEMENTS = [

    ("P", "H"),

    ("Q", "I"),

    # ("R", "J"),

]

 

def pick_latest_file(directory, exts=SUPPORTED_EXT):

    candidates = [

        os.path.join(directory, f)

        for f in os.listdir(directory)

        if f.lower().endswith(exts)

    ]

    return max(candidates, key=os.path.getmtime) if candidates else None

 

def read_table(path):

    # dtype=str preserves leading zeros and avoids Excel numeric coercion mismatches

    if path.lower().endswith(".csv"):

        return pd.read_csv(path, dtype=str)

    if path.lower().endswith(".xlsx"):

        return pd.read_excel(path, engine="openpyxl", dtype=str)

    return pd.read_excel(path, engine="xlrd", dtype=str)

 

def norm(x):

    """Trim, collapse internal whitespace, keep blanks stable."""

    if pd.isna(x):

        return ""

    s = str(x).strip()

    s = " ".join(s.split())

    return s

 

def build_outpath(out_dir, base="matched_bulk_rows", ext=".xlsx"):

    os.makedirs(out_dir, exist_ok=True)

    date = datetime.now().strftime("%Y%m%d")

    base_path = os.path.join(out_dir, f"{base}_{date}")

    out = f"{base_path}{ext}"

    i = 1

    while os.path.exists(out):

        out = f"{base_path}_{i}{ext}"

        i += 1

    return out

 

def excel_col_to_zero_based(col):

    """

    Accepts:

      - Excel letter(s): A, B, ..., Z, AA...

      - 1-based numeric strings: "1" means first column

      - 0-based numeric ints: 0 means first column (if user passes int)

    Returns 0-based index.

    """

    if col is None or str(col).strip() == "":

        return None

 

    # int input

    if isinstance(col, int):

        return col

 

    s = str(col).strip()

 

    # numeric (treat as 1-based for convenience)

    if s.isdigit():

        return int(s) - 1

 

    # letters

    s = s.upper()

    n = 0

    for ch in s:

        if not ("A" <= ch <= "Z"):

            raise ValueError(f"Invalid column reference: {col}")

        n = n * 26 + (ord(ch) - ord("A") + 1)

    return n - 1

 

def main():

    # file pickup

    for d in [BULK_DIR, MIGRATION_DIR, OUTPUT_DIR, ARCHIVE_DIR]:

        if not os.path.isdir(d):

            raise FileNotFoundError(f"Missing directory: {d}")

 

    bulk_file = pick_latest_file(BULK_DIR)

    mig_file = pick_latest_file(MIGRATION_DIR)

 

    if not bulk_file or not mig_file:

        raise FileNotFoundError(

            f"Missing input file(s). bulk_file={bulk_file}, migration_file={mig_file}"

        )

 

    bulk_df = read_table(bulk_file)

    mig_df = read_table(mig_file)

 

    # Matching Bulk Cols = A,B,C => 0,1,2

    # Matching Mig Cols  = B,C,D => 1,2,3

    bulk_k = bulk_df.iloc[:, [0, 1, 2]].applymap(norm)

    mig_k  = mig_df.iloc[:, [1, 2, 3]].applymap(norm)

 

    bulk_keys = pd.DataFrame(

        {"_k1": bulk_k.iloc[:, 0], "_k2": bulk_k.iloc[:, 1], "_k3": bulk_k.iloc[:, 2]}

    )

    mig_keys = pd.DataFrame(

        {"_k1": mig_k.iloc[:, 0], "_k2": mig_k.iloc[:, 1], "_k3": mig_k.iloc[:, 2]}

    )

 

    bulk_work = pd.concat([bulk_df, bulk_keys], axis=1)

    mig_work = pd.concat([mig_df, mig_keys], axis=1)

 

    # multiple cols replace

    if REPLACEMENTS:

        # matchindex

        bulk_index = pd.MultiIndex.from_frame(bulk_work[["_k1", "_k2", "_k3"]])

 

        for bulk_col_ref, mig_col_ref in REPLACEMENTS:

            replace_bulk_idx = excel_col_to_zero_based(bulk_col_ref)

            replace_mig_idx = excel_col_to_zero_based(mig_col_ref)

 

            # index error check

            if replace_bulk_idx < 0 or replace_bulk_idx >= len(bulk_df.columns):

                raise IndexError(f"Bulk replacement column out of range: {bulk_col_ref} -> idx {replace_bulk_idx}")

            if replace_mig_idx < 0 or replace_mig_idx >= len(mig_df.columns):

                raise IndexError(f"Migration replacement column out of range: {mig_col_ref} -> idx {replace_mig_idx}")

 

            bulk_target_col_name = bulk_df.columns[replace_bulk_idx]

            mig_source_col_name = mig_df.columns[replace_mig_idx]

 

            # Build mapping: key -> replacement value (last wins on duplicate keys)

            mig_map = (

                mig_work[["_k1", "_k2", "_k3", mig_source_col_name]]

                .dropna(subset=[mig_source_col_name])

                .drop_duplicates(subset=["_k1", "_k2", "_k3"], keep="last")

                .set_index(["_k1", "_k2", "_k3"])[mig_source_col_name]

            )

 

            repl_values = mig_map.reindex(bulk_index)  # aligned to bulk rows

            mask = repl_values.notna().to_numpy()

 

            bulk_work.loc[mask, bulk_target_col_name] = repl_values.to_numpy()[mask]

 

            print(f"Replaced bulk column '{bulk_target_col_name}' using migration column '{mig_source_col_name}'.")

 

    # filter only matching rows (if exist in migration data)

    mig_unique_keys = mig_work[["_k1", "_k2", "_k3"]].drop_duplicates()

    matched_bulk = bulk_work.merge(

        mig_unique_keys, on=["_k1", "_k2", "_k3"], how="inner"

    )

 

    # drop helper columns from output

    matched_bulk = matched_bulk.drop(columns=["_k1", "_k2", "_k3"])

 

    out_path = build_outpath(OUTPUT_DIR, base="matched_bulk_rows", ext=".xlsx")

    matched_bulk.to_excel(out_path, index=False)

 

    # archive inputs

    os.makedirs(ARCHIVE_DIR, exist_ok=True)

 

    # Avoid archive name collisions by timestamping if needed

    def safe_move(src_path, dest_dir):

        base = os.path.basename(src_path)

        dest_path = os.path.join(dest_dir, base)

        if os.path.exists(dest_path):

            name, ext = os.path.splitext(base)

            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            dest_path = os.path.join(dest_dir, f"{name}_{stamp}{ext}")

        shutil.move(src_path, dest_path)

        return dest_path

 

    archived_bulk = safe_move(bulk_file, ARCHIVE_DIR)

    archived_mig = safe_move(mig_file, ARCHIVE_DIR)

 

    print(f"Bulk file used: {bulk_file}")

    print(f"Migration file used: {mig_file}")

    print(f"Matched bulk rows written to: {out_path}")

    print(f"Bulk archived to: {archived_bulk}")

    print(f"Migration archived to: {archived_mig}")

 

if __name__ == "__main__":

    main()