'''
=============================================================================================================

This program is designed to automate the transformation and loading of data from PostgreSQL to ElasticSearch. 
The dataset used is a dataset about historical sales of a supermarket company, which has been recorded in 3 
different branches for 3 months of data.

=============================================================================================================

'''

# Import libraries
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd


# Reads a CSV file and uploads to a PostgreSQL database
def load_csv_to_postgres():
    database = "airflow_maudy"
    username = "airflow"
    password = "airflow"
    host = "postgres"

    # Create URL to PostgreSQL
    postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

    # Create URL to SQLAlchemy
    engine = create_engine(postgres_url)
    conn = engine.connect()
    df = pd.read_csv('/opt/airflow/dags/P2M3_maulidya_fauziyyah_data_raw.csv')
    df.to_sql('table_m', conn, index=False, if_exists='replace')  # Menggunakan if_exists='replace' agar tabel digantikan jika sudah ada



# Connects to a PostgreSQL database using SQLAlchemy, retrieves all data from the table table_m, and saves it as a CSV file to the specified path on the Airflow server.
def ambil_data():
    # fetch data
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres/airflow_maudy")
    conn = engine.connect()

    df = pd.read_sql_query("select * from table_m", conn)
    df.to_csv('/opt/airflow/dags/P2M3_maulidya_fauziyyah.csv', sep=',', index=False)



# Reads a CSV file, cleans the data by removing missing values and duplicates, set column names to lowercase, converts columns to appropriate data types, and then saves the cleaned and transformed data to a new CSV file.
def preprocessing(): 
    data = pd.read_csv("/opt/airflow/dags/P2M3_maulidya_fauziyyah.csv")

    # clean up data 
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)

    # lowercase columns
    data.columns = ['invoice_id', 'branch', 'city', 'customer_type',
                    'gender', 'product_line', 'unit_price', 'quantity',
                    'tax_5', 'total', 'date', 'time', 'payment', 'cogs', 
                    'gross_margin_percentage', 'gross_income', 'rating']

    # convert data type
    data['unit_price'] = data['unit_price'].astype(int)
    data['quantity'] = data['quantity'].astype(int)
    data['tax_5'] = data['quantity'].astype(float)
    data['total'] = data['quantity'].astype(float)
    data['cogs'] = data['quantity'].astype(float)
    data['gross_margin_percentage'] = data['quantity'].astype(float)
    data['gross_income'] = data['quantity'].astype(float)
    data['rating'] = data['quantity'].astype(float)

    data['date'] = data['date'].astype('datetime64')
    data['time']= data['time'].astype('datetime64[h]')

    data.to_csv('/opt/airflow/dags/P2M3_maulidya_fauziyyah_clean.csv', index=False)



# Reads a CSV file, converts each row to a dictionary, and indexes the data into an Elasticsearch index named "table_new" and uploading the data to Elasticsearch.
def upload_to_elasticsearch():
    es = Elasticsearch("http://elasticsearch:9200")
    df = pd.read_csv('/opt/airflow/dags/P2M3_maulidya_fauziyyah_clean.csv')
    
    for i, r in df.iterrows():
        doc = r.to_dict()  # Convert the row to a dictionary
        res = es.index(index="table_new", id=i+1, 
                       body=doc, 
                       #op_type="index"
                       )
        print(f"Response from Elasticsearch: {res}")



# Defines an Airflow DAG named "P2M3_maulidya_fauziyyah_DAG" with a schedule to run at 6:30 AM daily, ands a sequence of tasks including loading CSV data to PostgreSQL, fetching data from PostgreSQL, preprocessing the data, and uploading it to Elasticsearch.        
default_args = {
    'owner': 'Maulidya',
    'start_date': datetime(2023, 12, 24, 12, 00)
}
# Define DAG with a schedule to run at 6:30 AM daily
with DAG(
    "P2M3_maulidya_fauziyyah_DAG",
    description='Milestone_3',
    schedule_interval='30 6 * * *',
    default_args=default_args, 
    catchup=False
) as dag:
    # Task
    load_csv_task = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=load_csv_to_postgres)
    
    # Task: 1
    '''  Fungsi ini ditujukan untuk menjalankan ambil data dari postgresql. '''
    fetching_data = PythonOperator(
        task_id='fetching_data',
        python_callable=ambil_data)

    # Task: 2
    '''  Fungsi ini ditujukan untuk menjalankan pembersihan data.'''
    edit_data = PythonOperator(
        task_id='edit_data',
        python_callable=preprocessing)

    # Task: 3
    '''  Fungsi ini ditujukan untuk menjalankan upload data ke elasticsearch.'''
    upload_data = PythonOperator(
        task_id='upload_data_elastic',
        python_callable=upload_to_elasticsearch)

    # The sequence of tasks in the Airflow:
    # with TaskGroup("processing_tasks") as processing_tasks:
    load_csv_task >> fetching_data >> edit_data >> upload_data      