import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout= "wide")

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())

list_of_states.insert(0, 'Overall India')

st.sidebar.title('India ka Data Viz')
selected_state = st.sidebar.selectbox('Select a state', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('plot Graph')

if plot:
    st.text('Size represent primary parameter')
    st.text('Color represent Secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size = primary, color = secondary,  zoom=4,
                                size_max= 35,
                                mapbox_style="carto-positron", width = 1200, height = 700, hover_name = 'District')
        st.plotly_chart(fig)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name= 'District')
        st.plotly_chart(fig)

