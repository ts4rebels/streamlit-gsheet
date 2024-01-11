import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

for row in df[::-1].head(20).itertuples():
    st.write(f"**{row.filename}** was uploaded on *{row.date}*") if {row.previews} != nan st.markdown( - [{row.previews}](preview))
