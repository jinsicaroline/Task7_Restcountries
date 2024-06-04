import requests

def get_brewery_count_by_state(states):
    url = "https://api.openbrewerydb.org/breweries"

    try:
        brewery_counts = {}
        for state in states:
            params = {"by_state": state}
            response = requests.get(url, params=params)
            data = response.json()
            brewery_counts[state] = len(data)

        return brewery_counts

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

# List of states
states_of_interest = ["Alaska", "Maine", "New York"]

# Get brewery counts in the specified states
brewery_counts = get_brewery_count_by_state(states_of_interest)

# Print the brewery counts for each state
for state, count in brewery_counts.items():
    print(f"{state}: {count} breweries")
