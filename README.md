# Metropolitano Project

This project will discover some analytic insights related to the metropolitan service in Lima city.

With this project i am going to get the certification of [Data Engineering zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp.git)

To execute the project do the following

1. Install the library requeriments: `conda install requeriments.txt`
2. To upload `csv.gz` files in github `npm run git-upload`

## Scope

The trips were required to ATU, the Peruvian Transport entity who deliver me an [azure bucket](https://atugobpe.sharepoint.com/sites/DocumentosExternosSSTR/Documentos%20compartidos/Forms/AllItems.aspx?id=%2Fsites%2FDocumentosExternosSSTR%2FDocumentos%20compartidos%2FSSTR%20%2D%20UFAU%20%2D%20EXTERNO%2F7%29%20JULIO%20%2D%20SAIP%2FExp%2E%20N°4950%2D2025%2D02%2D0006762%20%2D%20CARLOS%20ALBERTO%20LEON%20LIZA&p=true&ga=1), where i can find the xls files. Data corresponds from January to May 25.

The project is divided into two parts:

- Import compressed files to a github repository
- Build an ELT pipeline to load these files GCS bucket, transform into useful metrics and display in an observable notebook

## 1.0 Importing files into Github

The `src/converter.py` script has the following features:

- The script reads daily `xlsx` files of each month (subfolder) and converts into a `csv.gz` compressed file month by month
- By default the script has the hability to process all the folders, but can also process a single subfolder entering the parameter `src/converter.py --month JULIO`.
- You can use `npm run git-upload` to automate the process, see `package.json` file.

## 2.0 Build an ELT pipeline

The process is represented by these tasks:

- Extract the `csv.gz` files from github repository
- Load into GCS bucket
- Transform the compressed files into analytical tables in BQ
- Show key metrics or insights in an observablehq notebook
