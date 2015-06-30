# -*- coding: utf-8 -*-

'''

@author 
'''

import Tkinter as tk

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
        self.initialize()


    def initialize(self):

        # Define entry field
        self.code.set(u"Enter barcode")
        self.readcode = tk.Entry(master = self, textvariable = self.code)
        self.readcode.bind("<Return>", self.OnConfirm)
        # Have the entry text selected to enable immediate typing
        self.readcode.focus_set()
        self.readcode.selection_range(0, tk.END)

        # Define button
        self.gobutton = tk.Button(self, text = "Display", command = self.OnConfirm)

        # Place elements on the grid
        self.grid()
        self.readcode.grid(column = 0, row = 0, sticky = "EW")
        self.gobutton.grid(column = 1, row = 0)


    def OnConfirm(self):
        self.readcode.focus_set()
        self.readcode.selection_range(0, tk.END)



if __name__ == "__main__":
    app = otf(None)
    app.title("On-the-fly barcode generator")
    app.mainloop()