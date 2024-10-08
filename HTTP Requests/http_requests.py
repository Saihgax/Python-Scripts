""" Write a Python function that fetches data from a public API and returns the parsed JSON response """
import requests

def fetch_data_from_api(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Api request failed with status code {response.status_code}")


api_url = "https://jsonplaceholder.typicode.com/todos/1"
data = fetch_data_from_api(api_url)
print(data)