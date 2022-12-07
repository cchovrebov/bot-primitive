import pandas as pd

path = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=ETH&market=USD&interval=5min&apikey=demo&datatype=csv'

df = pd.read_csv(path)

df = df[::-1].reset_index()

df = df.drop(['index'], axis=1)

print(df)
