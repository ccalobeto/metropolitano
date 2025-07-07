import pandas as pd
import os

input_folder = '/Users/carlosalbertoleonliza/developer/projects/tutorials/datasets/atu-metropolitano/test'
output_folder = './data'

data_types = {
  'Ubicacion': str
}

# Temporary list to collect DataFrames
dataframes = []

list_main_folder = os.listdir(input_folder)

for folder in list_main_folder:
  if folder != '.DS_Store':
    sub_folder = os.path.join(input_folder, folder)
    files = os.listdir(sub_folder)
    for file in files:
      if file.endswith('.xlsx'):
        print(f'---Processing file: {file}')
        df = pd.read_excel(os.path.join(sub_folder, file), header=0, skiprows=3, dtype=data_types)
        
        # do some data wrangling
        df.drop(df.columns[0], axis=1, inplace=True)
        df['from'] = file
        cols = df.columns.tolist()
        cols = ['from'] + [col for col in cols if col != 'from']
        df = df[cols]
        df['fecha_hora'] = df['Fecha'].dt.strftime('%Y-%m-%d') + ' ' + df['Hora']
        df['fecha_hora'] = pd.to_datetime(df['fecha_hora'], format='%Y-%m-%d %H:%M:%S')
        df.drop(['Fecha', 'Hora'], axis=1, inplace=True)
        
        dataframes.append(df)
        
    combined_df = pd.concat(dataframes, ignore_index=True)
    output_filePath = os.path.join(output_folder, folder.lower() + '_2025.csv')
    print(f'Processing filePath: {output_filePath}, Total rows: {len(combined_df)}')
    combined_df.to_csv(output_filePath, index=False)

    print(f'rows of {folder}: \n', combined_df.head(2))