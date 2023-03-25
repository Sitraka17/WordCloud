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

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create a word cloud from a string of text
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
wordcloud = WordCloud().generate(text)

# Display the word cloud using Matplotlib
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

