# Metropolitano Project

This project will discover some analytic insights related to the metropolitan service in Lima city.

With this project i am going to get the certification of [Data Engineering zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp.git)

To execute the project do the following

1. Install the library requeriments: `conda install requeriments.txt`
2. Upload `csv.gz` files in github `npm run git-upload`
3. Upload `csv` files into GCS bucket
4. Transform tables in BigQuery
5. See metrics in observablehq

## Scope

The trips were required to ATU, the Peruvian Transport entity who deliver me an [azure bucket](https://atugobpe.sharepoint.com/sites/DocumentosExternosSSTR/Documentos%20compartidos/Forms/AllItems.aspx?id=%2Fsites%2FDocumentosExternosSSTR%2FDocumentos%20compartidos%2FSSTR%20%2D%20UFAU%20%2D%20EXTERNO%2F7%29%20JULIO%20%2D%20SAIP%2FExp%2E%20N°4950%2D2025%2D02%2D0006762%20%2D%20CARLOS%20ALBERTO%20LEON%20LIZA&p=true&ga=1), where i can find the xls files. Data corresponds from January to May 25.

The project is divided into two parts:

- Import compressed files to a github repository
- Build an ELT pipeline to load these files GCS bucket, transform into useful metrics and display in an observable notebook

## 1.0 Importing files into Github

The `src/converter.py` script has the following features:

- The script reads daily `xlsx` files of each month (subfolder) and converts into a `csv.gz` compressed file month by month
- By default the script has the hability to process all the folders, but can also process a single subfolder entering the parameter **--month** like `src/converter.py --month JULIO`.
- You can use `npm run git-upload` to automate the process, see `package.json` file.

## 2.0 Build an ELT pipeline

The process is represented by these tasks:

- Extract the `csv.gz` files from github repository
- Load into GCS bucket
- Transform the compressed files into analytical tables in BQ
- Show key metrics or insights in an observablehq notebook

### 2.1 Upload `csv` files to GCS Bucket

- Quick GCP setup
  - Create project account
  - Create your service account, give it *permissions* and add a key
  - Place the key in a safety place in your computer
- `src/IaC` has all the code to create gcp resources
- Setup Kestra
  - `docker compose up -d` to spin up kestra and postgres db containers
  - Go to `http://localhost:18080` and give credentials placed in **KESTRA_CONFIGURATION** inside `docker-compose.yml`
  - Copy scripts `gcp-kv.yaml` and `gcp_taxi_scheduled.yalm` to kestra flows via *curl* like this

    ```sh
    curl -u admin@kestra.io:Admin1234 -X POST http://localhost:18080/api/v1/flows/import \
    -F "fileUpload=@flows/gcp_kv.yaml"

    ```

  - Add key **GOOGLE_CREDENTIALS_ID** in *KV Store* with your service account, copy the hole json key

  - Execute `.yaml` scrips in kestra
    - Execute `gcp_kv.yaml` to create kestra internal variables
    - Execute `gcp_scheduled.yaml` to perform ETL
