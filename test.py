import pygame as pg
from Color import Color
from BoardView import BoardView
from Board import Board
from FileSelector import FileSelector

#b = Board(True)
#b.play([[2,0],[0,0]])
#b.play([[0,0],[2,0]])
#b.play([[2,0],[0,1]])
#b.play([[0,1],[2,0]])
#b.play([[2,0],[0,2]])
#b.play([[0,2],[2,0]])
#b.play([[2,1],[0,0]])
#b.play([[0,0],[2,1]])
#b.play([[2,1],[0,1]])
#b.play([[0,1],[2,1]])
#b.play([[2,1],[0,2]])
#b.play([[0,2],[2,1]])
#b.play([[2,2],[0,0]])
#b.play([[0,0],[2,2]])
#b.play([[2,2],[0,1]])
#b.play([[0,1],[2,2]])
#b.play([[2,2],[0,2]])
#breakpoint()
#print(b.check_winner())
#print(b.spaces)
#print(b.spaces[0])
#bv = BoardView(b, pg.Surface((600,600)))

pg.init()

rectangles = []

for i in range(4):
    for j in range(4):
        rectangles.append(pg.Rect([i * 200, j*200], [200, 200]))

screen = pg.display.set_mode([800,800])
screen.fill([200, 200, 200])
filled = {}

#font = pg.font.Font("Chalkduster/Chalkduster.ttf", 232)
#t = font.render("X", True, Color.WHITE, Color.DARK_GREEN)
#screen.blit(t, t.get_rect())

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
    #surface = bv.update()
    #screen.blit(surface, (100,100))

fs = FileSelector('games/', 500, 500)
fs_surface = fs.update()
container = pg.Surface((500,500))
container.blit(fs_surface, fs_surface.get_rect())

#def get_filename():
#    import easygui
#    file_name = easygui.fileopenbox()
#    print(file_name)

keep_going = True

while keep_going:
    fs_surface = fs.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keep_going = False
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            #get_filename()
            #t = pg.transform.scale_by(t, .5)
            #t = pg.transform.scale(t, (300,300))
            #screen.blit(t, t.get_rect())
            for i, r in enumerate(rectangles):
                mouse_pos = pg.mouse.get_pos()
                if r.collidepoint(mouse_pos):
                    filled[i] = True
                else:
                    print("no")
        elif event.type == pg.MOUSEWHEEL:
            #fs_surface.scroll(0, event.y)
            #screen.scroll(0, event.y)
            fs.increment_scroll_pos(event.y)
            #print(fs.scroll_pos, event.y)
    draw_rects()
    container.fill([120,220,250])
    container.blit(fs_surface, fs_surface.get_rect())
    screen.blit(container, container.get_rect())
    pg.display.flip()

pg.quit()
