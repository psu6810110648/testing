# screens/start_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        title_label = Label(text='KING OF FRUIT', font_size=50, size_hint=(1, 0.6))

        btn_start = Button(text='START GAME', font_size=30, size_hint=(1, 0.2), background_color=(0.2, 0.8, 0.2, 1))

        btn_start.bind(on_press=self.go_to_game)

        btn_exit = Button(text='EXIT', font_size=30, size_hint=(1, 0.2), background_color=(0.8, 0.2, 0.2, 1))

        btn_exit.bind(on_press=self.exit_game)

        layout.add_widget(title_label)
        layout.add_widget(btn_start)
        layout.add_widget(btn_exit)
        
        self.add_widget(layout)

    # --- ส่วนของ Callbacks ---
    def go_to_game(self, instance):
        print(">> กดปุ่มเริ่มเกม! กำลังสลับไปหน้า GameScreen...")

        self.manager.current = 'game'

    def exit_game(self, instance):
        print(">> กดปุ่มออกแอป!")
        from kivy.app import App
        App.get_running_app().stop()
        
# --- โค้ดส่วนนี้เอาไว้รันทดสอบเฉพาะไฟล์นี้ ---
if __name__ == '__main__':
    from kivy.app import App
    from kivy.uix.screenmanager import ScreenManager

    class TestStartApp(App):
        def build(self):
            # สร้างตัวจัดการหน้าจอ และใส่หน้า StartScreen ของบิวเข้าไป
            sm = ScreenManager()
            sm.add_widget(StartScreen(name='start'))
            return sm
            
    # คำสั่งสตาร์ทเครื่องยนต์ (รันแอป)
    TestStartApp().run()