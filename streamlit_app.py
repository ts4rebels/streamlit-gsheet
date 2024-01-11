import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

st.title('Latest Updates')

for row in df.itertuples():
    st.write(f"**{row.filename}** was uploaded on {row.date}")
