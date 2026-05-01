---

# Weather Forecast ETL Pipeline

A Data Engineering project built while learning how to handle automated data pipelines. 

This project pulls weather data from an API, cleans it up, and saves it into a cloud Postgres database.

## Project Workflow
1.  **Extract:** Fetches 7-day weather forecasts (temperature and rain) from **Open-Meteo API**.
2.  **Transform:** Uses **Python** and **Pandas** to turn that raw API data into a clean, organized table format.
3.  **Load:** Connects to an **Aiven PostgreSQL** database and saves the data.

## Tech Stack
*   **Language:** Python 3.12+
*   **Environment Manager:** `uv` (for fast, reliable package management)
*   **Operating System:** Windows Subsystem for Linux (WSL)
*   **Database:** Aiven Managed PostgreSQL
*   **Libraries:** `psycopg2` (for database connection), `pandas` (for data cleaning), and `openmeteo-requests`.

## Project Structure
*   `main.py`: The "brain" of the project that runs the whole process
*   `extract_data.py`: Handles the API calls to Open-Meteo
*   `transform_data.py`: Cleans the data and handles timestamps
*   `load_data.py`: Manages the connection to Aiven and inserts the data

<!--## Key Features
*   **Idempotency:** The script uses `CREATE TABLE IF NOT EXISTS`, so it won't crash if you run it multiple times.
*   **Security:** Sensitive database credentials are kept in a `.env` file and are hidden from GitHub via `.gitignore`.
*   **Efficiency:** Uses `requests_cache` to avoid hitting the API too many times during testing. -->

## How to Run
1. Clone this repo to your environment.
2. Create a `.env` file and add your `AIVEN_URI`.
3. Run the pipeline using `uv`:
   ```bash
   uv run main.py
   ```

---
