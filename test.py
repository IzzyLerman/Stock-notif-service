#example python calling the stock notif API

import requests

API_URL = "http://localhost:6465/"


#Adding "AAPL" to the watchlist
response = requests.post(API_URL+'stocks/aapl',{})
print(response, response.content)
input()
#Get price update for AAPL
response = requests.get(API_URL+'stocks/aapl')
print(response, response.content)
input()
#Get price update for BNNA (failure)
response = requests.get(API_URL+'stocks/bnna')
print(response, response.content)
input()
#Add IBM to watchlist
response = requests.post(API_URL+'stocks/ibm',{})
print(response, response.content)
input()
#Get a summary of all coins
response = requests.get(API_URL+'summary')
print(response, response.content)

#clear the watchlist
requests.post(API_URL + 'clearall')