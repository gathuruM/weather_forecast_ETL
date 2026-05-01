import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values

load_dotenv() 
# Assemble URI from .env variables
URI = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?sslmode=require"

# Create the table where data will be stored
def create_first_table():
    create_query = """
    CREATE TABLE IF NOT EXISTS weather_forecast(
    id SERIAL PRIMARY KEY,
    date TIMESTAMPTZ,
    latitude FLOAT,
    longitude FLOAT,
    temperature FLOAT,
    rain FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

    try:
        conn = psycopg2.connect(URI)

        # create cursor for query execution
        cursor = conn.cursor()
        cursor.execute(create_query)

        # Save changes
        conn.commit()
        print("Table 'weather_forecast' successfully created!")

    except Exception as e:
        conn.rollback()
        print(f"Error creating table: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

# Connect, Insert, Close
def load_data(data):

    create_first_table()

    query = """
    INSERT INTO weather_forecast (date, latitude, longitude, temperature, rain) VALUES %s"""

    # convert data to tuples
    data_tuples = list(data.itertuples(index=False, name=None))

    try:
        conn = psycopg2.connect(URI)

        # create cursor
        cursor = conn.cursor()
        print("Inserting rows into the Database")
        execute_values(cursor, query, data_tuples)

        # Save changes
        conn.commit()
        print(f"Successfully loaded {len(data)} records")

    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
