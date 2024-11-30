A microservice made for my teammate for CS361-Software Engineering I

To begin, make sure node is installed, then run npm init in the home
directory. This should install all npm dependencies. To start the API,
you can use the command
  node .



Communication Contract (for CS361 Assignment 8)

A. Use a GET, POST, or DELETE request to interact with the stock watchlist
or to get price updates or summaries from the API. 
GET Endpoints:
'/stocks': List of stocks in the watchlist
ex.
import requests
response = requests.get("http://localhost:6465/stocks")

'/stocks/:symbol': Get price updates on stock with symbol 'symbol'
'/summary': Get a summary of all stocks on the watchlist

POST Endpoints:
'/stocks/:symbol': Add a stock to the watchlist with symbol 'symbol'
'/clearall': Clear the watchlist

DELETE Endpoint:
'/stocks/:symbol": Delete stock with symbol 'symbol' from the watchlist

B. When receiving data with the 'requests' module in python, a JSON will
be in the 'content' field of the response.

ex. 
import requests
response = requests.get("http://localhost:6465/summary")
print(response.content)
#This will print:

{
"status":200,
"message":"Success",
"stocks":[{
  "symbol":"aapl",
  "low":"226.6600",
  "high":"230.1600",
  "volume":"36211774",
  "change":"0.2600",
  "change percent":"0.1140%"
  },{
  "symbol":"ibm",
  "low":"206.1900",
  "high":"210.3300",
  "volume":"2860746",
  "change":"2.1600",
  "change percent":"1.0380%"
  }]
}

![uml](https://github.com/user-attachments/assets/29b209ac-df55-4928-b4f5-948760dcf0aa)
