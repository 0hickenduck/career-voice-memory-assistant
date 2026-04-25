import streamlit as st

# Page title
st.title("Career Voice Memory Assistant")

# A text box for user input
text = st.text_area("今日の就活・学習内容を入力してください")

# A button. The code inside runs when the button is clicked.
if st.button("保存"):
    st.write("入力内容:")
    st.write(text)
    st.success("保存しました")