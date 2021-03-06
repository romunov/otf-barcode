# -*- coding: utf-8 -*-

'''
Application that will, down the line, be able to print labels in real time. Hopefully.

@author Roman Luštrik (roman.lustrik@biolitika.si)
'''

# import statements
import Tkinter as tk
from functions import createBarCode

# class definition starts here
class otf(tk.Tk):

    label_height = 100
    label_width = 200
    preview_width = 150
    preview_height = 150

    def __init__(self, parent):
        tk.Tk.__init__(self, parent) # repeat arguments from def __init__()
        self.parent = parent
        # self.image = None
        # self.codeimage = None #
        self.rbv = tk.StringVar() # radio button value
        self.rbv.set("dm") # default selection is DataMatrix
        self.radiobuttons = None # radio buttons used in the application
        self.code = tk.StringVar()
        self.readcode = tk.Entry(self, textvariable = self.code) # entry field where code is entered
        self.gobutton = None # "display" button
        # self.cv = None
        self.photo = None # where image of the code is saved
        self.canvas_photo = None # canvas used, don't know why I can't put image on this canvas
        self.canvas_label = None # canvas used to display the label to be printed
        self.photo_on_canvas = None # image saved to canvas
        self.label_on_canvas = None # images displayed that will be printed/exported
        self.to_label_1d = None # store image for 1D code
        self.to_label_human = None # store image for human readable code

        self.initialize()

    def initialize(self):
        ## Define entry field
        self.code.set(u"USE UPPERCASE LETTERS ONLY")
        self.readcode = tk.Entry(master = self, textvariable = self.code, width = 30)
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

        ## Define radiobuttons
        # self.radiobuttons.set("L")
        self.radiobuttons = tk.Radiobutton(self, text = "QR code", variable = self.rbv, value = "qr",
                                           indicatoron = False, command = self.OnConfirm).grid(row = 2, column = 0,
                                                                                               sticky = tk.W)
        self.radiobuttons = tk.Radiobutton(self, text = "DataMatrix", variable = self.rbv, value = "dm",
                                           indicatoron = False, command = self.OnConfirm).grid(row = 2, column = 1,
                                                                                               sticky = tk.W)

        ## Create photo based on input available
        self.photo = createBarCode(otf_string = self.readcode.get())
        # Create blank canvas for printing label
        self.canvas_photo = tk.Canvas(master = self, width = otf.preview_width, height = otf.preview_height)
        # Add image to the canvas
        self.photo_on_canvas = self.canvas_photo.create_image(round(self.photo.width()/2), round(self.photo.height()/2),
                                                              anchor = tk.CENTER, image = self.photo)

        # # Create label and put it on canvas
        self.refreshLabel()

        # Place elements on the grid
        self.grid()
        self.readcode.grid(column = 0, row = 0, sticky = tk.E)
        self.gobutton.grid(column = 1, row = 0, sticky = tk.E)
        self.canvas_photo.grid(row = 1, columnspan = 2, sticky = tk.S)
        self.canvas_label.grid(row = 3, columnspan = 1, sticky = tk.N)

    # Reaction to click/<Enter> action on buttons
    def OnConfirm(self):
        self.readcode.focus_set()
        self.readcode.selection_range(0, tk.END)
        self.refreshImage()
        self.refreshLabel()

        return None

    def OnReturn(self, event):
        self.readcode.focus_set()
        self.readcode.selection_range(0, tk.END)
        self.refreshImage() # this refreshes the barcode image
        self.refreshLabel()  # this refreshes the label meant for printing

        return None

    def refreshImage(self):
        self.photo = createBarCode(otf_string = self.readcode.get(), codetype = self.rbv.get())
        self.canvas_photo.itemconfig(self.photo_on_canvas, image = self.photo)

        return None

    def refreshLabel(self):
        if self.label_on_canvas is not None:
            self.canvas_label.delete(self.label_on_canvas)

        self.canvas_label = tk.Canvas(master = self, width = otf.label_width, height = otf.label_height)
        self.to_label_1d = createBarCode(otf_string = self.readcode.get(), codetype = "128", ang = 90,
                                         size = (100, 100))
        self.to_label_human = createBarCode(otf_string = self.readcode.get(), codetype = "human", size = (50, 50),
                                            ang = 90)
        self.label_on_canvas = self.canvas_label.create_image(0, 25, anchor = tk.NW, image = self.to_label_human)
        self.label_on_canvas = self.canvas_label.create_image(50, 0, anchor = tk.NW, image = self.to_label_1d)
        self.label_on_canvas = self.canvas_label.create_image(150, 25, anchor = tk.NW, image = self.to_label_human)

        self.canvas_photo.grid(row = 1, columnspan = 2, sticky = tk.S)
        self.canvas_label.grid(row = 3, columnspan = 1, sticky = tk.N)

        return None

# run the program
if __name__ == "__main__":
    app = otf(None)
    app.title("On-the-fly barcode generator")
    app.mainloop()