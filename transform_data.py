import pandas as pd

def transform_data(responses):
    dataframes = []

    for response in responses:
        # print(f"Coordinates: {response.Latitude()}°N, {response.Longitude()}°E")
        # print(f"Timezone: {response.Timezone()} {response.TimezoneAbbreviation()}")

        # Process Data with Time(Hourly)
        hourly = response.Hourly()
        
        hourly_data = {
            "date" : pd.date_range(
                start=pd.to_datetime(hourly.Time() + response.UtcOffsetSeconds(), unit='s'),
                end=pd.to_datetime(hourly.TimeEnd() + response.UtcOffsetSeconds(), unit='s'),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive='left'
                ),
            "latitude" : response.Latitude(),
            "longitude" : response.Longitude(),
            "temprature" : hourly.Variables(0).ValuesAsNumpy(),
            "rain" : hourly.Variables(1).ValuesAsNumpy()
        }

        dataframes.append(pd.DataFrame(data = hourly_data))
        
        data = pd.concat(dataframes, ignore_index=True)
    print("Data successfully transformed!")

    return data