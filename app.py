import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **The EDA App**

---
''')

# Upload CSV data
with st.sidebar.header('Upload CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload input file in CSV", type=["csv"])
    st.sidebar.markdown("""

    [Try Sample CSV](https://raw.githubusercontent.com/kashifm777/EDA/main/concrete.csv)
""")

# Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input as DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV to be uploaded.')
    if st.button('Press to use Sample Dataset'):
        # Sample data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)


st.header('some text')
hide_st_style = """
    <style>
        MainMenu {visibility: hiden;}
        footer {visibility: hidden; }
        
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)