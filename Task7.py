import requests

class URLReader:
    def __init__(self, url):
        self.url = url

    def read_url(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.text
            else:
                return f"Error: Unable to fetch URL. Status code: {response.status_code}"
        except Exception as e:
            return f"Error: {str(e)}"

# Example usage:
url = input("https://restcountries.com/v3.1/all")
reader = URLReader(url)
content = reader.read_url()
print(content)