from extract_data import extract_data
from transform_data import transform_data
from load_data import load_data


def run_etl():
    # EXTRACT
    responses = extract_data()

    # TRANSFORM
    transformed_data = transform_data(responses)

    # LOAD
    load_data(transformed_data)
    # print("Hello from weather-project!")


if __name__ == "__main__":
    run_etl()
