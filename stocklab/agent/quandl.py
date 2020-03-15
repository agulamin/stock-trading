import quandl
quandl.ApiConfig.api_key = 'P7FWKS8z29tH6ib_JmDm'
data = quandl.get('BCHARTS/BITFLYERUSD', start_date='2020-02-28', end_date='2020-02-28')

print(data)
# https://www.quandl.com/data/BCHARTS-Bitcoin-Charts-Exchange-Rate-Data/usage/quickstart/python