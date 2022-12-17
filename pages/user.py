import streamlit as st
from utils import lib

def user():
    
    handler = lib.Tool()

    st.header('User Input Interface')
    userId   = st.text_input("Please enter patient's id")
    userGPT  = st.text_input("Please enter patient's GPT")
    userGOT  = st.text_input("Please enter patient's GOT")
    checkInput    = st.button("Confirm")
    if checkInput:
        if userId and userGPT and userGOT:
            data_pack = {
                "id": userId,
                "GPT": userGPT,
                "GOT": userGOT,
            }
        else: st.info("Incorrect Argument Number")
        check = False

    userId = st.text_input("Please enter patient's id to fetch data")
    check = st.button("Confirm ")
    if check: st.snow()
    return

if __name__=='__main__':
    user()