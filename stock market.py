# Import the necessary modules
import requests
import json

# Set the URL for the NASDAQ API and your API key
url = "https://api.nasdaq.com/api/quote/AAPL/info?assetclass=stocks"
api_key = "638e1eba2519c7.22543236"

# Set the headers for the request
headers = {
    "Authorization": "Bearer " + api_key
}

# Make a request to the API and get the response
response = requests.get(url, headers=headers)

# Parse the JSON data from the response
data = json.loads(response.text)

# Get the stock price from the data
stock_price = data["data"]["lastSalePrice"]

# Print the stock price
print("The current stock price for AAPL on the NASDAQ is: $" + str(stock_price))
