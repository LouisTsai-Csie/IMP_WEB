import streamlit as st
from utils import lib
from utils import config
import random
import time

def calculation():
    
    st.header("Calculation Demo")

    getUserDataButton = st.button("Get User Data")
    if getUserDataButton: 
        st.info("Get User Data Successfully")
        st.subheader("GPT Encrypted Data")
        st.write(lib.handler.encrypted_number_list[0])

        st.subheader("GOT Encrypted Data")
        st.write(lib.handler.encrypted_number_list[1])

        expander = st.expander('System Workflow')
        colA, colB = expander.columns(2)

        colA.subheader("GPT Shares")
        GPTShareList = random.sample(range(config.N), config.T)
        GPTDict = {}
        for i in range(len(GPTShareList)):
            GPTDict[str(GPTShareList[i])] = lib.handler.share_list[0][GPTShareList[i]]
        colA.json(GPTDict)

        colB.subheader("GOT Shares")
        GOTShareList = random.sample(range(config.N), config.T)
        GOTDict = {}
        for i in range(len(GOTShareList)):
            GOTDict[str(GOTShareList[i])] = lib.handler.share_list[1][GOTShareList[i]]
        colB.json(GOTDict)

    
    DoOperation = st.button("Operation")

    if DoOperation:

        st.success("Calculation Success")

        item = lib.handler.cal()

        enc = item[0]

        dec = item[1]

        st.subheader("Result calculated from the institution")
        for key, val in enc.items():
            st.subheader(key)
            st.write(val)
        
        st.subheader("Result decrypted from the system")
        for key, val in dec.items():
            st.subheader(key)
            st.write(val)

if __name__=="__main__":
    calculation()