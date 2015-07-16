# -*- coding: utf-8 -*-

'''
codetype is a string and can be "dm" (DataMatrix), "qr" (QR)
@author Roman Luštrik, 11.6.2015
'''

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageTk
import io
import Tkinter as tk

# Generate QR code
def createBarCode(otf_string, codetype = "dm", size = (200, 200), bg_color = "white", font_color = "black"):

    if codetype == "qr":
        # from hubarcode.qrcode import QRCodeEncoder
        # qr = QRCodeEncoder(otf_string)
        # qr_in_bytes = io.BytesIO(qr.get_imagedata())
        # img = PIL.Image.open(qr_in_bytes)

        # return img

        import qrcode
        qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 5, border = 6)
        qr.add_data(otf_string)
        qr.make(fit = True)
        img = qr.make_image()
        img = ImageTk.PhotoImage(img)

        return img

    if codetype == "dm":
        from hubarcode.datamatrix import DataMatrixEncoder
        dm = DataMatrixEncoder(otf_string)
        dm_in_bytes = io.BytesIO(dm.get_imagedata())
        img = Image.open(dm_in_bytes)
        img = ImageTk.PhotoImage(img)

        return img

    if codetype == "128":
        img = Image.new("RGB", size = size, color = bg_color)
        draw = ImageDraw.Draw(img)
        font_img = ImageFont.truetype(font = "code39.ttf")

        draw.text(xy = (10, 10), text = otf_string, font = font_img, fill = font_color)
        out_img = ImageTk.PhotoImage(img) # convert to PhotoImage since Canvas can't handle PIL images

        return out_img

    if codetype == "human":
        img = Image.new("RGB", size = size, color = bg_color)
        draw = ImageDraw.Draw(img)
        font_img = ImageFont.truetype(font = "seguisb.ttf")

        draw.text(xy = (10, 10), text = otf_string, font = font_img, fill = font_color)
        out_img = ImageTk.PhotoImage(img) # convert to PhotoImage since Canvas can't handle PIL images

        return out_img

# TODO: zrihtaj updatelabel, da bo delal kot se zagre
def updateLabel(self):
    self.to_label_1d = createBarCode(otf_string = self.readcode.get(), codetype = "128")
    self.to_label_human = createBarCode(otf_string = self.readcode.get(), codetype = "human", size = (20, 200))

    # draw images on canvas to be used as labels
    self.image_on_canvas_label = self.canvas_print_label.create_image(0, 0, anchor = tk.NW, image = self.to_label_1d)
    # calculate to_label_1d width and offset the second image by exactly that amount
    self.image_on_canvas_label = self.canvas_print_label.create_image(self.to_label_1d.width(), 0, anchor = tk.NW, image = self.photo)
    self.image_on_canvas_label = self.canvas_print_label.create_image(self.to_label_1d.width() + self.photo.width(), 0, anchor = tk.NW, image = self.to_label_human)

    return None

def refreshImage(self):
        self.photo = createBarCode(otf_string = self.readcode.get(), codetype = self.rbv.get()) # create barcode
        # ph_width, ph_height = self.photo.size # get size until it's hot
        self.photo = ImageTk.PhotoImage(self.photo) # convert it to PhotoImage
        self.canvas.itemconfig(self.image_on_canvas, image = self.photo) # update canvas

        return None