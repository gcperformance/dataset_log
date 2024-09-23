import os
import requests

dataset = os.getenv('DATASET')
resource = os.getenv('RESOURCE')
service = os.getenv('SERVICE')

if not all([dataset, resource, service]):
    raise EnvironmentError("Environment variables DATASET, RESOURCE, and SERVICE are required")

url = f"https://open.canada.ca/data/en/dataset/{dataset}/resource/{resource}"
response = requests.get(url)
response.raise_for_status()

csv_file = f"{service}.csv"
with open(csv_file, 'wb') as file:
    file.write(response.content)

print(f"{csv_file} saved successfully")

