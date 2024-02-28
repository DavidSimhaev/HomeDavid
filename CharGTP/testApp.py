from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import threading
import time

class MyApp(App):
    def build(self):
        self.text_input = TextInput(text='Initial Text')
        threading.Thread(target=self.text_change_thread).start()
        return self.text_input

    def text_change_thread(self):
        while True:
            time.sleep(5)
            Clock.schedule_once(self.update_text)

    def update_text(self, dt):
        # Обновление текста в основном потоке
        self.text_input.text = "New Text"

if __name__ == '__main__':
    MyApp().run()
