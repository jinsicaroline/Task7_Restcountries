import requests

def get_breweries_in_states(states):
    url = "https://api.openbrewerydb.org/breweries"

    try:
        breweries = []
        for state in states:
            params = {"by_state": state}
            response = requests.get(url, params=params)
            data = response.json()
            breweries.extend(data)

        brewery_names = [brewery["name"] for brewery in breweries]
        return brewery_names

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

# List of states
states_of_interest = ["Alaska", "Maine", "New York"]

# Get brewery names in the specified states
brewery_names = get_breweries_in_states(states_of_interest)

# Print the brewery names
for name in brewery_names:
    print(name)
