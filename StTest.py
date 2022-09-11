import streamlit as st
import numpy as np
import pandas as pd
import PIL.Image as Im

st.title("Streamlit 超入門")

st.write("DataFrame")


"""# 1.表を表示する"""

arr1=np.array([[12, 2, 31, 4], [10, 2, 3, 40]])
df = pd.DataFrame(data=arr1,columns=['1列目','2列目','3列目','4列目'])

#st.writeで表を表示
"""## 1-1.st.writeで表示"""
st.write(df)

#st.datafameで表を表示（幅、高さを変更可）
"""## 1-2.st.dataframeで表示"""
st.dataframe(df)
"""## 1-3.st.dataframeで幅、高さを指定して表示"""

st.dataframe(df, width=200, height=200)
#表の中で最大値をハイライトする場合(列指定の場合axis=0、行指定の場合axis=1)
"""## 1-4.st.dataframeで列で一番大きい数字をハイライトして表示"""
st.dataframe(df.style.highlight_max(axis=0), width=400, height=200)
"""## 1-5.st.dataframeで行で一番大きい数字をハイライトして表示"""
st.dataframe(df.style.highlight_max(axis=1), width=400, height=200)

#静的な表を表示
"""## 1-6.st.tableで表示"""
st.table(df.style.highlight_max(axis=1))

#参考
st.write("https://docs.streamlit.io/library/api-reference/data/st.dataframe")


"""# 2.テキストを書く"""

"""## 2-1.マークダウン"""
"""
# 章
## 節
### 項
"""

"""## 2-2.プログラム"""
"""
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

"""# 3.グラフを書く"""
"""## 3-1.折れ線グラフ"""
df=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)
st.line_chart(df)

"""## 3-2.エリアチャート"""
st.area_chart(df)

"""## 3-3.棒グラフ"""
st.bar_chart(df)

"""## 3-4.マップ"""
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
    columns=["lat", "lon"]
)
st.map(df)

"""# 4.画像"""
st.write('Display Image')

img = Im.open('C:\python\VScode\Testimage.jpg')
st.image(img, caption='よいよい', use_column_width=True)