import streamlit as st
import numpy as np
import pandas as pd

st.title("streamlit 超入門")

st.write("DataFrame")

# df = pd.DataFrame({
# "1列目":[1, 2, 3, 4],  
#     "2列目":[10, 20, 30, 40]
# })

#st.dataframe(df.style.highlight_max(axis=0), width=1000, height=300)

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

# df = pd.DataFrame(
#    np.random.rand(20,3) ,
#    columns=["a", "b", "C"]
# )
# # st.line_chart(df)
# st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=["lat","lon"]
)
st.map(df)