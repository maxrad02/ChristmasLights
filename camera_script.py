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
pixels[0] = (255, 0, 0)

def main():
    for i in range(1, num_pixels):
        pixels[i - 1] = (0, 0, 0)
        time.sleep(0.03)
        pixels.show()

        pixels[i] = (255, 0, 0)
        pixels.show()
        time.sleep(0.03)


main()
