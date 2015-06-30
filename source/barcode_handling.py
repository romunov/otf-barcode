# -*- coding: utf-8 -*-

'''

@author Roman Luštrik, 11.6.2015
'''

import qrcode
import Tkinter
from PIL import ImageTk

def createBarCode(otf_string):
    qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 5, border = 6)

    qr.add_data(otf_string)

    qr.make(fit = True)

    img = qr.make_image()

    return img

def displayImage(self):
    self.image = createBarCode(otf_string = self.readcode)
    self.codeimage = ImageTk.PhotoImage(self.image)

    # Create canvas
    cv = Tkinter.Canvas(master = None, width = self.image.pixel_size,
                            height = self.image.pixel_size)

    # Add image to the canvas
    cv.create_image(0, 0, image = self.codeimage)

    cv.grid(column = 0, row = 1, columnspan = 2, padx = 5, pady = 5)