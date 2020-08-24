import neopixel
from machine import Pin
import time
from m5stack import *

np = neopixel.NeoPixel(Pin(26), 64)

RED = (10, 10, 0)
BLACK = (0, 0, 0)
COLOR = (0, 0, 0)

# необходимо понять, как запустить 2 или более точки в одну команду
# если оно у нас идёт по одному, как присваивание элементу списка? кортежа? словаря?
# Похоже, это список(list), каждому элементу которого мы присваиваем кортеж (tuple)
#print(type(np[0])) #так можно посмотреть тип данных, не удаляем пока

#вывод всех значений
def show_all_values():
    for i in np:
        print(i)

def for_range():
    for i in range (10):
        np[i] = COLOR
        np.write()
        i += 1
        time.sleep(0.1)


# functions of disposal led
def layer_h_1(color):
    for i in [0, 7, 8, 15, 16, 23, 24, 31, 32, 39, 40, 47, 48, 55, 56, 63]:
        np[i] = color
        np.write()
def layer_h_2(color):
    for i in [1, 6, 9, 14, 17, 22, 25, 30, 33, 38, 41, 46, 49, 54, 57, 62]:
        np[i] = color
        np.write()
def layer_h_3(color):
    for i in [2, 5, 10, 13, 18, 21, 26, 29, 34, 37, 42, 45, 50, 53, 58, 61]:
        np[i] = color
        np.write()
def layer_h_4(color):
    for i in [3, 4, 11, 12, 19, 20, 27, 28, 35, 36, 43, 44, 51, 52, 59, 60]:
        np[i] = color
        np.write()
def vertical_row_1(color):
    for i in [0, 1, 2, 3]:
        np[i] = color
        np.write()
def vertical_row_2(color):
    for i in [7, 6, 5, 4]:
        np[i] = color
        np.write()
def vertical_row_3(color):
    for i in [8, 9, 10, 11]:
        np[i] = color
        np.write()
def vertical_row_4(color):
    for i in [15, 14, 13, 12]:
        np[i] = color
        np.write()
def vertical_row_5(color):
    for i in [16, 17, 18, 19]:
        np[i] = color
        np.write()
def vertical_row_6(color):
    for i in [23, 22, 21, 20]:
        np[i] = color
        np.write()
def vertical_row_7(color):
    for i in [24, 25, 26, 27]:
        np[i] = color
        np.write()
def vertical_row_8(color):
    for i in [31, 30, 29, 28]:
        np[i] = color
        np.write()
def vertical_row_9(color):
    for i in [32, 33, 34, 35]:
        np[i] = color
        np.write()
def vertical_row_10(color):
    for i in [39, 38, 37, 36]:
        np[i] = color
        np.write()
def vertical_row_11(color):
    for i in [40, 41, 42, 43]:
        np[i] = color
        np.write()
def vertical_row_12(color):
    for i in [47, 46, 45, 44]:
        np[i] = color
        np.write()
def vertical_row_13(color):
    for i in [48, 49, 50, 51]:
        np[i] = color
        np.write()
def vertical_row_14(color):
    for i in [55, 54, 53, 52]:
        np[i] = color
        np.write()
def vertical_row_15(color):
    for i in [56, 57, 58, 59]:
        np[i] = color
        np.write()
def vertical_row_16(color):
    for i in [60, 61, 62, 63]:
        np[i] = color
        np.write()
# functions to generate good palettes of colors
# rainbow

def drop_all_leds():
    for i in range(64):
        np[i] = BLACK
        np.write()

def change_layers(color, delay):
    layer_h_1(color)
    time.sleep_ms(delay)
    layer_h_2(color)
    time.sleep_ms(delay)
    layer_h_3(color)
    time.sleep_ms(delay)
    layer_h_4(color)


x = 1
y = 1
z = 40
iteration_count = 0

