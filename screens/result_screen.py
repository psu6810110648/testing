from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.app import App
from kivy.graphics import Color, RoundedRectangle

# --- คลาสปุ่มขอบมน ---
class RoundedButton(Button):
    def __init__(self, bg_color=(0.2, 0.8, 0.2, 1), radius=25, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        with self.canvas.before:
            Color(rgba=bg_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[radius])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

# --- หน้าจอสรุปผล (Result Screen) ---
class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()

        # 1. พื้นหลัง (เปลี่ยนเป็น self.bg_image เพื่อให้สั่งเปลี่ยนรูปได้ทีหลัง)
        self.bg_image = Image(source='assets/images/bg.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg_image)
        
        # 2. พื้นหลังสีดำจางๆ (Overlay) - ปรับลดลงนิดนึงจะได้เห็นรูปสวยๆ ชัดขึ้น
        with layout.canvas.after:
            Color(0, 0, 0, 0.3) # ปรับความเข้มเงาตรงนี้ (0.3 = จาง, 0.7 = มืด)
        
        # 3. ข้อความแสดงผล (เงา + ตัวจริง)
        self.result_shadow = Label(
            text='[b]YOU WIN![/b]', markup=True,
            font_size='80sp', color=(0, 0, 0, 0.5),
            pos_hint={'center_x': 0.51, 'center_y': 0.69}
        )
        layout.add_widget(self.result_shadow)

        self.result_label = Label(
            text='[b]YOU WIN![/b]', markup=True,
            font_size='80sp', color=(1, 0.85, 0.1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        layout.add_widget(self.result_label)

        # 4. ข้อความบอกคะแนน (เปลี่ยนเป็นสีเข้ม ตามที่คุยกัน เพื่อให้อ่านง่ายบนทุเรียน)
        self.score_label = Label(
            text='Score: 1,500', font_size='45sp', bold=True,
            color=(1, 1, 1, 1), # เริ่มต้นสีขาว (เดี๋ยวเปลี่ยนออโต้ในฟังก์ชันด้านล่าง)
            pos_hint={'center_x': 0.5, 'center_y': 0.55}
        )
        layout.add_widget(self.score_label)

        # 5. ปุ่ม Play Again
        btn_restart = RoundedButton(
            text='PLAY AGAIN', font_size='24sp', bold=True,
            bg_color=(0.2, 0.6, 1, 1), # สีฟ้า
            size_hint=(0.4, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.35}
        )
        btn_restart.bind(on_press=self.restart_game)
        layout.add_widget(btn_restart)

        # 6. ปุ่ม Main Menu
        btn_home = RoundedButton(
            text='MAIN MENU', font_size='20sp', bold=True,
            bg_color=(0.9, 0.5, 0.1, 1), # สีส้ม
            size_hint=(0.3, 0.08),
            pos_hint={'center_x': 0.5, 'center_y': 0.22}
        )
        btn_home.bind(on_press=self.go_home)
        layout.add_widget(btn_home)

        self.add_widget(layout)

    # --- ฟังก์ชันอัปเดตผลลัพธ์ (หัวใจสำคัญ!) ---
    def update_result(self, is_win, score):
        if is_win:
            # 🏆 ถ้าชนะ: ใช้รูป bg_win.png และตัวหนังสือสีทอง
            self.bg_image.source = 'assets/images/win.png'
            self.result_label.text = "[b]YOU WIN![/b]"
            self.result_label.color = (1, 0.85, 0.1, 1) # สีทอง
            self.score_label.color = (0.4, 0.2, 0, 1) # คะแนนสีน้ำตาลเข้ม (ให้อ่านง่ายบนพื้นทอง)
        else:
            # 💀 ถ้าแพ้: ใช้รูป bg.png เดิม และตัวหนังสือสีแดง
            self.bg_image.source = 'assets/images/bg.png' 
            self.result_label.text = "[b]GAME OVER[/b]"
            self.result_label.color = (0.9, 0.2, 0.2, 1) # สีแดง
            self.score_label.color = (1, 1, 1, 1) # คะแนนสีขาวปกติ
            
        self.score_label.text = f"Score: {score:,}" # ใส่ลูกน้ำคั่นหลักพันให้ด้วย
        self.result_shadow.text = self.result_label.text

    # --- Callbacks ---
    def restart_game(self, instance):
        print(">> กดปุ่มเล่นอีกครั้ง")
        # self.manager.current = 'game' 

    def go_home(self, instance):
        print(">> กดปุ่มกลับหน้าเมนู")
        self.manager.current = 'start'

# --- ส่วนทดสอบรัน ---
if __name__ == '__main__':
    from kivy.app import App
    from kivy.uix.screenmanager import ScreenManager
    
    # จำลองสถานะ (ลองเปลี่ยน True เป็น False เพื่อเทสหน้าแพ้)
    TEST_WIN = True 

    class TestResultApp(App):
        def build(self):
            sm = ScreenManager()
            result_screen = ResultScreen(name='result')
            sm.add_widget(result_screen)
            
            # จำลองการส่งค่าคะแนนเข้าไป
            result_screen.update_result(is_win=TEST_WIN, score=2500)
            
            return sm

    TestResultApp().run()