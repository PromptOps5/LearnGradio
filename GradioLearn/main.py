from gradioComponent.NumberFunction import Calculate
from gradioComponent.strReverse import StrReverse
from gradioComponent.slider import GradioSlider
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

if __name__ == "__main__":
    pass