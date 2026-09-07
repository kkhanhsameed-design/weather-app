import streamlit as st
import requests
API="bf993998029ffe5ecdf7514807f35130"

def get_weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
    response=requests.get(url)
    if response.status_code==200:
        return response.json()
    return None


st.set_page_config(page_title=" Weather APP",
                   page_icon="🌥️",
                   layout="wide")

st.title("**🌥️ Weather Forecast**")
st.header("**For the detail of the weather**")

city=st.text_input("Enter your city:")
if st.button("🔍 SEARCH"):
        
    if city.strip()=="":
        st.write("PLEASE ENETER A CITY")
    else:
        with st.spinner("Loading Data..."):
            data=get_weather(city)
        if data is None:
            st.write("city not found")
        else:
            col1,col2=st.columns([1,4])
            with col1:
               icon_code = data['weather'][0]['icon']
               st.image(f"https://openweathermap.org/img/wn/{icon_code}@2x.png")

            with col2:
                st.write(f"{data["name"]},/n{data['sys']['country']}")
                st.metric("🌡️temperature",f"{data['main']['temp']}")
                st.metric("loal time",f"{data['timezone']}")
                st.write("**condition**",f"{data['weather'][0]['description'].title()}**")
            st.divider()
            st.subheader("for more detail")
            cl1,cl2,cl3,cl4=st.columns(4)
            cl1.metric("💦humidity",f"{data['main']['humidity']}")
            cl2.metric("🌞 feel like",f"{data['main']['feels_like']}")
            cl3.metric("wind speed",f"{data['wind']['speed']}K/H")
            cl4.metric("cloud",f"{data['clouds']['all']}")
            st.divider()

