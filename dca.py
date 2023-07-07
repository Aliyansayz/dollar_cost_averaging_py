import yfinance as yf


ada = yf.download( tickers="ADA-USD" , interval= '1D')[['Close']]
date_start= '2020-9-9'  
date_end= '2021-9-9'

# using date filter
df = ada.loc[date_start:date_end,:]
df


# daily invesment
investment = 5.0


z = [investment] * len(df) 
total_investment = [ z[i] + sum(z[:i]) for i, val in enumerate(z)  ]


price = df['Close'].tolist()

# Measuring price change

change = (np.diff(price) / price[:-1])
change = np.append(change, 0.0)
df['Change'] = change

df['Investment'] = total_investment

total_balance = [0.0] * len(total_investment)
total_balance[0] = total_investment[0] + ( change[0] * total_investment[0] )

for i in range(1 , len(total_investment)):
 
    new_balance = total_balance[i-1] + 5 # adding 5$ daily to our previous balance
    total_balance[i] =   new_balance + ( new_balance * change[i] )
 


