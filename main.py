import streamlit  as st
st.title("Welcome to my app")
st.write("hello")
st.header("header")
st.subheader("Sub header")
st.markdown("<h1>Heading-2</h1>",unsafe_allow_html=True)
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXdXC2iQ5iJPCEhIHQKgY3_2VxHAMo8QGj5A&s", caption="A kid playing")
# st.audio("audio.mp3")
# st.video("video.mp4")
st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)