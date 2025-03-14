from airflow import DAG #import DAG
from airflow.providers.https.hooks.http import HTTPHook #For interacting with the API 
from airflow.providers.hooks.postgres import PostgresHook #For pushing our data to Postgres
from airflow.decorators import task 
from airflow.utils.dates import days_ago 


