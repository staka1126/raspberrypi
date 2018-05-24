from picamera import PiCamera
from time import sleep
import datetime
import os
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

td = datetime.date.today()
ymd = td.strftime("%Y%m%d")
ymdhms = td.strftime("%Y%m%d%H%M%S")

if os.path.exists("/home/pi/DCIM/" + ymd) == False:
    os.makedirs("/home/pi/DCIM/" + ymd)

camera = PiCamera()
camera.awb_mode = "fluorescent"
camera.capture("/home/pi/DCIM/" + ymd + "/DCIM_" + ymdhms + ".jpg")

# Raspberry Pi pin configuration
RST = 24

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

image = Image.open("/home/pi/DCIM/" + ymd + "/DCIM_" + ymdhms + ".jpg")
image = image.resize((128, 96))
image = image.crop((0, 16, 128, 80))
image = image.convert("1")

disp.image(image)
disp.display()
