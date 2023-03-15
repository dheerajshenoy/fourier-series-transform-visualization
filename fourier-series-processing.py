import pygame as pg
from pygame import *
from pygame.draw import line, circle
import numpy as np

clock = pg.time.Clock()

pg.init()

running = True
paused = False

d_info = pg.display.Info()
#screen = pg.display.set_mode((d_info.current_w, d_info.current_h))
bg = (0, 0, 0)

sw, sh = 1400, 1000
screen = pg.display.set_mode((sw, sh))

#sw, sh = d_info.current_w, d_info.current_h

x = 0
y = 0


font = pg.font.SysFont("Rajdhani", 50)
img = font.render('PAUSED', True, (255, 255, 255))

time = 0.0
dt = 0.1

X, Y = sw/2, sh/2

WHITE = (255, 255, 255)

cir1 = [sw/2 - 400, sh/2]
r = 80
wave = []

def update():
    global time, dt, X, Y
    time += dt
    X = cir1[0] + r * np.cos(time)
    Y = cir1[1] + r * np.sin(time)
    wave.insert(0, Y)


def render():
    screen.fill(bg)
    global dt, X, Y
    circle(center=cir1, radius=r, surface=screen, color=WHITE, width=1)
    line(start_pos=cir1, end_pos=(X, Y), surface=screen, color=WHITE)
    circle(center=(X, Y), radius=6, surface=screen, color=WHITE, width=0)

    for i in range(len(wave)):
        end_pos = (sw/2 + i, wave[i])
        circle(center=end_pos, radius=2, surface=screen, color=WHITE)
    line(end_pos=(X, Y), start_pos=(sw/2, wave[0]), surface=screen, color=WHITE)

    pg.display.update()

    if len(wave) > 500:
        wave.pop()

while running:
    clock.tick(30)
    ev = pg.event.get()

    for events in ev:
        if events.type == pg.QUIT:
            running = False

        if events.type == pg.KEYUP:
            if events.key == pg.K_SPACE:
                paused = not paused

    if paused:
        screen.blit(img, (20, 20))
        pg.display.update()
    else:
        update()
        render()

