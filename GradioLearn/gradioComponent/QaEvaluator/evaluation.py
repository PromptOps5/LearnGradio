"""
This class will contain the logic for the evaluation of the questions and answers
"""

from gradioComponent.QaEvaluator.prompts import Prompt

class Evaluator:

    def __init__(self,model,openai_client):
        self.model = model
        self.openAi = openai_client

    def evaluate(self, all_text, choice):
        """This will evaluate the questions and answer based on the LLM"""
        try: 
            prompt = Prompt()

            evaluation_prompt = prompt.getPrompt(all_text, choice)

            prompt_body = [
                {"role": "system", "content": evaluation_prompt},
                {"role": "user", "content": all_text}
            ]

            response = self.openAi.chat.completions.create(
                        model=self.model,
                        messages=prompt_body,
                        temperature=0.2
                    )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in the evaluation logic: {e}")
            return "Error in LLM response generation"
