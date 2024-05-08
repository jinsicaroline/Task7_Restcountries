import requests

def display_euro_countries():
    url = "https://restcountries.com/v3.1/all"

    try:
        response = requests.get(url)
        data = response.json()

        for country_data in data:
            country_name = country_data.get("name", {}).get("common")
            currency_data = country_data.get("currencies", {})
            if currency_data:
                for currency_code, currency_info in currency_data.items():
                    if "euro" in currency_info.get("name", "").lower():
                        print(f"Country: {country_name}")
                        print(f"Currency: {currency_info.get('name')}")
                        print(f"Currency Symbol: {currency_info.get('symbol')}")
                        print("-------------------------")
                        break  # Break out of inner loop once Euro currency is found

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


