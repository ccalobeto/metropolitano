CREATE
OR REPLACE EXTERNAL TABLE `{{kv('GCP_PROJECT_ID')}}.{{render(vars.table)}}_ext` (
    block_id INT64 OPTIONS (
        description = 'Block identifier from schedule, e.g. 7103'
    ),
    fecha_hora_incidencia TIMESTAMP OPTIONS (
        description = 'Incidence timestamp (sample format: D/MM/YYYY H:MM:SS)'
    ),
    route_name STRING OPTIONS (
        description = 'Route name, e.g. "RB - Regular B"'
    ),
    tp_sname STRING OPTIONS (
        description = 'Trip pattern short name or stop short name, e.g. "NARL"'
    ),
    direction_description STRING OPTIONS (description = 'Direction, e.g. "Sur", "Norte"'),
    pod STRING OPTIONS (
        description = 'Planned time of departure or POD field (sample shows values like 6:36:00)'
    ),
    hora_sched STRING OPTIONS (
        description = 'Scheduled hour field from CSV (could be an integer hour or time string)'
    ),
    deviation INT64 OPTIONS (
        description = 'Deviation in minutes from schedule (can be negative)'
    ),
    vehicle_id INT64 OPTIONS (description = 'Vehicle identifier, e.g. 11083'),
    mes STRING OPTIONS (
        description = 'Month name in English from source CSV, e.g. April'
    )
) OPTIONS (
    format = 'CSV',
    uris = ['{{render(vars.gcs_file)}}'],
    skip_leading_rows = 1,
    ignore_unknown_values = TRUE
);