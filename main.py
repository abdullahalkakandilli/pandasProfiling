import requests
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import pandas_profiling

import pandas as pd

def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_icon="✂️", page_title="General Analytics")


c2, c3 = st.columns([6, 1])


with c2:
    c31, c32 = st.columns([12, 2])
    with c31:
        st.caption("")
        st.title("General Analytics")
    with c32:
        st.image(
            "images/logo.png",
            width=200,
        )

uploaded_file = st.file_uploader(
    " ",
    key="1",
    help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    uploaded_file.seek(0)
    table_ = df.to_dict()
    new_data = {}
    # loop through each key in the original dictionary
    for key in table_:
        # get the values from the inner dictionary and convert them to a list
        values = list(table_[key].values())
        # add the values to the new dictionary with the same key
        values = [str(value) if not isinstance(value, str) else value for value in values]
        new_data[key] = values


    pr = df.profile_report()
    st_profile_report(pr)

else:
    st.info(
        f"""
            👆 Upload a .csv file first. Sample to try: [biostats.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv)
            """
    )
    st.video('https://youtu.be/HgLyNo0UGXo')
    st.stop()
