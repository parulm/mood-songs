import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from pygame import mixer


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.number = TextInput(multiline=False)
        self.add_widget(self.number)
        self.add_widget(Label(text=str(self.number)))
        print(self.number)
        print("songs/happy/"+str(self.number)+".mp3")
        

class MyApp(App):

    def build(self):
        return LoginScreen()
        #return Label(username)


if __name__ == '__main__':
    MyApp().run() 
