import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import os
import subprocess
import pyfiglet
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class calchiderapp(App):
	def build(self):
		self.window = Widget()
		self.window.cols = 1
		self.icon = "iconcon.png"
		self.logo = Image(source="logo.png")
		self.logo.y=(200)
		self.logo.x=(90)
		self.window.add_widget(self.logo)
		self.inicon = Label(text="Y/N_Calculator")
		self.window.add_widget(self.inicon)
		self.inicon.y=(450)
		self.box = TextInput(multiline=True)
		self.box.height=(30)
		self.box.width=(279)
		self.box.y=(450)
		self.window.add_widget(self.box)
		#creating 0 to 9 buttons
		self.butn1 = Button(text="1")
		self.window.add_widget(self.butn1)
		self.butn1.width=(18)
		self.butn1.height =(18)
		self.butn1.y=(370)
		#creating the butn2
		self.butn2 = Button(text="2")
		self.butn2.width=(18)
		self.butn2.height=(18)
		self.butn2.y=(370)
		self.butn2.x=(25)
		self.window.add_widget(self.butn2)
		return self.window

if __name__ == "__main__":
	calchiderapp().run()