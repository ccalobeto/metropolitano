CREATE
OR REPLACE EXTERNAL TABLE `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}_ext` (
    operador_id INT64 OPTIONS (
        description = 'Numeric operator id taken from the first CSV column (e.g. 14, 13)'
    ),
    operador STRING OPTIONS (
        description = 'Operator name, e.g. "Peru Masivo", "Transvial"'
    ),
    ubicacion INT64 OPTIONS (
        description = 'Numeric location code from CSV (third column)'
    ),
    fecha_hora TIMESTAMP OPTIONS (
        description = 'Datetime of the record parsed from CSV (format: YYYY-MM-DD HH:MM:SS)'
    ),
    nombre_titulo STRING OPTIONS (
        description = 'Title/name field shown in CSV (e.g. "Tarjeta con valor anonymo", "TV Estudiante")'
    ),
    ruta STRING OPTIONS (
        description = 'Route name or label from CSV (may be padded with spaces)'
    ),
    paradero STRING OPTIONS (
        description = 'Stop or station name (may contain special characters)'
    ),
    monto NUMERIC OPTIONS (
        description = 'Fare amount in local currency, decimal value'
    )
) OPTIONS (
    format = 'CSV',
    uris = ['{{render(vars.gcs_file)}}'],
    skip_leading_rows = 1,
    ignore_unknown_values = TRUE
);