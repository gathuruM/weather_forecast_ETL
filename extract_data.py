import requests
import openmeteo_requests
import requests_cache
from retry_requests import retry

# Listing Coordinates
latitudes = [-1.2833, -1.167778, -1.107778, -4.0547, -0.1022, 1.3333, 0.3136, 9.0227]
longitudes = [36.8167, 36.973333, 36.642778, 39.6636, 34.7617, 37.1167, 32.5811, 38.7469]

# Nairobi: -1.2833, 36.8167
# Ruiru : -1.167778; Longitude: 36.973333
# Limuru : -1.107778; Longitude: 36.642778
# Mombasa:-4.0547, 39.6636
# Kisumu : -0.1022, 34.7617
# Samburu : 1.3333, 37.1167° E
# Kampala : 0.3136, 32.5811
# Addis Ababa : 9.0227, 38.7469

# Extract Function
def extract_data():
    # Setting up the Open-Meteo API Client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 2)
    open_meteo = openmeteo_requests.Client(session = retry_session)

    # Defining variables
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude" : latitudes,
        "longitude" : longitudes,
        "hourly" : ["temperature_2m", "rain"],
        "timezone" : "auto"
    }

    try:
        responses = open_meteo.weather_api(url, params=params)
        print("Successful Data Extraction")

    except Exception as e:
        print(f"Error fetching data {e}")

    return responses
