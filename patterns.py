import time
from math import *
import random

NUM_PIXELS = 50
ORANGE = (238, 65, 25)
GREEN = (0, 255, 0)
WHITE = (255, 255, 175)
OFF = (0, 0, 0)

def off(fc):
    pixels = [(0, 0, 0)] * NUM_PIXELS
    put_symmetric(fc, pixels)
    put_symmetric(fc, pixels)

def orange(fc):
    pixels = [ORANGE] * NUM_PIXELS
    put_symmetric(fc, pixels)
    put_symmetric(fc, pixels)

def green(fc):
    pixels = [GREEN] * NUM_PIXELS
    put_symmetric(fc, pixels)
    put_symmetric(fc, pixels)

def white(fc):
    pixels = [WHITE] * NUM_PIXELS
    put_symmetric(fc, pixels)
    put_symmetric(fc, pixels)

def bacon_static(fc):
    pixels = [(0, 0, 0)] * NUM_PIXELS
    for i in range(NUM_PIXELS/2):
        pixels[2*i] = ORANGE
        pixels[2*i+1] = GREEN
    put_symmetric(fc, pixels)

def bacon_static_inverse(fc):
    pixels = [(0, 0, 0)] * NUM_PIXELS
    for i in range(0, NUM_PIXELS, 2):
        pixels[i] = GREEN
        pixels[i+1] = ORANGE
    put_symmetric(fc, pixels)

def twinkle(fc):
    pixels = [(0, 0, 0)] * NUM_PIXELS * 2
    for i in range(0, NUM_PIXELS*2, 2):
        pixels[i] = ORANGE
        pixels[i+1] = GREEN

    for i in range(0, NUM_PIXELS*2):
        if(random.randint(0, 100) < 5):
            pixels[i] = (25, 255, 175)

    fc.put_pixels(pixels)
    time.sleep(0.05)

def strobe(fc):
    orange(fc)
    time.sleep(0.05)
    off(fc)
    time.sleep(0.05)
    green(fc)
    time.sleep(0.05)
    off(fc)
    time.sleep(0.05)
    white(fc)
    time.sleep(0.03)
    off(fc)
    time.sleep(0.05)

def chase(fc):
    pixels = [(0, 0, 0)] * NUM_PIXELS

    for i in range(NUM_PIXELS):
        pixels[i] = ORANGE
        put_symmetric(fc, pixels)
        time.sleep(0.1)

    for i in range(NUM_PIXELS):
        pixels[i] = GREEN
        put_symmetric(fc, pixels)
        time.sleep(0.1)

def stack(fc):
    position = NUM_PIXELS
    while(position > 0):
        for i in range(position):
            pixels = [GREEN] * NUM_PIXELS

            for j in range(position, NUM_PIXELS):
                pixels[j] = ORANGE

            pixels[i] = ORANGE
            put_symmetric(fc, pixels)

            time.sleep(0.05)

        position -= 1

    position = NUM_PIXELS

    while(position > 0):
        for i in range(position):
            pixels = [ORANGE] * NUM_PIXELS

            for j in range(position, NUM_PIXELS):
                pixels[j] = GREEN

            pixels[i] = GREEN
            put_symmetric(fc, pixels)

            time.sleep(0.05)

        position -= 1

def colorwheel(fc):
    SCALE = 128
    SEPARATION = 10
    z = time.time() % 255
    pixels = [OFF] * NUM_PIXELS * 2

    for i in range(0, NUM_PIXELS*2):
        pixels[i] = wheel(int(z * SCALE + SEPARATION * i) % 255)

    fc.put_pixels(pixels)

def wheel(pos):
    pos = int(pos) % 255
    if pos < 85:
        return (255 - pos * 3, 0, pos * 3)
    if pos < 170:
        pos -= 85
        return (0, pos * 3, 255 - pos * 3)

    pos -= 170
    return (pos * 3, 255 - pos * 3, 0)

def put_symmetric(fc, input):
    copy = list(input)
    copy.extend(copy)
    fc.put_pixels(copy)
