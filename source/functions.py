# -*- coding: utf-8 -*-

'''
Static methods.
@author 
'''

import io

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageTk

def createBarCode(otf_string, codetype = "dm", size = (200, 200), bg_color = "white", font_color = "black"):
    if codetype == "qr":
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
