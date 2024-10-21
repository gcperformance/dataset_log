import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

services = os.getenv('SERVICES')

if not services:
    raise EnvironmentError("Environment variable SERVICES is required")

output_dir = "services"
os.makedirs(output_dir, exist_ok=True)

for service, resource in json.loads(services).items():

  url = f"https://open.canada.ca/data/en/datastore/dump/{resource}"
  response = requests.get(url)
  response.raise_for_status()
  
  csv_file = os.path.join(output_dir, f"{service}.csv")
  with open(csv_file, 'wb') as file:
      file.write(response.content)
  
  print(f"{csv_file} saved successfully")

