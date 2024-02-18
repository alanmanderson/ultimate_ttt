import pygame

pygame.init()
game = pygame.display.set_mode([900,1000])
game.fill((245,175,255))
blue = (0,43,255)
black = (0,0,0)
white = (255,255,255)
current_player = 0

def print_game_info(x, y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('GeeksForGeeks', True, white, blue)
    textRect = text.get_rect()
    textRect.center = (x, y)
    game.blit(text, textRect)

def print_board( x, y, width,color):
    print(x, y, width)

    pygame.draw.line(game,(color),(x+1/3*width,y),(x+1/3*width,y+width),10)

    pygame.draw.line(game,(color),(x+2/3*width,y),(x+2/3*width,y+width),10)

    pygame.draw.line(game,(color),(x,y+1/3*width),(x+width,y+1/3*width),10)

    pygame.draw.line(game,(color),(x,y+2/3*width),(x+width,y+2/3*width),10)



def draw_x(x, y, width):

    pygame.draw.line(game,(black),(x,y),(x+width,y+width),8)

    pygame.draw.line(game,(black),(x+width,y),(x,y+width),8)
    
def draw_o(x, y, width):
    width = 1/2*width
    pygame.draw.circle(game,white,(x+width,y+width),width,8)
    #pass
def print_selection( symbol, x, y):
    pass

for i in range(0, 900, 300):
    for j in range(0, 900, 300):

        print_board( i+10, j+10, 280,blue)

print_board(0, 0, 900,black)


continue_game = True

while continue_game:
    ev = pygame.event.get()

    for event in ev:
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print_selection("x", pos[0], pos[1])
            draw_x(pos[0], pos[1], 100)
            draw_o(pos[0], pos[1], 100)
            print(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                continue_game = False
    print_game_info(0, 900)
    pygame.display.flip()

pygame.quit()
