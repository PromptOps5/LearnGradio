"""
This class will have the logic to get the questions based on the options chosen by the user
"""
import json
import os
class Questions:

    def __init__(self, choice):
        self.choice = choice
        self.questionnaire  = self._loadQuestionaire()

    
    def _loadQuestionaire(self):
        """Load the questionaire from the file path"""
        try:
            questions = []
            file_path = 'D:\\Projects\Gradio\\LearnGradio\\GradioLearn\\gradioComponent\\resource\\questions.json'
            if not os.path.exists(file_path):
                return questions
            with open(file_path,'r',encoding='utf-8') as f:
                questions = json.load(f)
            return questions
        except Exception as e:
            print(f"exception in loadQuestionaire: {e}")
            return []
    
    def _fetchSubjectQuestion(self):
        """Questions pertaining to the choice"""
        try:
            questions = []
            if self.questionnaire:
                for ques in self.questionnaire:
                    if ques['topic'].lower() == self.choice.lower():
                        questions.append(ques['question'])
                return questions
            return questions
        except Exception as e:
            print(f"An error occured in fetchSubjecsQuestion: {e}")
            return []


    def getQuestions(self):
        """public to framework method to fetch the questions related to the choice made"""
        questions = self._fetchSubjectQuestion()
        return questions
        

