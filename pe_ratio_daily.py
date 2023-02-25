import requests
import pandas as pd

# Define the URL for the API endpoint
url = "https://www.twse.com.tw/exchangeReport/BWIBBU_d"

# Define the parameters for the API request
params = {
    "response": "json",
    "date": "20230224",
    "selectType": "ALL",
}

# Send the API request and retrieve the data
response = requests.get(url, params=params)
data = response.json()

# Send the API request and retrieve the data
response = requests.get(url, params=params)
data = response.json()

# Extract the data into a Pandas DataFrame
columns = ["證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季"]
rows = []

try:
	for item in data["data"]:
		rows.append([item[0], item[1], item[2], item[3], item[4], item[5], item[6]])
except KeyError:
	print('Data does not exist on certain date.')

df = pd.DataFrame(rows, columns=columns)

# Output the DataFrame to a CSV file
df.to_csv("pe_ratios.csv", index=False, encoding="utf_8_sig")

