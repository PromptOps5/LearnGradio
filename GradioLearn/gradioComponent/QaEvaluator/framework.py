"""This is the framework to interact with by the user"""
from random import choices
from openai import OpenAI
from dotenv import load_dotenv
import os
from gradioComponent.QaEvaluator.evaluation import  Evaluator
from gradioComponent.QaEvaluator.questions import Questions

class Framework:

    def __init__(self):
        """initialize the working LLM environment"""
        self.openai = None
        self.model = None
        try:
            self.loadEnv()
        except Exception as e:
            print(f"LLM environment couldn't be loaded: {e}")
            return
            
    def loadEnv(self):
        load_dotenv(override=True)
        apikey = os.getenv('OPENAI_API_KEY')
        self.openai = OpenAI(api_key=apikey)
        self.model = 'gpt-4o-mini'

    def evaluate(self, all_text, choice):
        """This method will be used in gradio output to evaluate the answers written"""
        try:
            evaluator = Evaluator(self.model, self.openai)
            response = evaluator.evaluate(all_text, choice)
            return response
        except Exception as e:
            print(f"There is an error in evaluate: {e}")
            return "error in evalution of the answers submitted"
    
    def getQuestions(self, choice):
        """This method will get the questions based on choice made by user"""
        return Questions(choice).getQuestions()



            

