import pandas as pd
import pathlib

INPUT_DIR = pathlib.Path("data/input/test")
OUTPUT_DIR = pathlib.Path("data/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MAP_MONTHS = {
    "ENERO": "01",
    "FEBRERO": "02",
    "MARZO": "03",
    "ABRIL": "04",
    "MAYO": "05",
    "JUNIO": "06",
    "JULIO": "07",
    "AGOSTO": "08",
    "SETIEMBRE": "09",
    "OCTUBRE": "10",
    "NOVIEMBRE": "11",
    "DICIEMBRE": "12",
}


def process_month(month_dir: pathlib.Path):
    """Read all Excel files in a month folder, concatenate, and save one .csv.gz"""
    all_files = sorted(month_dir.glob("*.xlsx"))
    if not all_files:
        print(f"⚠️ No Excel files found in {month_dir}")
        return

    dataframes = []
    for f in all_files:
        try:
            df = pd.read_excel(f, engine="openpyxl", skiprows=2, header=1)
            df = df.loc[:, ~df.columns.str.contains("^Unnamed")]  # remove ghost cols
            dataframes.append(df)
            print(f"📥 Loaded {f.name} ({len(df)} rows)")
        except Exception as e:
            print(f"❌ Failed to load {f}: {e}")

    if not dataframes:
        print(f"⚠️ Skipping {month_dir}, no valid Excel files")
        return

    # Concatenate daily files into one monthly dataframe
    combined = pd.concat(dataframes, ignore_index=True)

    # Filename pattern
    month = MAP_MONTHS[month_dir.name]  # e.g. "2025-01"
    out_path = OUTPUT_DIR / f"metropolitano_tripdata_2025-{month}.csv.gz"

    combined.to_csv(out_path, index=False, compression="gzip")
    print(f"✅ Wrote {out_path} ({len(combined)} rows total)")


def main():
    # Each subfolder = one month
    month_dirs = [d for d in INPUT_DIR.iterdir() if d.is_dir()]

    if not month_dirs:
        print("⚠️ No month subfolders found in data/input/")
        return

    for month_dir in sorted(month_dirs):
        process_month(month_dir)


if __name__ == "__main__":
    main()

