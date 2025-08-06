import gradio as gr

class GradioSlider:
    def __init__(self):
        pass

    def squareNumber(self, num):
        return num ** 2

    def grSliderInterface(self):
        demo = gr.Interface(
            fn=self.squareNumber,
            inputs = gr.Slider(minimum=1, maximum=100, step=1),
            outputs = gr.Number(label="Square of the number"),
            theme=gr.themes.Soft()
        )

        return demo
