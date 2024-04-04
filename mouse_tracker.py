# 0,0       X increases -->
# +---------------------------+
# |                           | Y increases
# |                           |     |
# |   1920 x 1080 screen      |     |
# |                           |     V
# |                           |
# |                           |
# +---------------------------+ 1919, 1079
import tkinter as tk
import pyautogui


class LineTracker:
    def __init__(self, app, width = 250, height = 250, limit = 200):
        self.app = app
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(self.app, width = self.width, height = self.height)
        self.canvas.pack()
        self.lines = []
        self.limit = limit

        self.pre_x = 0
        self.pre_y = 0
        self.loop()

    #Convert program monitor coordinates to window coordinates.
    def _get_scale_coordination(self, x ,y):
        sys_width,sys_height = pyautogui.size()
        trans_width = sys_width / self.width
        trans_height = sys_height / self.height

        return x/trans_width ,y/trans_height
    
    #Input the coordinates of two points and draw a line segment between them on the canvas.
    def _add_line(self, x, y):
        scaled_x, scaled_y = self._get_scale_coordination(x,y)
        lind_id = self.canvas.create_line(self.pre_x, self.pre_y, scaled_x, scaled_y)
        self.lines.append(lind_id)

        if (len(self.lines) > self.limit):
            self.canvas.delete(self.lines.pop(0))
        
        self.pre_x = scaled_x
        self.pre_y = scaled_y
    
    #Continuously monitor the coordinates of the mouse cursor.
    def loop(self):
        print('Press Ctrl-C to quit.')

        try:
            while True:
                x, y = pyautogui.position()
                self._add_line(x,y)
                self.app.update()
        except KeyboardInterrupt:
            print('\n')

