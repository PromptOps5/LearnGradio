from gradioComponent.NumberFunction import Calculate
from gradioComponent.strReverse import StrReverse
from gradioComponent.slider import GradioSlider
from gradioComponent.FileUpload import FileUpload

def AddFunction():
    add = Calculate()
    add.grInterface().launch()

def Calculator():
    demo = Calculate()
    demo.calculatorInterface().launch()

def StringReverse():
    strReverse = StrReverse()
    strReverse.StrReverseInterface().launch()

def StringConcat():
    strConcat = StrReverse()
    strConcat.StrConcatInterface().launch()

def SliderInterface():
    demo = GradioSlider()
    demo.grSliderInterface().launch()

def TextFileUpload():
    demo = FileUpload()
    demo.fileUploadInterface().launch()

def getDataFrames():
    demo = FileUpload()
    demo.GetFileDataFrame().launch()

def getDataFramesWithSlider():
    demo = FileUpload()
    demo.GetFileFrameWithSlider().launch()

if __name__ == "__main__":
    pass