import requests

def fetch_data(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "https://example.com/data"
    data = fetch_data(url)
    print(data)