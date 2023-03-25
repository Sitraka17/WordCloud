import streamlit as st

# Title
st.title("My Streamlit App")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.write("This is some text.")

# Markdown
st.markdown("This is some **bold** text.")

# Dataframe
import pandas as pd
df = pd.DataFrame({
  'column 1': [1, 2, 3, 4],
  'column 2': ['a', 'b', 'c', 'd']
})
st.write(df)

# Plot
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
st.pyplot(plt)

