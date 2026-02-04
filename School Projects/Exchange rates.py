import requests

# Where the iput is used
currency1=input(" What currency are you changing from? ").upper()
currency2=input(" What currency are you changing to? ").upper()
moneyinput=float(input("how much money are you going to convert "))

# Where currency1 is the base currency you want to use
url = "https://open.er-api.com/v6/latest/"+currency1

# Making our request
response = requests.get(url)
data = response.json()

#where we get the exchange ratesd
cex=float(data['rates'][c2])
#this is where the calcualtaions are done then printed out
mo=mi*cex
print(mo)

