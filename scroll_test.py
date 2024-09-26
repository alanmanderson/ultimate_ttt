try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
from tkfilebrowser import askopendirname, askopenfilenames, asksaveasfilename



import pygame as pg
from Color import Color
from BoardView import BoardView
from Board import Board
from tkfilebrowser import askopendirname

askopendirname()

rectangles = []

for i in range(4):
    for j in range(4):
        rectangles.append(pg.Rect([i * 200, j*200], [200, 200]))

screen = pg.display.set_mode([800,800])
screen.fill([200, 200, 200])
filled = {}

font = pg.font.Font("Chalkduster/Chalkduster.ttf", 232)
t = font.render("X", True, Color.WHITE, Color.DARK_GREEN)
screen.blit(t, t.get_rect())

def draw_rects():
    mouse_pos = pg.mouse.get_pos()
    for i,r in enumerate(rectangles):
        s = pg.Surface((200,200))
        c = [0, 0, 15 * i]
        s.fill(c)
        if i in filled:
            pg.draw.circle(s, [150,25,25], [100,100], 80, 3)
        screen.blit(s, r)
        if r.collidepoint(mouse_pos):
            pg.draw.rect(screen, [200, 200, 0], r, 3)
    surface = bv.update()
    screen.blit(surface, (100,100))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            #t = pg.transform.scale_by(t, .5)
            t = pg.transform.scale(t, (300,300))
            screen.blit(t, t.get_rect())
            for i, r in enumerate(rectangles):
                mouse_pos = pg.mouse.get_pos()
                if r.collidepoint(mouse_pos):
                    filled[i] = True
                else:
                    print("no")            
    draw_rects()
    pg.display.flip()
