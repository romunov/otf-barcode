# -*- coding: utf-8 -*-

'''

@author Roman Luštrik, 9.6.2015
Followed http://sebsauvage.net/python/gui/ to create the basic layout.
'''

import Tkinter
from barcode_handling import createBarCode, displayImage

class otf(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.image = None
        self.codeimage = None
        self.code = None
        self.readcode = None
        self.labelVariable = None
        self.gobutton = None
        self.cv = None
        self.initialize()


    def initialize(self):

        self.grid()

        # Entry field for barcode
        self.code = Tkinter.StringVar()
        self.readcode = Tkinter.Entry(self, textvariable = self.code)
        self.readcode.grid(column = 0, row = 0, sticky = "EW")
        self.readcode.bind("<Return>", self.OnPressEnter)
        self.code.set(u"Enter barcode name")

        # Button for printing
        self.gobutton = Tkinter.Button(self, text = u"Display",
                                  command = self.OnButtonClick)
        self.gobutton.grid(column = 1, row = 0)

        # some text under the entry field
        # self.labelVariable = Tkinter.StringVar()
        # label = Tkinter.Label(self, anchor = "w",
        #                       fg = "white",
        #                       bg = "grey",
        #                       text = "test",
        #                       textvariable = self.labelVariable)
        # self.labelVariable.set(u"Code will be printed here")

        #Display default image
        displayImage(self)

        # enable resizing
        self.grid_columnconfigure(0, weight = 1)
        self.resizable(True, True)

        # stop window resizing
        self.update()
        self.geometry(self.geometry())

        self.readcode.focus_set()
        self.readcode.selection_range(0, Tkinter.END)

        # label.grid(column = 0, row = 1, sticky = "EW")

    def OnButtonClick(self):
        # self.labelVariable.set(self.code.get())
        self.readcode.focus_set()
        self.readcode.selection_range(0, Tkinter.END)

        displayImage(self)

        # save_to_file = self.code.get() + ".png"
        # plt.imsave(save_to_file, self.image)

    def OnPressEnter(self, event):
        # self.labelVariable.set(self.code.get())
        self.readcode.focus_set()
        self.readcode.selection_range(0, Tkinter.END)


if __name__ == "__main__":
    app = otf(None)
    app.title("On-the-fly barcode generator")
    app.mainloop()