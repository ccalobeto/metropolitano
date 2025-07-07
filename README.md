# Metropolitano Project

# Content

## Convert xlsx to parquet files
The python script will fetch all the xlsx files from `/Users/carlosalbertoleonliza/developer/projects/tutorials/datasets/atu-metropolitano` and export parquet files to `./data`. 

Run
```sh
python ./scripts/xlsxToCsv.py
```

## Make some statistics in clickhouse client
Counting rows
```sql
select count() from file('./atu/*.parquet')
```

Query of missing data
```sql
SELECT DISTINCT
    Ruta,
    Paradero
FROM file('./atu/*.parquet')
ORDER BY
    Ruta ASC,
    Paradero ASC
INTO OUTFILE './user_files/paraderos-alimentadores.csv'
```


