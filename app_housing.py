import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('Califonia Housing Data (1990) by Linxin Feng')
df = pd.read_csv('housing.csv')


price_filter = st.slider('Minimal Median House Price:', 0, 50001, 20000)  # min, max, default


location_filter = st.sidebar.multiselect(
     'Choose The Location Type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

income_level = st.sidebar.radio(
    "Select income level:", ['Low (<2.5)', 'Medium(>2.5 & <4.5)', 'High(>4.5)']

)


if income_level == 'Low(<2.5)':
    fitered_df = df[df['median_income']<=2.5]
elif income_level == 'Medium(>2.5 & >4.5)':
    filtered_df = df[[df['median_income'] > 2.5] & [df['median_income'] < 4.5]]
else:
    filtered_df = df[df['median_income'] > 4.5]




df = df[df.median_income >= price_filter]

df = df[df.ocean_proximity.isin(location_filter)]


if income_level == 'Low(<2.5)':
    fitered_df = df[df['median_income']<=2.5]
elif income_level == 'Medium(>2.5 & >4.5)':
    filtered_df = df[[df['median_income'] > 2.5] & [df['median_income'] < 4.5]]
else:
    filtered_df = df[df['median_income'] > 4.5]





st.map(df)

st.subheader('Median House Value')

fig, ax = plt.subplots(figsize=(20,5))
ax.hist(filtered_df['median_house_value'], bins = 30)
ax.set_title('Histogram of Hedian House Value', fontsize=16)
ax.set_xlabell('Hedian House Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

st.pyplot(fig)