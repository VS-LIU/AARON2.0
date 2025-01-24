import os
import requests
from dotenv import load_dotenv

from shared.utils import measure_response_time

load_dotenv()
AUTH_HEADER = os.getenv("AUTH_HEADER")
ACCOUNT = os.getenv("PUBLIC_KEY")
BASE_URL = os.getenv("URL_NY_FULL_API")


def get_account_balance():
    if not AUTH_HEADER:
        raise ValueError("AUTH_HEADER environment variable is not set.")

    # API endpoint
    print()
    print(">>>>>>>>>>>>>> `GET ./api/v2/balance`")
    print(BASE_URL)
    url = f"{BASE_URL}/api/v2/balance"

    # Headers
    headers = {
        "Authorization": AUTH_HEADER
    }

    # Query parameters
    params = {
        "ownerAddress": ACCOUNT
    }
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers, params=params)

        # Raise an exception for non-200 status codes
        response.raise_for_status()
        
        # Return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching balance: {e}")
        return None
    
    
def check_rate_limit():
    if not AUTH_HEADER:
        raise ValueError("AUTH_HEADER environment variable is not set.")


    print()
    print(">>>>>>>>>>>>>> `GET ./api/v2/rate-limit`")
    print(BASE_URL)
    url = f"{BASE_URL}/api/v2/rate-limit"

    headers = {
        "Authorization": AUTH_HEADER
    }

    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers)

        # Raise an exception for non-200 status codes
        response.raise_for_status()
        
        # Return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching rate limit: {e}")
        return None