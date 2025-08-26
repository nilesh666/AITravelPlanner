from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config.config import GROQ_API

llm = ChatGroq(
    groq_api_key = GROQ_API,
    model = "llama-3.3-70b-versatile",
    temperature = 0.5,

)

prompt = ChatPromptTemplate([
    ("system", "You are a travel assistant. The user will provide a {city} and {interests} they are interested in visiting. Based on these inputs, generate a clear, bulleted itinerary for a one-day trip. Arrange the places in an order that makes sense geographically and logistically (minimizing travel time). Add short notes (1–2 lines) about each stop, including what to expect or why it’s special. Keep the response concise and easy to follow."),
    ("human", "Create a itineary for my day trip")
])

def generate(city, interests: list[str])->str:
    response = llm.invoke(
        prompt.format_messages(city = city, interests = ", ".join(interests))
    )
    return response.content