color = (100, 0, 100)
'''while x < 40:
    iteration_count += 1
    
    change_layers(color, 100)
    
    x += 5
    y += 3
    z -= 2  
    if x > 40:
        x = 0
    if y > 40:
        y = 0
    if z < 2:
        y = 40
    #time.sleep(0.01)
    color = (x, y, z)
    '''
drop_all_leds()
delay_a = 7
dark =  (0, 0, 0)
dark_color = (0, 0, 0)
color = (10, 25, 25)
color2 = (0, 0, 0)

r = 0
g = 0
b = 0

# висим в цикле, выполняя действие по нажатию на большую кнопку M5, и выходим, если нажата кнопка Б
mode = 1
if mode == 1:
    while True:
        if btnA.isPressed() == True:
            vertical_row_1(color)
            time.sleep_ms(delay_a)

            vertical_row_1(dark)
            vertical_row_2(color)
            time.sleep_ms(delay_a)

            vertical_row_2(dark)
            vertical_row_3(color)
            time.sleep_ms(delay_a)

            vertical_row_3(dark)
            vertical_row_4(color)
            time.sleep_ms(delay_a)

            vertical_row_4(dark)
            vertical_row_5(color)
            time.sleep_ms(delay_a)

            vertical_row_5(dark)
            vertical_row_6(color)
            time.sleep_ms(delay_a)

            vertical_row_6(dark)
            vertical_row_7(color)
            time.sleep_ms(delay_a)

            vertical_row_7(dark)
            vertical_row_8(color)
            time.sleep_ms(delay_a)

            vertical_row_8(dark)
            vertical_row_9(color)
            time.sleep_ms(delay_a)

            vertical_row_9(dark)
            vertical_row_10(color)
            time.sleep_ms(delay_a)

            vertical_row_10(dark)
            vertical_row_11(color)
            time.sleep_ms(delay_a)

            vertical_row_11(dark)
            vertical_row_12(color)
            time.sleep_ms(delay_a)

            vertical_row_12(dark)
            vertical_row_13(color)
            time.sleep_ms(delay_a)

            vertical_row_13(dark)
            vertical_row_14(color)
            time.sleep_ms(delay_a)

            vertical_row_14(dark)
            vertical_row_15(color)
            time.sleep_ms(delay_a)

            vertical_row_15(dark)
            vertical_row_16(color)
            time.sleep_ms(delay_a)

            vertical_row_16(dark)
        else:
            drop_all_leds()
        if btnB.isPressed() == True:
            break

if mode == 2:
    while True:
        if btnA.isPressed() == True:

            vertical_row_6(color2)
            vertical_row_7(color2)
            vertical_row_10(color2)
            vertical_row_11(color2)
            r += 17
            g += 8
            b += 3


            vertical_row_1(color)
            time.sleep_ms(delay_a)

            vertical_row_1(dark_color)
            vertical_row_2(color)
            time.sleep_ms(delay_a)

            vertical_row_2(dark_color)
            vertical_row_3(color)
            time.sleep_ms(delay_a)

            vertical_row_3(dark_color)
            vertical_row_4(color)
            time.sleep_ms(delay_a)

            vertical_row_4(dark_color)
            vertical_row_5(color)
            time.sleep_ms(delay_a)

            vertical_row_5(dark_color)
            vertical_row_12(color)
            time.sleep_ms(delay_a)

            vertical_row_12(dark_color)
            vertical_row_13(color)
            time.sleep_ms(delay_a)

            vertical_row_13(dark_color)
            vertical_row_14(color)
            time.sleep_ms(delay_a)

            vertical_row_14(dark_color)
            vertical_row_15(color)
            time.sleep_ms(delay_a)

            vertical_row_15(dark_color)
            vertical_row_16(color)
            time.sleep_ms(delay_a)

            vertical_row_16(dark_color)
            vertical_row_9(color)
            time.sleep_ms(delay_a)

            vertical_row_9(dark_color)
            vertical_row_8(color)
            time.sleep_ms(delay_a)

            vertical_row_8(dark_color)
            color2 = (r, g, b)
        else:
            drop_all_leds()
        if btnB.isPressed() == True:
            break