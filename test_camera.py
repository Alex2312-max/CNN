from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time

from android.permissions import request_permissions, Permission


Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
    Button:
        text: 'Switch camera'
        size_hint_y: None
        height: '48dp'
        on_press: root.switch()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        self.camera = self.ids['camera'](0)
        print(self.ids)
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

    def switch(self):
        self.camera = self.ids['camera'](1)


class TestCamera(App):

    def build(self):
        request_permissions([Permission.CAMERA])
        return CameraClick()


if __name__ == '__main__':
    TestCamera().run()