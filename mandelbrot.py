from math import log, log2
from PIL import Image

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Image dimensions
WIDTH, HEIGHT = 600, 600

# Creating a new image using PIL, with specified dimensions and HSV mode
mandelbrot_img = Image.new("HSV", (WIDTH, HEIGHT))
pixels = mandelbrot_img.load()

SCALE = 150
ESC_RADIUS = 2
MAX_ITER = 50

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2


def draw_mandelbrot():
    for y in range(-HALF_HEIGHT, HALF_HEIGHT):
        for x in range(-HALF_WIDTH, HALF_WIDTH):
            num_of_iter, modulus = num_of_iterations(x / SCALE, y / SCALE)
            pixel_color = get_pixel_color(num_of_iter, modulus)

            # Transform the coordinates of every pixel depending on the centre of the screen
            pixels[x + HALF_WIDTH, y + HALF_HEIGHT] = pixel_color


def mandelbrot_log_func(num_of_iter, modulus):
    return abs(
        (num_of_iter - log2(log2(modulus) / log(ESC_RADIUS))) / num_of_iter)


def get_pixel_color(num_of_iter, modulus):
    if modulus <= ESC_RADIUS:
        return BLACK

    func = mandelbrot_log_func(num_of_iter, modulus)
    comp = int(255 * func)

    return comp, 255, 255


def num_of_iterations(x, y):
    c = complex(x, y)
    z = 0
    modulus = 0

    for iteration in range(MAX_ITER):
        modulus = abs(z)

        if modulus > ESC_RADIUS:
            return iteration, modulus

        z = z**2 + c

    return MAX_ITER, modulus


if __name__ == "__main__":
    draw_mandelbrot()
    mandelbrot_img.convert("RGB").save("generated-mandelbrot.png")
