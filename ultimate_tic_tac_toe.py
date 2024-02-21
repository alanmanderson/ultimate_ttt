import pygame
import math
import random
from Board import Board
from BoardController import BoardController
from View import View

pygame.init()
master_board_width = 900
small_board_width = 280
game = pygame.display.set_mode([master_board_width,1000])
game.fill((245,175,255))
purple = (245,175,255)
blue = (0,43,255)
black = (0,0,0)
white = (255,255,255)
green = (0, 201, 47)
red = (255,0,0)
X = "X"
O = "O"
current_board = None

current_player = X
def createBoards():
    boards = [[Board() for i in range(3)] for j in range(3)]
    master_board = Board()
    return boards, master_board

def is_click_on_board (x,y):
    return x >= 0 and x < 900 and y >= 0 and y < 900
        
def is_new_game_clicked (x,y):
    return x >= 350 and x < 555 and y >= 935 and y < 970

def print_game_info(x, y):
    font = pygame.font.SysFont('chalkduster', 32)
    text = font.render('Current Player: ' + current_player, True, white, blue)
    text_button = font.render('New Game ', True, white, blue)
    textRect = text.get_rect()
    text_buttonRect = text_button.get_rect()
    textRect.center = (master_board_width / 2 + x, y + 20)
    game.blit(text, textRect)
    text_buttonRect.center = (master_board_width / 2 + x, y + 50)
    game.blit(text_button, text_buttonRect)

def print_board( x, y, width,color):
    pygame.draw.line(game,(color),(x+1/3*width,y),(x+1/3*width,y+width),10)
    pygame.draw.line(game,(color),(x+2/3*width,y),(x+2/3*width,y+width),10)
    pygame.draw.line(game,(color),(x,y+1/3*width),(x+width,y+1/3*width),10)
    pygame.draw.line(game,(color),(x,y+2/3*width),(x+width,y+2/3*width),10)


def draw_x(x, y, width, thickness,color):
    width = width-10
    pygame.draw.line(game,(color),(x,y),(x+width,y+width),thickness)
    pygame.draw.line(game,(color),(x+width,y),(x,y+width),thickness)

    
def draw_o(x, y, width, thickness,color):
    width = 1/2*width
    pygame.draw.circle(game,color,(x+width,y+width),width,8)

def draw_square(x,y,width,color):
    pygame.draw.line(game,(color),(x,y),(x+width,y),10)
    pygame.draw.line(game,(color),(x,y),(x,y+width),10)
    pygame.draw.line(game,(color),(x+width,y),(x+width,y+width),10)
    pygame.draw.line(game,(color),(x,y+width),(x+width,y+width),10) 
    
def print_selection( symbol, x, y):
    pass


def get_board_coordinate_from_x_y(x, y):
    game_width = master_board_width / 3
    square_width = game_width / 3
    board_x = math.floor(x/game_width)
    board_y = math.floor(y/game_width)
    square_x = math.floor((x - board_x * game_width)/square_width)
    square_y = math.floor((y - board_y * game_width)/square_width)
    return (board_x, board_y), (square_x, square_y)


def get_top_left_from_board_square_coords(board_coords, square_coords):
    game_width = master_board_width / 3
    square_width = game_width / 3
    square_x = board_coords[0] * game_width + square_coords[0] * square_width
    square_y = board_coords[1] * game_width + square_coords[1] * square_width
    return (square_x, square_y)

def get_top_left_from_board_coord(x, y):
    x_coord = math.floor(x*(master_board_width/3))
    y_coord = math.floor(y*(master_board_width/3))
    return (x_coord,y_coord)

def prompt_player_names():
    cpu = input ("would you like to play a computer? ")
    player_x = input  ("player X please type in your name ")
    player_o = input ("player O please type your name (type CPU for computer)")
    if cpu == "y" or cpu == "yes":
        mode = input ("would you like to play an easy CPU or hard CPU?")
    return player_x, player_o

boards, master_board = createBoards() 
view = View()
controller = BoardController(master_board, boards, view)


