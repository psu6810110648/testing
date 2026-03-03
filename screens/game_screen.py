from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle, Rectangle
import random
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

# --- 1. สร้างคลาสปุ่ม "ไพ่ผลไม้" (TileButton) ---
# อันนี้แหละที่จะทำให้มีกรอบขาวๆ สวยๆ
class TileButton(Button):
    def __init__(self, fruit_source, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''  # ลบพื้นหลังสีเทาเดิมของปุ่ม
        self.background_color = (0, 0, 0, 0) # ทำให้ปุ่มใส
        self.fruit_source = fruit_source
        
        # วาดกราฟิกเอง
        with self.canvas.before:
            # A. เงา (สีดำจางๆ)
            Color(0, 0, 0, 0.2)
            self.shadow = RoundedRectangle(pos=(self.x+3, self.y-3), size=self.size, radius=[15])
            
            # B. กรอบการ์ดสีขาว (หรือสีครีม)
            Color(0.95, 0.95, 0.9, 1) 
            self.card_bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[15])
            
        with self.canvas.after:
            # C. รูปผลไม้ (วาดทับลงไป)
            Color(1, 1, 1, 1)
            pad = 10 # ระยะห่างจากขอบ
            self.fruit_rect = Rectangle(source=self.fruit_source, 
                                      pos=(self.x+pad, self.y+pad), 
                                      size=(self.width-pad*2, self.height-pad*2))

        # สั่งให้มันขยับตามถ้าหน้าจอเปลี่ยนขนาด
        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        # อัปเดตตำแหน่งเงา
        self.shadow.pos = (self.x+3, self.y-3)
        self.shadow.size = self.size
        # อัปเดตตำแหน่งการ์ด
        self.card_bg.pos = self.pos
        self.card_bg.size = self.size
        # อัปเดตตำแหน่งผลไม้
        pad = 10
        self.fruit_rect.pos = (self.x+pad, self.y+pad)
        self.fruit_rect.size = (self.width-pad*2, self.height-pad*2)


# --- 2. หน้าจอเกมหลัก ---
class GameScreen(Screen):
    # Properties สำหรับ bind กับ UI
    slot_display = StringProperty("Slots: 0/7") # แก้เป็นภาษาอังกฤษก่อนกันสี่เหลี่ยม
    time_display = StringProperty("Time: 60")
    
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.fruit_types = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
        self.MAX_SLOTS = 7
        self.slots = []
        self.tiles = []
        self.score = 0
        self.game_over_flag = False
        self.time_left = 60
        
        # --- สร้าง UI ในโค้ดเลย (จะได้ไม่ต้องแก้ ui.kv ไปมา) ---
        self.layout = FloatLayout()
        
        # 1. พื้นหลัง (Background)
        self.bg = Image(source='assets/images/bg.png', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.bg)
        
        # 2. กระดานเกม (Game Board)
        # ปรับ size_hint เพื่อให้ตารางไม่เต็มจอเกินไป มีที่ว่างสวยๆ
        self.game_board = GridLayout(cols=7, spacing=10, padding=20,
                                     size_hint=(0.9, 0.6), 
                                     pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.layout.add_widget(self.game_board)
        
        # 3. แถบข้างล่าง (Slot Bar)
        # วาดพื้นหลังแถบสีเทาเข้ม
        with self.layout.canvas.after:
            Color(0.2, 0.2, 0.2, 0.9)
            RoundedRectangle(pos=(50, 20), size=(700, 100), radius=[20])

        self.add_widget(self.layout)

    def on_enter(self):
        """เริ่มเกมใหม่"""
        self.score = 0
        self.game_over_flag = False
        self.time_left = 60
        self.time_display = f"Time: {self.time_left}"
        self.generate_tiles()
        self.timer_event = Clock.schedule_interval(self.update_time, 1)

    def generate_tiles(self):
        """สุ่มและสร้างไพ่"""
        self.game_board.clear_widgets()
        self.tiles = []
        self.slots = []
        
        # สุ่มไพ่ 21 ใบ
        tile_list = []
        for i in range(7):
            fruit = self.fruit_types[i]
            for _ in range(3):
                tile_list.append(fruit)
        random.shuffle(tile_list)
        
        # สร้างปุ่มแบบใหม่ (TileButton)
        for fruit in tile_list:
            # ใช้ TileButton ที่เราสร้างไว้ข้างบน!
            tile_btn = TileButton(
                fruit_source=f'assets/images/picgame/{fruit}.png',
                size_hint=(None, None),
                size=(80, 80) # ขนาดการ์ด
            )
            
            # ผูกฟังก์ชันคลิก
            tile_btn.bind(on_press=lambda btn, f=fruit: self.on_tile_click_new(btn, f))
            self.game_board.add_widget(tile_btn)
            
            self.tiles.append({'fruit': fruit, 'widget': tile_btn})
        
        print(f"🎮 สร้างไพ่ {len(tile_list)} ใบแบบการ์ดสวยๆ เสร็จแล้ว!")

    def update_time(self, dt):
        if self.game_over_flag: return
        self.time_left -= 1
        self.time_display = f"Time: {self.time_left}"
        if self.time_left <= 0:
            self.game_over(is_win=False)

    def on_tile_click_new(self, btn_instance, fruit_type):
        if self.game_over_flag: return
        
        self.play_sound('click.wav')
        
        if len(self.slots) >= self.MAX_SLOTS: return

        # เพิ่มเข้า slot และซ่อนไพ่บนกระดาน
        self.slots.append(fruit_type)
        btn_instance.disabled = True
        btn_instance.opacity = 0
        
        self.check_match()
        self.check_win()

    def check_match(self):
        from collections import Counter
        fruit_count = Counter(self.slots)
        for fruit, count in fruit_count.items():
            if count >= 3:
                self.play_sound('match.wav')
                for _ in range(3): self.slots.remove(fruit)
                self.score += 100
                return True
        return False

    def check_win(self):
        visible_tiles = [t for t in self.tiles if t['widget'].opacity > 0]
        if len(visible_tiles) == 0:
            self.game_over(is_win=True)

    def game_over(self, is_win):
        self.game_over_flag = True
        result_screen = self.manager.get_screen('result')
        result_screen.update_result(is_win=is_win, score=self.score)
        self.manager.current = 'result'

    def on_leave(self):
        if hasattr(self, 'timer_event'): self.timer_event.cancel()

    def play_sound(self, sound_file):
        sound = SoundLoader.load(f'assets/sounds/{sound_file}')
        if sound: 
            sound.volume = 1.0
            sound.play()