# =========================
# Imports
# =========================

import pandas    as pd
import numpy     as np
import streamlit as st
import yfinance as yf
import folium

import plotly.express       as px
import plotly.graph_objects as go

from PIL              import Image
from streamlit_folium import folium_static
from streamlit_folium import st_folium
from datetime         import datetime

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title = "Home",
    page_icon = "🍝",
    layout='wide'
)

# =================================
# ETL
# =================================

start_date = "2017-01-01"
end_data = datetime.now().strftime('%Y-%m-%d')

tickers = ['VALE3.SA']

df = yf.download(tickers, start=start_date, end=end_data, progress=False)

def get_data(start_date, end_date, ticker):
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    df = df.reset_index()

    return df

# =================================
# Sidebar
# =================================

st.sidebar.markdown('# Stocks Dashboard')
st.sidebar.markdown('## See the prices of your favorite stocks')

st.sidebar.markdown("""---""")
st.sidebar.markdown('## Filters')
ticker_option = st.sidebar.multiselect(
    'Select stocks',
    ['VALE3.SA', 'PETR4.SA'],
    default = ['VALE3.SA']
)

df = get_data(start_date, end_data, ticker_option)

st.sidebar.markdown("""---""")
st.sidebar.markdown("Made by Gabriel Alves")

# =================================
# Main page
# =================================

st.write('# Stocks dashboard')

st.markdown(""" 
### Select your favorite stocks on the sidebar and follow the prices on the charts above
""")

df_aux = df.reset_index()
with st.container():
    fig = px.line(df_aux, x="Date", y="Adj Close", title=ticker_option[0])
    st.plotly_chart(fig, use_container_width=True)