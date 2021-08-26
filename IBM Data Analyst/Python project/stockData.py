import yfinance as yf
amd = yf.Ticker("AMD")
amd_info = amd.info
print(amd_info['country'])
print(amd_info['sector'])
print(amd.history(period="max"))
