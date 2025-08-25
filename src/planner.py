from langchain_core.messages import HumanMessage, AIMessage
from chains.travel_chain import generate
from utils.logger import logging
from utils.custom_exception import CustomException
import sys

class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city="" 
        self.interests = []
        self.plan=""
        logging.info("Initialized travel planning instance")

    def set_city(self, city):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logging.info("City set successfully")        
        except Exception as e:
            logging.error("Error in setting the city")
            raise CustomException(e, sys)
        
    def set_interests(self, intrst_str:str):
        try:
            self.interests = [i.strip() for i in intrst_str.split(",")] 
            self.messages.append(HumanMessage(content=intrst_str))
            logging.info("Initialized travel planning instance")
        except Exception as e:
            logging.error("Error in setting the interests")
            raise CustomException(e, sys)
    
    def generate_plan(self):
        try:
            logging.info("Generating the plan")
            plan=generate(self.city, self.interests)
            self.plan=plan
            self.messages.append(AIMessage(content=self.plan))
            logging.info("Itinerary generated successfully")
            return self.plan
        except Exception as e:
            logging.error("Error in generating the plan")
            raise CustomException(e, sys)
        

