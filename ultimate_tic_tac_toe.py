import pygame
import Board
import math

pygame.init()
master_board_width = 900
small_board_width = 280
game = pygame.display.set_mode([master_board_width,1000])
game.fill((245,175,255))
blue = (0,43,255)
black = (0,0,0)
white = (255,255,255)
X = "X"
O = "O"
current_player = X
boards = [[Board.Board() for i in range(3)] for j in range(3)]
current_board = None
master_board = Board.Board()

def print_game_info(x, y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Current Player: ' + current_player, True, white, blue)
    textRect = text.get_rect()
    textRect.center = (master_board_width / 2 + x, y + 20)
    game.blit(text, textRect)

def print_board( x, y, width,color):
    pygame.draw.line(game,(color),(x+1/3*width,y),(x+1/3*width,y+width),10)
    pygame.draw.line(game,(color),(x+2/3*width,y),(x+2/3*width,y+width),10)
    pygame.draw.line(game,(color),(x,y+1/3*width),(x+width,y+1/3*width),10)
    pygame.draw.line(game,(color),(x,y+2/3*width),(x+width,y+2/3*width),10)


def draw_x(x, y, width, thickness):
    width = width-10
    pygame.draw.line(game,(black),(x,y),(x+width,y+width),thickness)
    pygame.draw.line(game,(black),(x+width,y),(x,y+width),thickness)

    
def draw_o(x, y, width, thickness):
    width = 1/2*width
    pygame.draw.circle(game,white,(x+width,y+width),width,8)

    
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
    

for i in range(0, master_board_width, int(master_board_width / 3)):
    for j in range(0, master_board_width, int(master_board_width / 3)):

        print_board( i+10, j+10, 280,blue)

print_board(0, 0, 900,black)


continue_game = True

while continue_game:
    ev = pygame.event.get()

    for event in ev:
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
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
            current_board = square_coord
            winner = selected_board.check_winner()
            print("winner: " + str(winner))
            if winner == X or winner == O:
                if winner == O:
                    x = math.floor(board_coord[0]*(master_board_width/3))
                    y = math.floor(board_coord[1]*(master_board_width/3))
                    width = 300
                    draw_o(x, y, width, 15)
                if winner == X:
                    x = math.floor(board_coord[0]*(master_board_width/3))
                    y = math.floor(board_coord[1]*(master_board_width/3))
                    width = 300
                    draw_x(x, y, 300, 15)
                master_board.play (winner,board_coord[0],board_coord[1] )
                master_winner = master_board.check_winner()
                
                if master_winner != False:
                    print("master_winner")
                    print(master_winner)
                    continue_game = False
            print(board_coord, square_coord)
            print_selection("x", pos[0], pos[1])
            top_left = get_top_left_from_board_square_coords(board_coord, square_coord)
            if current_player == X:
                draw_x(top_left[0], top_left[1], small_board_width / 3, 8)
                current_player = O
            else:
                draw_o(top_left[0], top_left[1], small_board_width / 3, 8)
                current_player = X
            print(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                continue_game = False
    print_game_info(0, 900)
    pygame.display.flip()

pygame.quit()
