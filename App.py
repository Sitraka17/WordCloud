# App

import streamlit as st
import requests

API_KEY = "your_api_key"
CITY = "Paris"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)


