import streamlit as st

dict = {"brand 🚗": ["Ford", "KIA", "Toyota", "Tesla"],
        "model 🚙": ["Mustang", "Optima", "Corolla", "Model 3"],
        "year 📆": [1964, 2007, 2022, 2021],
        "color 🌈": ["Black ⚫", "Red 🔴", "White ⚪", "Red 🔴"],
        "emoji 🚀🚀": ["👨🏻‍🚀", "👩🏻‍🚀", "👩🏻‍🚒🚀", "👨🏻‍🚒"]}
st.dataframe(dict)
