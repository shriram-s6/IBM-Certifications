import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/' \
      'IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')
title = soup.title.text
# print(title)
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    amazon_data = amazon_data.append(
        {"Date": date, "Open": Open, "High": high, "Low": low, "Close": close, "Adj Close": adj_close,
         "Volume": volume}, ignore_index=True)
# print(amazon_data.head(5))
column = amazon_data.columns.values
# print(column)
print(amazon_data.iloc[-1:, 1])
