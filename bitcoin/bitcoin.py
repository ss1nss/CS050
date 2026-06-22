import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

if len(sys.argv) > 1:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        usd_amount = data["bpi"]["USD"]["rate_float"] * float(sys.argv[1])
        print(f"${usd_amount:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    except requests.RequestException:
        sys.exit()
