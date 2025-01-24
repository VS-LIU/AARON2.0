import os
import requests
from dotenv import load_dotenv

load_dotenv()
AUTH_HEADER = os.getenv("AUTH_HEADER")
ACCOUNT = os.getenv("PUBLIC_KEY")
BASE_URL = os.getenv("URL_NY_FULL_API")

import requests

def get_coin_data(coin_ticker):
    """Fetch data for a specific coin."""
    try:
        # Replace `API_BASE_URL` with the actual endpoint for coin details
        response = requests.get(f"{API_BASE_URL}/coins/{coin_ticker}")
        if response.status_code == 200:
            data = response.json()
            print(f"Data for {coin_ticker}:")
            print(data)
        else:
            print(
                f"Error: Unable to fetch data for {coin_ticker} (HTTP {response.status_code})"
            )
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        
        
def get_pools():
    """
    type: GET
    endpoint: /api/v2/raydium/pools
    """
    url = f"{BASE_URL}/api/v2/raydium/pools"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching pools: {e}")
        return None