import streamlit as st

def home():
    st.header('System Design')
    st.subheader('Secret Splitting')
    st.text('Store data in distributed system')
    st.subheader('Homomorphic Encryption')
    st.text('Encrypted Data can still do calculation')

if __name__=='__main__':
    home()