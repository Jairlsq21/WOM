from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

from datetime import timedelta

# Parámetros
GCP_PROJECT_ID = 'wom-prueba'
GCS_BUCKET = 'files_repos2'
GCS_OBJECT = 'file/datos.csv'
BQ_DATASET = 'WOM_Dataset'
BQ_RAW_TABLE = 'tabla_raw'
BQ_TRANSFORMED_TABLE = 'tabla_transformada'

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='gcs_to_bq_transform',
    default_args=default_args,
    description='Carga archivo CSV desde GCS a BigQuery y transforma la data',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    tags=['gcs', 'bigquery'],
) as dag:

    # 1. Cargar archivo desde GCS a BigQuery
    load_csv_to_bq = GCSToBigQueryOperator(
        task_id='load_csv_to_bq',
        bucket=GCS_BUCKET,
        source_objects=[GCS_OBJECT],
        destination_project_dataset_table=f'{BQ_DATASET}.{BQ_RAW_TABLE}',
        skip_leading_rows=1,
        source_format='CSV',
        write_disposition='WRITE_TRUNCATE',
        field_delimiter=',',
        autodetect=True,
    )

    

    load_csv_to_bq 
