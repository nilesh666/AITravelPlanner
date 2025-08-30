# AI Travel Planner 🌍✈️

An **AI-powered travel planning application** built with **Groq API** and **LangChain**, featuring a simple frontend in **Streamlit**.

## 🚀 Features
- AI-driven travel planning with **Groq API** + **LangChain**
- **Streamlit**-based frontend for easy interaction
- Production-grade deployment with **logging & monitoring**

## 🛠️ Deployment Architecture
- Uses **ELK Stack** for log management:
  - **Filebeat** → Collects logs from each pod  
  - **Logstash** → Cleans and processes logs  
  - **Elasticsearch** → Stores structured logs  
  - **Kibana** → Visualizes and monitors processed logs  

- Deployed on a **GCP VM instance** using:
  - **kubectl** → Command-line tool to interact with Kubernetes cluster  
  - **Minikube** → Local Kubernetes cluster for development & deployment  
