import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 加载数据
st.title('Califonia Housing Data (1990) by Linxin Feng')
df = pd.read_csv('housing.csv')

# 滑动条筛选房价
price_filter = st.slider('Minimal Median House Price:', 0, 500001, 200000)  # 修正价格范围

# 侧边栏多选过滤位置
location_filter = st.sidebar.multiselect(
     'Choose The Location Type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# 收入水平单选按钮
income_level = st.sidebar.radio(
    "Select income level:", ['Low (<2.5)', 'Medium(>2.5 & <4.5)', 'High(>4.5)']
)

# 根据收入水平过滤
if income_level == 'Low (<2.5)':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium(>2.5 & <4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]

# 价格过滤
filtered_df = filtered_df[filtered_df['median_house_value'] >= price_filter]

# 位置过滤
filtered_df = filtered_df[filtered_df.ocean_proximity.isin(location_filter)]

# 1. 显示地图 (确保有 latitude 和 longitude 列)
st.map(filtered_df[['latitude', 'longitude']])

# 2. 显示直方图
st.subheader('Median House Value')

# 绘制直方图
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(filtered_df['median_house_value'], bins=30)
ax.set_title('Histogram of Median House Value', fontsize=16)
ax.set_xlabel('Median House Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# 在 Streamlit 中显示直方图
st.pyplot(fig)
