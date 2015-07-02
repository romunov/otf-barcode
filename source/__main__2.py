# -*- coding: utf-8 -*-

'''

@author 
'''

import Tkinter as tk
from PIL import Image, ImageTk

class otf(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent) # repeat arguments from def __init__()
        self.parent = parent
        self.image = None
        self.codeimage = None
        self.code = tk.StringVar()
        self.readcode = tk.Entry(self, textvariable = self.code)
        # self.labelVariable = None
        self.gobutton = None
        # self.cv = None
        self.photo = None
        self.initialize()


    def initialize(self):

        # Define entry field
        self.code.set(u"Enter barcode")
        self.readcode = tk.Entry(master = self, textvariable = self.code)
        self.readcode.bind("<Return>", self.OnConfirm)
        # Have the entry text selected to enable immediate typing
        self.readcode.focus_set()
        self.readcode.selection_range(0, tk.END)

        ## # Define bindings
        # Define button
        self.gobutton = tk.Button(self, text = "Display", command = self.OnConfirm)
        self.gobutton.bind("<Return>", self.OnReturn) # ok to focus on button using ALT and press Enter

        # Define enter
        self.readcode.bind("<Return>", self.OnReturn)

        ## Place figure on a canvas
        # Import photo and create canvas
        self.photo = Image.open("363.jpg")
        ph_width, ph_height = self.photo.size
        self.photo = ImageTk.PhotoImage(self.photo)
        cv = tk.Canvas(master = self, width = ph_width, height = ph_height)

        # Add image to the canvas
        cv.create_image(0,0, image = self.photo)

        # Place elements on the grid
        self.grid()
        self.readcode.grid(column = 0, row = 0)
        self.gobutton.grid(column = 1, row = 0)
        cv.grid(column = 0, row = 1, columnspan = 2)


    # Control resizing
    def OnConfirm(self):
        self.readcode.focus_set()
        self.readcode.selection_range(0, tk.END)
        print(self.readcode.get())

    def OnReturn(self, event):
        self.readcode.focus_set()
        self.readcode.selection_range(0, tk.END)
        print(self.readcode.get())



if __name__ == "__main__":
    app = otf(None)
    app.title("On-the-fly barcode generator")
    app.mainloop()