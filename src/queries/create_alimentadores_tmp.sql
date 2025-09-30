CREATE
OR REPLACE TABLE `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}` AS
SELECT
  MD5(
    CONCAT(
      COALESCE(CAST(operador_id AS STRING), ""),
      COALESCE(CAST(fecha_hora AS STRING), ""),
      COALESCE(CAST(ubicacion AS STRING), ""),
      COALESCE(CAST(ruta AS STRING), ""),
      COALESCE(CAST(paradero AS STRING), "")
    )
  ) AS unique_row_id,
  "{{render(vars.file)}}" AS filename,
  *
FROM
  `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}_ext`;