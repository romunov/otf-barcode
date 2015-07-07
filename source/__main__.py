# -*- coding: utf-8 -*-

'''

@author Roman Luštrik (roman.lustrik@biolitika.si)
'''

import Tkinter as tk
from PIL import ImageTk
from barcode_handling import createBarCode
from PIL import Image

class otf(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent) # repeat arguments from def __init__()
        self.parent = parent
        # self.image = None
        # self.codeimage = None #
        self.rbv = tk.StringVar() # radio button value
        self.radiobuttons = None # radio buttons used in the application
        self.code = tk.StringVar()
        self.readcode = tk.Entry(self, textvariable = self.code) # entry field where code is entered
        self.gobutton = None # "display" button
        # self.cv = None
        self.photo = None # where image of the code is saved
        self.canvas = None # canvas used, don't know why I can't put image on this canvas
        self.image_on_canvas = None # image saved to canvas
        self.image_on_canvas_label1 = None
        self.image_on_canvas_label2 = None
        self.canvas_print_label = None # canvas used to display the label to be printed
        self.to_label_1d = None # image for label
        self.to_label_2d = None # image for label

        self.initialize()


    def initialize(self):

        ## Define entry field
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

        ## Define radiobuttons
        # self.radiobuttons.set("L")
        self.radiobuttons = tk.Radiobutton(self, text = "QR code", variable = self.rbv, value = "qr",
                                           indicatoron = False, command = self.OnConfirm).grid(row = 2, column = 0,sticky = tk.W)
        self.radiobuttons = tk.Radiobutton(self, text = "DataMatrix", variable = self.rbv, value = "dm",
                                           indicatoron = False, command = self.OnConfirm).grid(row = 2, column = 1, sticky = tk.W)

        ## Place figure on a canvas
        # Import photo and create canvas
        self.photo = createBarCode(otf_string = self.readcode.get())
        ph_width, ph_height = self.photo.size
        self.photo = ImageTk.PhotoImage(self.photo)
        self.canvas = tk.Canvas(master = self, width = ph_width, height = ph_height)
        self.canvas_print_label = tk.Canvas(master = self, width = 600, height = 300)

        # Add image to the canvas
        self.image_on_canvas = self.canvas.create_image(round(ph_height/2), round(ph_width/2), image = self.photo)


        ## Create label for printing
        # Create 1D and 2D barcodes
        # first create an empty image and insert barcodes
        label_img = Image.new("RGB", size = (400, 200), color = "white") # hardcoded size, TODO: to make it dynamic
        self.to_label_2d = self.photo # from ImageTk.PhotoImage, NOT Image
        self.to_label_1d = createBarCode(otf_string = "tralala", codetype = "128")
        print("tralala")
        self.image_on_canvas_label1 = self.canvas_print_label.create_image(0, 0, image = self.to_label_1d)
        self.image_on_canvas_label2 = self.canvas_print_label.create_image(200, 0, image = self.to_label_2d)

        # Place elements on the grid
        self.grid()
        self.readcode.grid(column = 0, row = 0)
        self.gobutton.grid(column = 1, row = 0, sticky = tk.E)
        self.canvas.grid(row = 1, columnspan = 2, sticky = tk.N)

    # Control resizing
    def OnConfirm(self):
        self.readcode.focus_set()
        self.readcode.selection_range(0, tk.END)

        self.photo = createBarCode(otf_string = self.readcode.get(), codetype = self.rbv.get()) # create barcode
        # ph_width, ph_height = self.photo.size # get size until it's hot
        self.photo = ImageTk.PhotoImage(self.photo) # convert it to PhotoImage
        self.canvas.itemconfig(self.image_on_canvas, image = self.photo) # update canvas
        # self.canvas.config(width = ph_width, height = ph_height)

    def OnReturn(self, event):
        self.readcode.focus_set()
        self.readcode.selection_range(0, tk.END)
        # print(self.readcode.get())
        # print(self.code)

        self.photo = createBarCode(otf_string = self.readcode.get(), codetype = self.rbv.get()) # create barcode
        # ph_width, ph_height = self.photo.size # get size until it's hot
        self.photo = ImageTk.PhotoImage(self.photo) # convert it to PhotoImage
        self.canvas.itemconfig(self.image_on_canvas, image = self.photo) # update canvas
        # self.canvas.config(width = ph_width, height = ph_height)

if __name__ == "__main__":
    app = otf(None)
    app.title("On-the-fly barcode generator")
    app.mainloop()