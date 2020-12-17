import streamlit as st
import pandas as pd
import numpy as np

#import plotly.graph_objects as go
#from plotly import tools
#import plotly.offline as py
import plotly.express as px

st.title("How good are you at ABCDE?")

st.sidebar.title("Questionnaire")
A = st.sidebar.slider("How good are you at A?",1,5,3,step=1)
B = st.sidebar.slider("How good are you at B?",1,5,3,step=1)
C = st.sidebar.slider("How good are you at C?",1,5,3,step=1)
D = st.sidebar.slider("How good are you at D?",1,5,3,step=1)
E = st.sidebar.slider("How good are you at E?",1,5,3,step=1)

df = pd.DataFrame(dict(
    goodness=[A, B, C, D, E],
    topic=['A','B','C','D','E']))
fig = px.line_polar(df, r='goodness', theta='topic', line_close=True, range_r=[1,5])

st.plotly_chart(fig)
