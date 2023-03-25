import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Title
st.title("Word Cloud Generator")

# Text input
text = st.text_input("Enter some text")

# Generate word cloud
wordcloud = WordCloud().generate(text)

# Display word cloud using Matplotlib
if text:
    st.set_option('deprecation.showPyplotGlobalUse', False) # to avoid warning message
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()

