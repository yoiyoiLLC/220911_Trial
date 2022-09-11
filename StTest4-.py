import streamlit as st
import numpy as np
import pandas as pd
import PIL.Image as Im
import time

st.title("Streamlit 超入門")

st.write("プレグスバーの表示")
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(1,10):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'DONE!!!'
"""# st.columnsとst.expander"""

left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('いかいかまいか')

if st.checkbox('Show Image'):
    img = Im.open('C:\python\VScode\Testimage.jpg')
    st.image(img, caption='よいよい', use_column_width=True)
