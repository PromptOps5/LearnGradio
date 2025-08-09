"""
This will be the main UI for question and answer evaluation
"""
from gradioComponent.QaEvaluator.framework import Framework
import gradio as gr
class AppUI:
    def __init__(self):
        self.framework = Framework()
        self.choice = None
        self.questions = None

    def setChoice(self, choice):
        self.choice = choice
        self.questions = self.getQuestions(self.choice)
        updateTextboxes = [gr.update(label=f"Q{i+1}: {q}", value="") for i, q in enumerate(self.questions)]
        return updateTextboxes

    def getQuestions(self, choice):
        return self.framework.getQuestions(self.choice)

    
    def evaluateAnswers(self, *inputs):
        questions = self.questions
        if not self.questions:
            return "No topic selected!"
        feedbackSummary = []
        
        for i in range(0,len(questions)):
            question =  questions[i]
            answer = inputs[i]
            feedbackSummary.append(f"Q{i+1}: {question}\nAnswer: {answer}")
        
        all_text = "\n\n".join(feedbackSummary)
        feedback = self.framework.evaluate(all_text, self.choice)
        return feedback


    def getInterface(self):
        with gr.Blocks() as demo:
            gr.Markdown("## Subjective Test Evaluation System")

            dropdown = gr.Dropdown(
                label="Choose topic wisely",
                choices = ['java','csharp','angular'],
                value=None
                )
            
            textBoxes = [
                gr.Textbox(
                    label=f"Q{i+1}",
                    lines = 3
                )

                for i in range(0,10)
            ]

            submit_button = gr.Button("Submit Answers")

            feedback_output = gr.HTML("Feedback per Question")

            dropdown.change(
                fn=self.setChoice,
                inputs = dropdown,
                outputs = textBoxes
            )

            submit_button.click(
                fn=self.evaluateAnswers,
                inputs=textBoxes,
                outputs=feedback_output
            )
        return demo