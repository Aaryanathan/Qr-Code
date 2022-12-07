from pyqrcode import *
import png

s = "www.youtube.com"
url = pyqrcode.create(s)
url.svg("myqr.svg", scale=8)
url.png('myqr.png', scale=6)