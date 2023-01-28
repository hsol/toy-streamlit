import streamlit as st
st.title("God damn wow")
if st.button("click button"):
    for test in range(3):
      st.write("Data Loading..")
checkbox_btn = st.checkbox('Checktbox Button')
if checkbox_btn:
    st.write("훌륭한데요")