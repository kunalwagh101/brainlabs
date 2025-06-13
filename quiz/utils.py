import requests

API_URL = "https://countriesnow.space/api/v0.1/countries/capital"

def fetch_countries_from_api():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("error"):
            raise Exception("API Error")
        return data["data"]
    except Exception as e:
        return {"error": str(e)}
