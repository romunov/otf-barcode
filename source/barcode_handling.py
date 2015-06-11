# -*- coding: utf-8 -*-

'''

@author Roman Luštrik, 11.6.2015
'''

import qrcode

def createBarCode(otf_string):
    qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 5, border = 6)

    qr.add_data(otf_string)

    qr.make(fit = True)

    img = qr.make_image()

    save_to_file = otf_string + ".png"
    img.save("m001.png")

    return img
