from blinkt import set_pixel, set_brightness, show, clear
import time

set_brightness(0.1)

c_to_rgb = {
    'r':   (255, 0, 0),
    'g':  (0, 255, 0),
    'b': (0, 0, 255)
}

def set_color(color, timeout=2):
    code = c_to_rgb[color]
    for i in range(8):
        set_pixel(i, code[0], code[1], code[2])
    show()
    time.sleep(timeout)
    clear()

if __name__ == '__main__':
    set_color('r')
