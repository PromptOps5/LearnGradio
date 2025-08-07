from gradioComponent.slider import GradioSlider
import gradio as gr

class Calculate:
    """This class helps us to understand the number input box of gradio interface"""
    def __init__(self):
        pass

    def add(self,a,b):
        return a+b

    def calculator(self, num1, num2, operation):
        if operation=="addition":
            return num1+num2
        elif operation=="subtraction":
            return num1-num2
        elif operation=="multiplication":
            return num1 * num2
        elif operation=="division":
            if num2 != 0:
                return num1/num2
            else:
                return "Error num2 can't be zero"
        

    def grInterface(self):
        demo = gr.Interface(
            fn=self.add,
            inputs=[gr.Number(label="Number 1"),gr.Number(label="Number 2")],
            outputs=gr.Number(label="Sum"),
            title="Adddition Calculator",
            description="This is a simple addition calculator"
        )
        return demo
    
    def calculatorInterface(self):
        demo = gr.Interface(
            fn=self.calculator,
            inputs = [
                gr.Number(label="First Number"),
                gr.Number(label="Second Number"),
                gr.Dropdown(choices=["addition",
                "subtraction","multiplication","division"])
            ],
            outputs = gr.Number(label="Calculated value")
        )

        return demo