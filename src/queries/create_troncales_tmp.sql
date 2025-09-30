CREATE
OR REPLACE TABLE `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}` AS
SELECT
  MD5(
    CONCAT(
      COALESCE(CAST(block_id AS STRING), ""),
      COALESCE(CAST(fecha_hora_incidencia AS STRING), ""),
      COALESCE(CAST(route_name AS STRING), ""),
      COALESCE(CAST(vehicle_id AS STRING), "")
    )
  ) AS unique_row_id,
  "{{render(vars.file)}}" AS filename,
  *
FROM
  `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}_ext`;