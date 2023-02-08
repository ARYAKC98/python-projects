import pyqrcode
from pyqrcode import QRCode
a = "hello"
url = pyqrcode.create(a)
url.svg("testqrcode.svg",scale=8)