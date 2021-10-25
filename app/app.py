import streamlit as st
import pandas as pd
import requests
from settings import API_URL

spectra = st.file_uploader("upload file", type={"csv", "txt"})
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
    st.write(spectra_df)

pressed = st.button('Get Short Link')
if pressed:
    if spectra is not None:
        data = spectra_df.to_dict(orient='list')
        r = requests.post(API_URL, json=data)
        st.write(r.json())
    else:
        st.write('Please upload the data file')