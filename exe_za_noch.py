import random as rnd
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="Задай вопрос",
                      font_size=50,
                      on_press=self.btn_press,
                      background_color='cyan')
    def btn_press(self,instance):
        lst=('да',
             'нет',
             'возможно',
             'я так не думаю',
             'точно нет',
             'может быть',
             'иди нахуй заебал')
        instance.text=lst[rnd.randint(0,6)]
if __name__=="__main__":
    MyApp().run()
        
