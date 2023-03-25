# App

import streamlit as st
import requests

API_KEY = "your_api_key"
CITY = "Paris"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    st.write(f"Temperature: {temp}°C")
    st.write(f"Feels like: {feels_like}°C")
    st.write(f"Humidity: {humidity}%")
    st.write(f"Wind speed: {wind_speed} m/s")
    st.write(f"Description: {description}")
else:
    st.write("Error getting weather data")
    
