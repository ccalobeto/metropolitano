# Metropolitano Project

Here you will find more details on how i achieved into an automated solution for my project to get the certificate of Data Engineering zoomcamp

## Scope

The trips were required to ATU entity who deliver me a bucket in azure where i can find the xls files. In case of `alimentadores` folder data was delivered day by day during the first 5 months of 2025. In case of `Rutas Troncales` the were delivered by station

The project is divided into two parts:

- Importing the xlsx files to github repository
- Build an ELT pipeline to load intp GCS bucket, transform into useful metrics and display in observable notebooks

## Importing files into Github

This process will extract xlsx files from azure bucket and convert it to `csv.gz` compresed files. The files will be prepared before they are delivered to github

Tools used: python, kestra

Scripts to run in terminal

```sh
python ./scripts/xlsxToCsv.py
```

```sh
python ./scripts/xlsxToCsvTroncales.py
```

## Build an ELT pipeline

The process is represented by these tasks:

- Extract the `csv.gz` files from github repository
- Load into GCS bucket
- Transform

## Convert xlsx to parquet files

The python script will fetch all the xlsx files from `/Users/carlosalbertoleonliza/developer/projects/tutorials/datasets/atu-metropolitano` and export parquet files to `./data`.
