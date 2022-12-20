import streamlit as st
from utils import lib
from utils import config


def user():

    st.header('Upload Interface')
    userId   = st.text_input("Please enter patient's id")
    userGPT  = st.text_input("Please enter patient's GPT")
    userGOT  = st.text_input("Please enter patient's GOT")
    checkInput    = st.button("Confirm")
    if checkInput:
        if userId and userGPT and userGOT:
            data_pack = {
                "id": userId,
                "GPT": int(userGPT),
                "GOT": int(userGOT),
            }
            lib.handler.uploadData(data_pack)
        else: st.info("Incorrect Argument Number")
        check = False

        expander = st.expander("See the workflow")
        expander.subheader('Original Data')
        colA, colB, colC = expander.columns(3)
        colA.metric("User ID", userId)
        colB.metric("User GPT", userGPT)
        colC.metric("User GOT", userGOT)
        expander.subheader("Encrypted Data")
        expander.write(f"there are total {config.N} shares with threshold {config.T}")

        expander.write("GPT Encrypted Number")
        expander.write(lib.handler.encrypted_number_list[0])
        GPTDict = {}
        for i in range(len(lib.handler.share_list[0])):
            GPTDict[str(i+1)] = lib.handler.share_list[0][i]
        expander.write('GPT Shares')
        expander.json(GPTDict)

        expander.write("GOT Encrypted Number")
        expander.write(lib.handler.encrypted_number_list[1])
        GOTDict = {}
        for i in range(len(lib.handler.share_list[1])):
            GOTDict[str(i+1)] = lib.handler.share_list[1][i]
        expander.write("GOT Encrypted Data")
        expander.json(GOTDict)
    return

if __name__=='__main__':
    user()