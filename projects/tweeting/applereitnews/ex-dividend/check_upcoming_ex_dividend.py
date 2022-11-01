import yfinance as yf
from datetime import datetime, timedelta

def checkForUpcomingExDividend():
  exDividendEpoch = yf.Ticker("APLE").info['exDividendDate']
  lastDayToOwn = datetime.fromtimestamp(exDividendEpoch).strftime('%Y-%m-%d')
  today = datetime.today()
  
  if lastDayToOwn == (today+timedelta(days=1)).strftime('%Y-%m-%d'):
    text = "Tomorrow is Apple REIT's Ex-Dividend Date.\nWhoever owns APLE stock at the end of today will receive the next dividend."
  else:
    text = False

  return text
