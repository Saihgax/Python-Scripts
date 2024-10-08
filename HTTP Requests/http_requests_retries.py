""" Write a Python function that fetches data from a public API and returns the parsed JSON response """
import requests
import time

def fetch_data_from_api(api_url, retries=3, back_off_factor=0.3):
    attempt = 0
    while attempt <= retries:
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
        # except requests.exceptions.RequestException as e:
            print(f"Getting the following error: {e}")
            # Exponential Backoff
            time.sleep(back_off_factor * (2 ** attempt))
            attempt += 1
    raise Exception(f"Failed to get fetch data from {api_url} after {retries} attempts.")

api_url = "https://jsonplaceholder.typicode.com/todos/10000"
data = fetch_data_from_api(api_url)
print(data)