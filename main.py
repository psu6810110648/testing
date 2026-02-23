from kivy.app import App
from kivy.uix.label import Label

class KingOfFruitApp(App):
    def build(self):
        # สร้างข้อความต้อนรับง่ายๆ ก่อน
        return Label(text='Welcome to King of Fruit (Kivy Version!)', font_size=24)

if __name__ == '__main__':
    KingOfFruitApp().run()