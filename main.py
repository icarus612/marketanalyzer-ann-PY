from controllers.alphavantage import Alphavantage
from controllers.robinhood import Robinhood
from controllers.base_trade_bot_RH import TradeBot
from os import environ as env 

Alpha = Alphavantage('WA71OD0SUMQLQV08')
RH_Bot = Robinhood(env['RH_UNAME'], env['RH_PASSWORD'])
Alpha.get_daily_ts()

print(RH_Bot.account_data)


