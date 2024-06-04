import requests

def get_brewery_types_by_city(state):
    url = "https://api.openbrewerydb.org/breweries"

    try:
        params = {"by_state": state}
        response = requests.get(url, params=params)
        data = response.json()

        brewery_types_by_city = {}
        for brewery in data:
            city = brewery.get("city", "Unknown City")
            brewery_type = brewery.get("brewery_type", "Unknown Type")
            if city in brewery_types_by_city:
                if brewery_type not in brewery_types_by_city[city]:
                    brewery_types_by_city[city].append(brewery_type)
            else:
                brewery_types_by_city[city] = [brewery_type]

        return brewery_types_by_city

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

# List of states
states_of_interest = ["Alaska", "Maine", "New York"]

# Get brewery types by city for each state
for state in states_of_interest:
    print(f"Brewery types in {state}:")
    brewery_types_by_city = get_brewery_types_by_city(state)
    for city, types in brewery_types_by_city.items():
        print(f"{city}: {len(types)} types - {', '.join(types)}")
    print("-----------------------------")
