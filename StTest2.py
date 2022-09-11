import streamlit as st
import numpy as np
import pandas as pd
import PIL.Image as Im

st.title("Streamlit 超入門")

st.write("DataFrame")


"""# 1.インタラクティブなウィジェット"""
"""## 1-1.st.checkbox"""
if st.checkbox('Show Image'):
    img = Im.open('C:\python\VScode\Testimage.jpg')
    st.image(img, caption='よいよい', use_column_width=True)

"""## 1-2.st.selectbox"""
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたが好きな数字は', option, 'です'

"""## 1-3.st.text_input"""
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味 :', text

"""## 1-4.st.slider"""
condition = st.slider('あなたの今の調子は', 0, 100, 50)
'あなたの調子 :', condition
