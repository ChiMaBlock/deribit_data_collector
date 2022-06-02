import deribit_data as dm
btc_data = dm.Options("BTC")


# Get realised historical volatility
df = btc_data.get_hist_vol(save_csv=False)
print(df.tail())



# Get all option prices and relevant statistics - this should take less than 30 seconds.

df_2 = btc_data.collect_data(save_csv=False)
print(df_2[['instrument_name', 'last_price', 'mark_iv', 'open_interest']].head())