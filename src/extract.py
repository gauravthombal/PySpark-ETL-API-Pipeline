import requests
import json
import os

# API URL
url = "https://dummyjson.com/products"

# Fetch data
response = requests.get(url)

# Check request
if response.status_code == 200:

    # Convert response to JSON
    data = response.json()

    # Create folder if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)

    # Save JSON file
    with open("data/raw/products.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Data fetched successfully!")
    print("Saved as data/raw/products.json")

else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")