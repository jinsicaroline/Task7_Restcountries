import requests

def display_countries_info():
    url = "https://restcountries.com/v3.1/all"

    try:
        response = requests.get(url)
        data = response.json()

        for country_data in data:
            country_name = country_data.get("name", {}).get("common")
            currency_data = country_data.get("currencies", {})
            if currency_data:
                currency_name = currency_data.get(next(iter(currency_data)), {}).get("name")
                currency_symbol = currency_data.get(next(iter(currency_data)), {}).get("symbol")
                print(f"Country: {country_name}")
                print(f"Currency: {currency_name}")
                print(f"Currency Symbol: {currency_symbol}")
                print("-------------------------")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


