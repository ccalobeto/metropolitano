import pandas as pd
import os

input_folder = '/Users/carlosalbertoleonliza/developer/projects/tutorials/datasets/atu-metropolitano/test'
output_folder = './data'

# Temporary list to collect DataFrames
dataframes = []

list_main_folder = os.listdir(input_folder)

for folder in list_main_folder:
  if folder != '.DS_Store':
    sub_folder = os.path.join(input_folder, folder)
    files = os.listdir(sub_folder)
    for file in files:
      if file.endswith('.xlsx'):
        print(f'subfolder: {folder}, Processing file: {file}')
        df = pd.read_excel(os.path.join(sub_folder, file), header=0, skiprows=3)
        df['file'] = file
        dataframes.append(df)
        
    combined_df = pd.concat(dataframes, ignore_index=True)
    output_filePath = os.path.join(output_folder, folder.lower() + '_2025.csv')
    print(f'Processing filePath: {output_filePath}, Total rows: {len(combined_df)}')
    combined_df.to_csv(output_filePath, index=False)
