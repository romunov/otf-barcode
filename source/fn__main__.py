# -*- coding: utf-8 -*-

'''

@author Roman Luštrik, 29.6.2015
'''


from Tkinter import *
from barcode_handling import createBarCode
from PIL import Image, ImageTk
# import matplotlib.pyplot as plt

# def otf():
app_width = 600
app_height = 600

master = Toplevel()

canvas = Canvas(master, width = app_width, height = app_height)
canvas.pack()


img = createBarCode(otf_string = "M103")
# plt.imshow(img)

canvas.create_image(20, 20, anchor = NW, image = img)
img2 = img

# if __name__ == "__main__":
#     app = otf(None)
#     app.title("On-the-fly barcode generator")
#     app.mainloop()