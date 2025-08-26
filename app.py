import streamlit as st
from src.planner import TravelPlanner
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI travel planner")
st.title("Generate plan")
st.write("Simple travel planner")

with st.form("planner_form"):
    city = st.text_input("Enter your city name")
    interests = st.text_input("Enter places to visit(comma-seperated)")
    submit = st.form_submit_button("Generate plan")

    if submit:
        if city and interests:
            plan = TravelPlanner()
            plan.set_city(city)
            plan.set_interests(interests)
            text_plan = plan.generate_plan()
            st.subheader("The plan generated as follows")
            st.write(text_plan)
        else:
            st.write("Please fill city or interests to generate")
        
