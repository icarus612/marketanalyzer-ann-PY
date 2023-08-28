from controllers.alphavantage import Alphavantage
from controllers.robinhood import Robinhood

alpha = Alphavantage('WA71OD0SUMQLQV08')

alpha.get_daily_ts()
