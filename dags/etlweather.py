from airflow import DAG #import DAG
from airflow.providers.https.hooks.http import HTTPHook #For interacting with the API 
from airflow.providers.hooks.postgres import PostgresHook #For pushing our data to Postgres
from airflow.decorators import task 
from airflow.utils.dates import days_ago 

#Latitude and Longitude for desired Location (Cohasset Mass)
LATITUDE = '42.2417'
LONGITUDE = '-70.8119'
POSTGRES_CONN_ID='postrgres_default' #to connect to DB
API_CONN_ID='open_meteo_id' #connection name so we keep a note of it 

default_args={
    'owner': 'airflow', 
    'start_date': days_ago(1)
}