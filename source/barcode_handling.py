# -*- coding: utf-8 -*-

'''
codetype is a string and can be "dm" (DataMatrix), "qr" (QR)
@author Roman Luštrik, 11.6.2015
'''



import PIL
import io

# Generate QR code
def createBarCode(otf_string, codetype = "dm"):

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

        return img

    if codetype == "dm":
        from hubarcode.datamatrix import DataMatrixEncoder
        dm = DataMatrixEncoder(otf_string)
        dm_in_bytes = io.BytesIO(dm.get_imagedata())
        img = PIL.Image.open(dm_in_bytes)

        return img

