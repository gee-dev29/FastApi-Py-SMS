import os
from urllib import response

import requests


def normalize_country(country: dict) -> dict:
  capitals = country.get("capitals") or []
  continents = country.get("continents") or []
  currencies = country.get("currencies") or []
  descriptions = country.get("descriptions") or {}
  calling_codes = country.get("calling_codes") or []

  return {
    "name": country.get("names", {}).get("common"),
    "capital": capitals[0].get("name") if capitals else None,
    "continent": continents[0] if continents else None,
    "coordinate": country.get("coordinates"),
    "currency": currencies[0].get("name") if currencies else None,
    "description": descriptions.get("long"),
    "population": float(country["population"]) if country.get("population") is not None else None,
    "phone_code": calling_codes[0] if calling_codes else None,
    "timezones": country.get("timezones") or [],
  }

class countryApiClient:
  def __init__(self):
    self.base_url = os.getenv(
      "API_URL"
    )
    self.api_key = os.getenv("API_KEY")

  def getCountries(self) -> list[dict]:
    try:
      if not self.api_key:
        raise RuntimeError("API_KEY is not set in the environment variables")
      response = requests.get(
        self.base_url,
        headers={
          "Accept": "application/json",
          "Authorization": f"Bearer {self.api_key}",
        },
        params={"api-key": self.api_key},
        timeout=(3.0, 10.0),
      )

      response.raise_for_status()
      payload = response.json()
      countries = payload.get("data", {}).get("objects", [])
      return [normalize_country(country) for country in countries]
    except requests.exceptions.RequestException as e:
      raise RuntimeError(f"Error fetching countries: {e}") from e

  def getStates(self, country_code: str) -> list[dict]:
    try:
      response = requests.get(
          f"https://api.countrystatecity.in/v1/countries/{country_code}/states",
          headers={
            "Accept": "application/json",
            "X-CSCAPI-KEY": self.api_key,
          },
        timeout=(3.0, 10.0),
      )

      response.raise_for_status()
      payload = response.json()
      return payload if isinstance(payload, list) else payload.get("records", [])
    except requests.exceptions.RequestException as e:
      raise RuntimeError(f"Error fetching states: {e}") from e