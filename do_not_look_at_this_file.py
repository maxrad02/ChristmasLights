import board
import neopixel
import time
import random
# pixels = neopixel.NeoPixel(board.D12, 500)

# print("Lighting the first pixel red")

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D12

# The number of NeoPixels
num_pixels = 500

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1.0, auto_write=False, pixel_order=ORDER
)

pixels.fill((0, 0, 0))

direction = [0] * num_pixels
color = [0] * num_pixels
pix = [0] * num_pixels
inc = 4
max = 100

def switch_direction(i):
    if (pix[i][0] > max or pix[i][1] > max or pix[i][2] > max):
        direction[i] = 0

    if (color[i] < 2):
        if (pix[i][0] < inc):
            direction[i] = 1
            color[i] = random.randint(0, 2)
    if (color[i] == 2):
        if (pix[i][1] < inc):
            direction[i] = 1
            color[i] = random.randint(0, 2)

def christmas_cycle(wait):
    while True:
        pixels.show()
        time.sleep(wait)
        for i in range(num_pixels):
            switch_direction(i)
            inc_or_dec = -inc if direction[i] == 0 else inc   
            if (color[i] == 0):
                pix[i] = (pix[i][0] + inc_or_dec, 0, 0)                
                #pixels[i] = (pixels[i][0] + inc_or_dec, 0, 0)
                pixels[i] = pix[i]
            if (color[i] == 1):
                pix[i] = (pix[i][0] + inc_or_dec, pix[i][1] + inc_or_dec, pix[i][2] + inc_or_dec)
                #pixels[i] = (pixels[i][0] + inc_or_dec, pixels[i][1] + inc_or_dec, pixels[i][2] + inc_or_dec)
                pixels[i] = pix[i]
            if (color[i] == 2):
                pix[i] = (0, pix[i][1] + inc_or_dec, 0)
                #pixels[i] = (0, pixels[i][1] + inc_or_dec, 0)
                pixels[i] = pix[i]


def set_to_start_color():
    for i in range(num_pixels):
        random_brightness = random.randint(0, max)
        random_color = random.randint(0,2)

        direction[i] = random.randint(0, 1)
        color[i] = random_color

        if (random_color == 0):
            pixels[i] = (random_brightness, 0, 0)
            pix[i] = (random_brightness, 0, 0)
        if (random_color == 1):
            pixels[i] = (random_brightness, random_brightness, random_brightness)
            pix[i] = (random_brightness, random_brightness, random_brightness)
        if (random_color == 2):
            pixels[i] = (0, random_brightness, 0)
            pix[i] = (0, random_brightness, 0)

    pixels.show()



delay = 0.0000
set_to_start_color()
christmas_cycle(delay)
