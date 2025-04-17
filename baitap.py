import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.write("Thông tin nhóm:")
st.write("- Trần Minh Thanh : 2221050799")
st.write("- Phạm Thị Phượng : 2221050063")
st.write("- Nguyễn Trung Quốc : 2221050438")


# st.write("Hello ,let's learn how to build a streamlit app")

# 2.1 Hiển thị văn bản với Streamlit
st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

#2.2 hiển thị hình ảnh với Streamlit

st.subheader("Image:")
st.image("anh-nen-totoro.jpg")

st.subheader("Audio: ")
st.audio("https://vn.pikbest.com/sound-effects/cheerful-and-lively-guitar-short-video-with-beautiful-background-sound-effects_1150566.html")

st.subheader("Video: ")
st.video("https://www.youtube.com/watch?v=opcalZXrg3s")

# 2.3 Widgets

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)


st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

#2.4 Thanh bên(sidebar)

st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("click")
st.sidebar.radio("Pick",["Male","Female"])

# 2.5 Trực quan

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
)
st.line_chart(df)

df_2 = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
)
st.bar_chart(df_2) 

# 3. Project
 #read in the file
import pandas as pd

movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")
movies_data.info()
movies_data.dropna()

st.write("""Average Movie Budget, Grouped by Genre""")
avg_budget = movies_data.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

fig = plt.figure(figsize = (19, 10))
plt.bar(genre, avg_bud, color = 'maroon')
plt.xlabel('genre')
plt.ylabel('budget')
plt.title('Matplotlib Bar Chart Showing the Average \
Budget of Movies in Each Genre')

st.pyplot(fig)

# 4 Web 
