import tkinter as tk

class Page4:
    def __init__(self, parent_frame):
        self.label = tk.Label(parent_frame, text="This is Page 4", font=("Helvetica", 16), padx=20, pady=20)
    def destroy(self):
        # Add any additional cleanup code here
        self.label.destroy()
        # self.view1.destroy()