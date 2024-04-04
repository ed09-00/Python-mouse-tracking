import tkinter as tk
from mouse_tracker import LineTracker
if __name__ == '__main__':
    app = tk.Tk()
    tracker = LineTracker(app)
    app.mainloop() 
