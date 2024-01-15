import pygame as pg

pg.display.set_mode((500, 500))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    pg.display.update()