# Notes

## What are APIs

- An Application Programming Interface (API) is a set of commands, functions, protocols and objects that we can use to create software or interact with external systems

> The API is an interface between our program and an external system, we use the rules that the API prescribed to make a request to the external system for some piece of data (the request should align with the api requirements), then if the request is successful the external system will respond to that request with data

## API Endpoint

- The Uniform Resource Locator (url) location of data

## API Request

- Message sent to the API in order to interact with the extenal system

## How to make a request

```python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) # <Response [200]>

"""To get the actual json data"""
data = response.json() # {<data>}
print(data)
```

### Response codes

- Response codes tell us if our requests succeeded or failed

## API Parameters

- A way that allows us to give input (piece of data) when making an api request so that we can get different outcomes (different data)

```python
import requests

# No required parameters provided
response = requests.get("https://api.sunrise-sunset.org/json") # Bad request

parameters = {"lat": -26.204103, "lng": 28.047304} # Johannesburg
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
```

## Request Sample

- This is how we format the parameters in the url string

> Sample string: https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400

|              Endpoint               | Connector | Param Name | equal |   Value    | Tag More Params |
| :---------------------------------: | :-------: | :--------: | :---: | :--------: | :-------------: |
| https://api.sunrise-sunset.org/json |     ?     |    lat     |   =   | 36.7201600 |        &        |
