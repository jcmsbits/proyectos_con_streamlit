import yfinance as yf
import streamlit as st
import pandas as pd

# We can use Markdown on the text
st.write("""
    # Simple Stock Price App
         
    Shown are the **stock** closing ***price*** and volume of Google!
         
""")

# GOOGL for Google
# AAPL for Apple
# define the ticker symbol
# What action do we want
tickerSymbol = "GOOGL"

# get data on this ticker

tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker

tickerDf = tickerData.history(period= "1d", start = "2010-5-31", end = "2020-5-31")
# This Dataframe has the follow columns
# Open High     Low Close       Volume Dividends        Stock Splits

st.write(""""
         ## Closing Price
         """)
st.line_chart(tickerDf.Close)

st.write(""""
         ## Volume Price
         """)
st.line_chart(tickerDf.Volume)