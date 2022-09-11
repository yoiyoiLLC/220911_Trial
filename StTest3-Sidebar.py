import streamlit as st
import numpy as np
import pandas as pd
import PIL.Image as Im

st.title("Streamlit 超入門")

st.write("DataFrame")


"""# Sidebar"""
if st.checkbox('Show Image'):
    img = Im.open('C:\python\VScode\Testimage.jpg')
    st.image(img, caption='よいよい', use_column_width=True)

option = st.sidebar.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたが好きな数字は', option, 'です'

text = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味 :', text

condition = st.sidebar.slider('あなたの今の調子は', 0, 100, 50)
'あなたの調子 :', condition
