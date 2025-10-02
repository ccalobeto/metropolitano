import argparse
import pandas as pd
import pathlib

INPUT_DIR = pathlib.Path("datasets/input/Alimentadores")
OUTPUT_DIR = pathlib.Path("datasets/alimentadores/")
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
MAP_COLUMNS = {
    "# Operador": "operador_id",
    "Operador": "operador",
    "Ubicacion": "ubicacion",
    "Fecha": "fecha_hora",
    "Nombre del titulo": "nombre_titulo",
    "Ruta": "ruta",
    "Paradero": "paradero",
    "Monto S/.": "monto",

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
            # remove ghost cols
            df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
            # remove leading/trailing whitespace from string columns
            df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
            dataframes.append(df)
            print(f"Loaded {f.name} ({len(df)} rows)")
        except Exception as e:
            print(f"❌ Failed to load {f}: {e}")

    if not dataframes:
        print(f"⚠️ Skipping {month_dir}, no valid Excel files")
        return

    # Concatenate daily files into one monthly dataframe
    combined = pd.concat(dataframes, ignore_index=True)
    
    # combine 'Fecha' and 'Hora' into single datetime column
    combined['Fecha'] = pd.to_datetime(
        combined['Fecha'].dt.strftime('%Y-%m-%d') + ' ' + combined['Hora'], format='%Y-%m-%d %H:%M:%S'
    )
    combined.drop(['Hora'], axis=1, inplace=True)
    # rename columns
    combined.rename(columns=MAP_COLUMNS, inplace=True)

    # Filename pattern
    month = MAP_MONTHS[month_dir.name]  # e.g. "2025-01"
    out_path = OUTPUT_DIR / f"alimentadores_tripdata_2025-{month}.csv.gz"

    combined.to_csv(out_path, index=False, compression="gzip")
    print(f"✅ Wrote {out_path} ({len(combined)} rows total)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", help="Process only this month (e.g. 'ENERO')")
    args = parser.parse_args()

    if args.month:
        month_dir = INPUT_DIR / args.month
        if month_dir.exists():
            process_month(month_dir)
        else:
            print(f"⚠️ Month folder not found: {args.month}")
            
    else:
    # Each subfolder = one month
        month_dirs = [d for d in INPUT_DIR.iterdir() if d.is_dir()]

        if not month_dirs:
            print("⚠️ No month subfolders found in data/input/")
            return

        for month_dir in sorted(month_dirs):
            process_month(month_dir)


if __name__ == "__main__":
    main()

