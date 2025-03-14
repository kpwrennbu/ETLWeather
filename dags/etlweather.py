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

##DAG 
with DAG(dag_id='weather_etl_pipeline', #gives dag an id
         default_args=default_args, #gives it our args above
         schedule_interval='@days', #runs daily
         catchup=False
         ) as dags: 
    
    @task() 
    def extract_weather_data(): 
        """Extract weather data from Open-Meteo API using Airflow Connection."""
        
        #Use HTTP Hook to get connection detail from Airflow connection
        
        http_hook = HTTPHook(http_conn_id=API_CONN_ID, method="GET")
        
        # Build the API endpoint 
        # https://api.open-meteo.com/
        endpoint=f'/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true'
        
        #Make the request via the HTTP Hook 
        response = htt_hook.run(endpoint)
        
        if response.status_code == 200: 
            return response.json() 
        else: 
            raise Exception(f"Failed to fetch weather data: {response.status_code}")