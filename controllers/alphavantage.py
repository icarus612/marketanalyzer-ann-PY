
import requests

class Data_Integrator:
  def __init__(self, api_key, function='TIME_SERIES_DAILY', output_size='full', interval=5, default_symbol="GOOG"):
    self.base_api = 'https://www.alphavantage.co/query'
    self.api_key = api_key
    self.function = function
    self.output_size = output_size
    self.interval = interval
    self.default_symbol = default_symbol
    
  def update_params(self, new_params):
    current_params = vars(self)
    for key in current_params.keys():
      if key in new_params.keys():
        current_params[key] = new_params[key] 
      
  def query_data(self, symbol=None):
    params = {
      "symbol": symbol or default_symbol,
      "function": self.function,
      "interval": str(self.interval) + "min",
      "apikey": self.apikey,
      "outputsize": self.output_size
    }
    requests.get(self.base_api, params=params)
    if response.status_code == 200:
      return response.data()
    else:
      print("ERROR: ", response.status_code)
      
      