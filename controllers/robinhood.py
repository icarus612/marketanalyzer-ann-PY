import requests

class Robinhood_Controller:
  def __init__(self,  username, password, interval=5, current_symbol="GOOG"):
    self.login_url = 'https://api.robinhood.com/oauth2/token/'
    self.account_url = 'https://api.robinhood.com/accounts/'
    self.username = username
    self.password = password
    self.current_symbol = current_symbol
    self.interval = interval * 60
    self.account_data = {}
    self.access_token = False
    self.login()
    
  def set_interval(self, i):
    self.interval = i * 60
  
  def login(self):
    payload = {
      'grant_type': 'password',
      'scope': 'internal',
      'client_id': 'your_client_id',
      'username': self.username,
      'password': self.password
    }
    
    response = requests.post(self.login_url, data=payload)
    data = response.json()
    self.access_token = data['access_token']

  def get_account_data(self):
    headers = {
        'Authorization': f'Bearer {self.access_token}'
    }
        
    self.account_data = requests.get(self.account_url, headers=headers).json()