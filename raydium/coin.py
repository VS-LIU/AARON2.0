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