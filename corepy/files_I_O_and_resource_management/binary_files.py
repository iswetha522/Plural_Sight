
import fractal
pixels = fractal.mandelbrot(448, 256)

import reprlib
print(reprlib.repr(pixels))

import bmp
bmp.write_grayscale("mandel.bmp", pixels)
print(bmp.dimensions("mandel.bmp")) # (448, 256)