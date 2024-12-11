'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")

df = pd.read_csv('./cache/top_locations_map.csv')
st.title("Top Locations for Parking Tickets Within Syracuse")
st.caption('This Dashboard shows the parking tickets that were issued in the top locations with $1,000 or more in total aggregate violation amounts.')
locations_list = df['location'].unique()
location_choice = st.selectbox('Select a location', locations_list)

if location_choice:
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Total Tickets Issued', df[df['location'] == location_choice]['count'].sum())
        fig1, ax1 = plt.subplots()
        sns.barplot(data=df[df['location'] == location_choice], x = 'hourofday', y = 'count', hue = 'hourofday', estimator=sum, ax=ax1)
        ax1.set_title('Tickets Issued by Hour of Day')
        st.pyplot(fig1)
    with col2:
        st.metric('Total Amount', f"${df[df['location'] == location_choice]['amount_y'].sum()}")
        fig2, ax2 = plt.subplots()
        sns.barplot(data=df[df['location'] == location_choice], x = 'dayofweek', y = 'count', hue = 'dayofweek', estimator=sum, ax=ax2)
        ax2.set_title('Tickets Issued by Day of Week')
        st.pyplot(fig2)

    st.map(df[df['location'] == location_choice][['lat', 'lon']])
