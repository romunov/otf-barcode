# -*- coding: utf-8 -*-

'''

@author Roman Luštrik, 9.6.2015
Followed http://sebsauvage.net/python/gui/ to create the basic layout.
'''

import Tkinter
from PIL import Image, ImageTk
from barcode_handling import createBarCode

class otf(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.codeimage = None
        self.code = None
        self.readcode = None
        self.labelVariable = None
        self.initialize()

    def initialize(self):
        self.grid()

        # Entry field for barcode
        self.code = Tkinter.StringVar()
        self.readcode = Tkinter.Entry(self, textvariable = self.code)
        self.readcode.grid(column = 0, row = 0, sticky = "EW")
        self.readcode.bind("<Return>", self.OnPressEnter)
        self.code.set(u"Enter barcode name")

        # Create canvas
        self.codeimage = createBarCode(otf_string = self.readcode)
        # trying to display image http://stackoverflow.com/questions/14506497/image-in-canvas-backgroud-python
        cv = Tkinter.Canvas(master = None, width = self.codeimage.pixel_size,
                            height = self.codeimage.pixel_size)
        codeimage_canvas = cv.create_image(position = (0, 0), image = self.codeimage)
        codeimage_canvas.grid(column = 0, row = 1)

        # Button for printing
        gobutton = Tkinter.Button(self, text = u"Print",
                                  command = self.OnButtonClick)
        gobutton.grid(column = 1, row = 0)

        # some text under the entry field
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, anchor = "w",
                              fg = "white",
                              bg = "grey",
                              text = "test",
                              textvariable = self.labelVariable)
        self.labelVariable.set(u"Code will be printed here")

        # enable resizing
        self.grid_columnconfigure(0, weight = 1)
        self.resizable(True, True)

        # stop window resizing
        self.update()
        self.geometry(self.geometry())

        self.readcode.focus_set()
        self.readcode.selection_range(0, Tkinter.END)

        label.grid(column = 0, row = 1, sticky = "EW")

    def OnButtonClick(self):
        self.labelVariable.set(self.code.get())
        self.readcode.focus_set()
        self.readcode.selection_range(0, Tkinter.END)

        save_to_file = self.code.get() + ".png"
        self.codeimage.imsave(save_to_file, self.codeimage)

    def OnPressEnter(self, event):
        self.labelVariable.set(self.code.get())
        self.readcode.focus_set()
        self.readcode.selection_range(0, Tkinter.END)


if __name__ == "__main__":
    app = otf(None)
    app.title("On-the-fly barcode generator")
    app.mainloop()