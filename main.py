import quandl
import matplotlib

# set SONY brand
brand = "TSE/6758"
with open("apikey.txt", "r") as f:
    quandl.ApiConfig.api_key = f.read()
quandl_data = quandl.get(dataset=brand, returns='pandas')
quandl_data.to_json('got_data.json')
