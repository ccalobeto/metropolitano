# Metropolitano Project

# Content

## Convert xlsx to parquet files
The python script will fetch all the xlsx files from `/Users/carlosalbertoleonliza/developer/projects/tutorials/datasets/atu-metropolitano` and export parquet files to `./data`. 

Run
```sh
python ./scripts/xlsxToCsv.py
```
or 
```sh
python ./scripts/xlsxToCsvTroncales.py
```

## Make some statistics in clickhouse client
### Alimentadores
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

### Troncales

Counting rows
```sql
select count() from file('./atu/troncales_2025.parquet') 
```

Query data
```sql
SELECT DISTINCT
    route_name,
    TP_SNAME
FROM file('./atu/troncales_2025.parquet')
ORDER BY
    route_name ASC,
    TP_SNAME ASC
INTO OUTFILE './user_files/paraderos-troncales.csv'
```
