MERGE INTO `{{kv('GCP_PROJECT_ID')}}.{{kv('GCP_DATASET')}}.alimentadores_tripdata` T USING `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}` S ON T.unique_row_id = S.unique_row_id
WHEN NOT MATCHED THEN
INSERT
  (
    unique_row_id,
    filename,
    operador_id,
    operador,
    ubicacion,
    fecha_hora,
    nombre_titulo,
    ruta,
    paradero,
    monto
  )
VALUES
  (
    S.unique_row_id,
    S.filename,
    S.operador_id,
    S.operador,
    S.ubicacion,
    S.fecha_hora,
    S.nombre_titulo,
    S.ruta,
    S.paradero,
    S.monto
  );