#player_x, player_o = prompt_player_names()
current_player = X
for i in range(0, master_board_width, int(master_board_width / 3)):
    for j in range(0, master_board_width, int(master_board_width / 3)):

        print_board( i+10, j+10, 280,blue)

print_board(0, 0, 900,black)
last_play = False


continue_game = True
while continue_game:
    ev = pygame.event.get()

    for event in ev:
        # handle MOUSEBUTTONUP
        if event.type == pygame.QUIT:
            continue_game = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            print (pos)
            click_x = pos[0]
            click_y = pos[1]
            if not is_click_on_board(click_x,click_y):
                if not is_new_game_clicked(click_x, click_y):
                    continue
                game = pygame.display.set_mode([master_board_width,1000])
                game.fill((245,175,255))
                for i in range(0, master_board_width, int(master_board_width / 3)):
                    for j in range(0, master_board_width, int(master_board_width / 3)):
                        print_board( i+10, j+10, 280,blue)

                print_board(0, 0, 900,black)
                #player_x, player_y = prompt_player_names()
                current_player = X
                last_play = False
                continue
            pos = pygame.mouse.get_pos()
            board_coord, square_coord = get_board_coordinate_from_x_y(pos[0], pos[1])
            selected_board = boards[board_coord[0]][board_coord[1]]
            print("Current: ", current_board)
            print("Board: ", board_coord)
            if current_board != None and (current_board[0] != board_coord[0] or current_board[1] != board_coord[1]):
                continue
            success = selected_board.play(current_player, square_coord[0], square_coord[1])
            if not success:
                print("not success")
                continue           
            winner = selected_board.check_winner()
            print("winner: " + str(winner))
            (x, y) = get_top_left_from_board_coord(board_coord[0], board_coord[1])
            width = 300
            draw_square(x,y,width,black)
            draw_square(0,0,900,purple)

            if winner == X or winner == O:
                if winner == O:
                    draw_o(x, y, width, 15, white)
                if winner == X:
                    draw_x(x, y, width, 15, black)
                master_board.play(winner,board_coord[0],board_coord[1])
                master_winner = master_board.check_winner()
                if master_winner != False:
                    print("master_winner")
                    print(master_winner)
                    continue_game = False
            current_board = square_coord
            if master_board.get_symbol_at_coord(square_coord[0], square_coord[1]):
                current_board = None
            if current_board is not None:
                (x, y) = get_top_left_from_board_coord(current_board[0], current_board[1])
                draw_square(x,y,width,green)
            print(board_coord, square_coord)
            print_selection("x", pos[0], pos[1])
            top_left = get_top_left_from_board_square_coords(board_coord, square_coord)
            if current_player == X:
                draw_x(top_left[0], top_left[1], small_board_width / 3, 8,red)
                current_player = O
                last_coord_x_x = top_left[0]
                last_coord_y_x = top_left[1]
                if last_play:
                    print("play o")
                    draw_o(last_coord_x_o, last_coord_y_o, small_board_width / 3, 8,white)
                last_play = True
                    
            elif current_player == "CPU":
                cpu_x = random.randint(0,2)
                cpu_y = random.randint(0,2)
                square_coords = (cpu_x.cpu_y)
                board_coord = board_coord[0], board_coord[1]
                coord = get_top_left_from_board_square_coords(square_coords,board_coord)
                draw_o (coord[0],coord[1],small_board_width/3,8,red)
                last_coord_x_o = coord[0]
                last_coord_y_o = coord[1]
                current_player = player_x
                if last_play:
                    draw_x(last_coord_x_x, last_coord_y_x, small_board_width / 3, 8,black)
                last_play=True
            
            else:
                draw_o(top_left[0], top_left[1], small_board_width / 3, 8,red)
                current_player = X
                last_coord_x_o = top_left[0]
                last_coord_y_o = top_left[1]
                if last_play:
                    print("play o")
                    draw_x(last_coord_x_x, last_coord_y_x, small_board_width / 3, 8,black)
                last_play = True

            print(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                continue_game = False
    print_game_info(0, 900)
    pygame.display.flip()

pygame.quit()
