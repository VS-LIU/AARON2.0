import argparse
import os
import requests
from dotenv import load_dotenv
import json

from raydium.raydium import get_coin_data
from api.api import get_status
from shared.settings import get_settings, get_version
from account.account import get_account_balance, check_rate_limit

from assets import TITLE_ART

from shared.utils import measure_response_time

# API_BASE_URL = "https://api.example.com/crypto" 
# APP_VERSION = "1.0.0"


def cli():
    # settings
    MEASURE_RESPONSE_TIME = False
    DEBUG_MODE = True
    
    
    load_dotenv()
    
    if DEBUG_MODE:
        if not os.getenv("CHECK"):
            print("dotenv failed to load")
        else:
            print("Environment variables loaded successfully")
    
    response_time_setting = "ON" if MEASURE_RESPONSE_TIME else "OFF"
    
    parser = argparse.ArgumentParser(description="\"A-A-RON 2.0\" WIP")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    subparsers.add_parser("help", help="✅ Display the help menu")

    subparsers.add_parser("status", help="❌ Check the API status")
    
    # ACCOUNT settings
    account_parser = subparsers.add_parser("account", help="✅ Check your account status and details")
    account_parser.add_argument(
    "-b", "--balance", 
    action="store_true",  
    help="Check your account balance"
    )
    account_parser.add_argument(
    "-r", "--rate", 
    action="store_true",  
    help="Check your account's rate limit"
    )

    # SETTINGS for the CLI
    settings_parser = subparsers.add_parser("settings", help="✅ View current CLI settings")
    settings_parser.add_argument(
    "-mrt", "--measure_response_time", 
    action="store_true",  
    help="Measure the response time of API requests (Currently: " + response_time_setting + ")"
    )

    # FILTERS for BUY and SELL
    subparsers.add_parser("filters", help="❌ View the current filters (buy and sell)")

    # VERSION @TODO most likely delete
    subparsers.add_parser("version", help="❌ Display the application version")

    # COIN
    coin_parser = subparsers.add_parser("coin", help="❌ Fetch data for a specific coin")
    coin_parser.add_argument(
        "ticker", help="The ticker symbol of the coin (e.g., BTC, ETH, DOGE)"
    )

    print("Starting up...")
    print(TITLE_ART)
    parser.print_help()

    while True:
        try:
            user_input = input("Enter a command: ").strip().split()
            if not user_input:
                continue  

            if user_input[0].lower() in {"exit", "quit"}:
                print("Goodbye!")
                break

            args = parser.parse_args(user_input)
            if args.command == "help":
                parser.print_help()
            elif args.command == "account":
                if args.balance:
                    if MEASURE_RESPONSE_TIME:
                        balance_result, balance_time = measure_response_time(get_account_balance)
                        print(f"Response Time: {balance_time:.2f} ms")
                        print("Account Balance Response:", json.dumps(balance_result, indent=4))
                    else:
                        balance = get_account_balance()
                        print(f"Account balance: {json.dumps(balance, indent=4)}")
                elif args.rate:
                    if MEASURE_RESPONSE_TIME:
                        rate_limit_result, rate_limit_time = measure_response_time(check_rate_limit)
                        print(f"Response Time: {rate_limit_time:.2f} ms")
                        print("Rate Limit Response:", json.dumps(rate_limit_result, indent=4))
                    else:
                        rate_limit = check_rate_limit()
                        print(f"Rate limit: {json.dumps(rate_limit, indent=4)}")
                else:
                    print("Error: Missing or invalid argument.\n")
            elif args.command == "status":
                get_status()
            elif args.command == "settings":
                if args.measure_response_time:
                    if not MEASURE_RESPONSE_TIME:
                        MEASURE_RESPONSE_TIME = True
                        print("Measuring API response time enabled.")
                    else:
                        MEASURE_RESPONSE_TIME = False
                        print("Measuring API response time disabled.")
                else:
                    print("Current settings:")
                    print(f"\tMeasure API response time: {"ON" if MEASURE_RESPONSE_TIME else "OFF"} (use `settings -mrt` to toggle)")
                print()
            elif args.command == "version":
                get_version()
            elif args.command == "coin":
                get_coin_data(args.ticker)
            else:
                parser.print_help()
        except SystemExit:
            # @TODO Handle argparse's SystemExit exception to avoid exiting the loop
            pass
        except Exception as e:
            print(f"An error occurred: {e}")


