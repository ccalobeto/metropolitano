import pandas as pd
import os

input_folder = '/Users/carlosalbertoleonliza/developer/projects/tutorials/datasets/atu-metropolitano/Rutas Troncales_'
output_folder = './data'

types = {
    'Fecha_Incidencia': 'datetime64[ns]',
}
# Temporary list to collect DataFrames
dataframes = []

# Get the files
files = os.listdir(input_folder)

for file in files:
  if file.endswith('.xlsx'):
    print(f'---Processing file: {file}')
    df = pd.read_excel(os.path.join(input_folder, file), header=0, dtype=types)
    
    # print(f'types: {df.dtypes}')
    # do some data wrangling
    df['from'] = file
    cols = df.columns.tolist()
    cols = ['from'] + [col for col in cols if col != 'from']
    df = df[cols]
    df['fecha_salida'] = df['Fecha_Incidencia'].dt.strftime('%Y-%m-%d') + ' ' + df['Salida']
    df['fecha_salida'] = pd.to_datetime(df['fecha_salida'], format='%Y-%m-%d %H:%M:%S')
    df['fecha_POD'] = df['Fecha_Incidencia'].dt.strftime('%Y-%m-%d') + ' ' + df['POD']
    df['fecha_POD'] = pd.to_datetime(df['fecha_POD'], format='%Y-%m-%d %H:%M:%S')

    dataframes.append(df)
    
combined_df = pd.concat(dataframes, ignore_index=True)
output_filePath = os.path.join(output_folder, 'troncales_2025.parquet')
print(f'Processing filePath: {output_filePath}, Total rows: {len(combined_df)}')
combined_df.to_parquet(output_filePath, index=False)