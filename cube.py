import neopixel
from machine import Pin
import time

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

def layer_h_1(color):
    for i in [0, 7, 8, 15, 16, 23, 24, 31, 32, 39, 40, 47, 48, 55, 56, 63]:
        np[i] = color
        np.write()
 
def layer_h_2(COLOR):
    for i in [1, 6, 9, 14, 17, 22, 25, 30, 33, 38, 41, 46, 49, 54, 57, 62]:
        np[i] = COLOR
        np.write()

def layer_h_3(COLOR):
    for i in [2, 5, 10, 13, 18, 21, 26, 29, 34, 37, 42, 45, 50, 53, 58, 61]:
        np[i] = COLOR
        np.write()

def layer_h_4(COLOR):
    for i in [3, 4, 11, 12, 19, 20, 27, 28, 35, 36, 43, 44, 51, 52, 59, 60]:
        np[i] = COLOR
        np.write()

def drop_all_leds():
    for i in range(64):
        np[i] = BLACK
        np.write()

def change_layers(color):
    layer_h_1(color)
    time.sleep(0.03)
    layer_h_2(color)
    time.sleep(0.03)
    layer_h_3(color)
    time.sleep(0.03)
    layer_h_4(color)

x = 1
y = 1
z = 40
iteration_count = 0

color = (0, 0, 0)
while x < 40:
    iteration_count += 1
    
    change_layers(color)
    
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
    
drop_all_leds()
