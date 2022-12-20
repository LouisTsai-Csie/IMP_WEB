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
    
    DoOperation = st.button("Operation")

    if DoOperation:

        bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.1)
        bar.progress(percent_complete + 1)

        st.success("Calculation Success")
        
        st.subheader("GPT Shares")
        GPTShareList = random.sample(range(config.N), config.T)
        GPTDict = {}
        for i in range(len(GPTShareList)):
            GPTDict[str(GPTShareList[i])] = lib.handler.share_list[0][GPTShareList[i]]
        st.json(GPTDict)

        st.subheader("GOT Shares")
        GOTShareList = random.sample(range(config.N), config.T)
        GOTDict = {}
        for i in range(len(GOTShareList)):
            GOTDict[str(GOTShareList[i])] = lib.handler.share_list[1][GOTShareList[i]]
        st.json(GOTDict)
        
        st.subheader("GPT Encrypted Data")
        st.write(lib.handler.encrypted_number_list[0])

        st.subheader("GOT Encrypted Data")
        st.write(lib.handler.encrypted_number_list[1])

        st.subheader("Calculation")
        cal = lib.handler.cal()

        for key, val in cal.items():
            st.subheader(key)
            st.write(val)
        
if __name__=="__main__":
    calculation()