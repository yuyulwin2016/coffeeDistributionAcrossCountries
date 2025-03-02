import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(page_title= "Coffee Distribution across Countries", page_icon=":coffee:",layout="wide")
df = pd.read_csv('psd_coffee.csv')
st.sidebar.header('Filter')
country = st.sidebar.multiselect(
    "Select Country:",
    options = df['Country'].unique(),
    default = df['Country'].unique()[:10]
)
year = st.sidebar.multiselect(
    "Select Year:",
    options = df['Year'].unique(),
    default = df['Year'].unique()[:10]
)
st.title(":coffee: Coffee Distribution across Countries")
totalDistribution = df['Total Distribution'].sum()
totalSupply = df['Total Supply'].sum()
a, b = st.columns(2)
c, d = st.columns(2)
f, g = st.columns(2)

with a:
    st.subheader('Total Distribution')
    st.subheader(f"Total Bags: {totalDistribution}")
with b:
    st.subheader('Total Supply')
    st.subheader(f"Total Bags: {totalSupply}")

df_select = df.query("Country == @country and Year == @year")

distribution_by_country = df_select.groupby('Country')['Total Distribution'].sum()
fig_by_country = px.bar(
    distribution_by_country,
    x = distribution_by_country.values,
    y = distribution_by_country.index,
    title = "Distribution by Country"
)
c.plotly_chart(fig_by_country, use_container_width = True)

fig_by_year = px.pie(
    df_select,
    values = 'Total Distribution',
    names = 'Year',
    title = 'Distribution by Year'
)
d.plotly_chart(fig_by_year, use_container_width = True)

production_by_country = df_select.groupby('Country')['Production'].sum()
fig_by_country = px.line(
    distribution_by_country,
    x = production_by_country.values,
    y = production_by_country.index,
    title = "Production by Country"
)
f.plotly_chart(fig_by_country, use_container_width = True)

fig_by_export_import = px.scatter(
    df_select,
    x = 'Exports',
    y = 'Imports',
    title = "Export and Import"
)
g.plotly_chart(fig_by_export_import, use_container_width = True)