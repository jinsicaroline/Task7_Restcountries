import requests

def get_breweries_with_websites_by_state(states):
    url = "https://api.openbrewerydb.org/breweries"

    try:
        breweries_with_websites_by_state = {}
        for state in states:
            params = {"by_state": state}
            response = requests.get(url, params=params)
            data = response.json()

            breweries_with_websites = []
            for brewery in data:
                if "website_url" in brewery and brewery["website_url"]:
                    breweries_with_websites.append(brewery["name"])

            breweries_with_websites_by_state[state] = {
                "count": len(breweries_with_websites),
                "breweries": breweries_with_websites
            }

        return breweries_with_websites_by_state

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

# List of states
states_of_interest = ["Alaska", "Maine", "New York"]

# Get breweries with websites by state
breweries_with_websites_by_state = get_breweries_with_websites_by_state(states_of_interest)

# Print the count and list of breweries with websites for each state
for state, data in breweries_with_websites_by_state.items():
    print(f"Breweries with websites in {state}:")
    print(f"Count: {data['count']}")
    print("List:")
    for brewery in data["breweries"]:
        print(f"- {brewery}")
    print("-----------------------------")
