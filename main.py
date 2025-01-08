import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Day")

town = st.text_input("Place", key="town", value="Kyiv", placeholder="Write your city...")

st.slider("Forecast Days", min_value=1, max_value=5, key="day", help="Select the number of forecasted days")

option = st.selectbox("Category", options=("Temperature", "Sky"), key="category")

if st.session_state['day'] == 1:
    st.header(f"Temperature for the next {st.session_state['day']} day in {town}")
else:
    st.header(f"Temperature for the next {st.session_state['day']} days in {town}")

try:
    weather_data, date = get_data(place=town, forecast_days=st.session_state['day'], option=option)

    if option == "Temperature":
        figure = px.line(x=date, y=weather_data, labels={"x": "Date", "y": "Temperature ℃"})
        st.plotly_chart(figure)
    elif option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/clouds.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [images[condition] for condition in weather_data]
        st.image(sky_conditions, caption=date, width=115)
    else:
        st.warning("What?" ,icon="⚠️")
except KeyError:
    st.warning("That place does not exist!", icon="⚠️")