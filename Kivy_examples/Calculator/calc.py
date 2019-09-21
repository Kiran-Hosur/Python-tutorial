from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty,StringProperty)

class cal_1(GridLayout):
    count = NumericProperty(0)
    regB = NumericProperty(0)
    regA = NumericProperty(0)
    oper = StringProperty('')
    def selected(self,b):
        print(b.text)
        self.res.text += b.text
        self.count +=1
    def cls_screen(self):
        self.res.text = ""
        self.count = 0
    def add(self,op):
        self.regA = float(self.res.text)
        self.oper = str(op.text)
        self.cls_screen()
    def sub(self,op):
        self.regA = float(self.res.text)
        self.oper = str(op.text)
        self.cls_screen()
    def equal(self):
        self.regB = float(self.res.text)
        expn = str(self.regA) + self.oper + str(self.regB)
        res= eval(expn)
        self.res.text = str(res)

class calcApp(App):
    def build(self):
        return(cal_1())

calcApp().run()