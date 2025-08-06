import gradio as gr

class StrReverse:
    """This class helps us to understand the string input box of gradio interface"""
    def __init__(self):
        pass

    def strReverse(self, str):
        return str[::-1]

    def strConcat(self, str1, str2):
        return str1 +" "+ str2

    def StrReverseInterface(self):
        demo = gr.Interface(
            fn=self.strReverse,
            inputs=gr.Textbox(label="Enter a string"),
            outputs=gr.Textbox(label="Reversed string"),
        )

        return demo

    def StrConcatInterface(self):
        demo = gr.Interface(
            fn=self.strConcat,
            inputs=[gr.Textbox(label="Enter a string"),gr.Textbox(label="Enter a string")],
            outputs=gr.Textbox(label="Concatenated string"),
        )

        return demo
