import pygame
from Controller import Controller
from Color import Color
import math
import random

class BoardController(Controller):
    master_board_width = 900
    X = "X"
    O = "O"
    CAT = "CAT"
    def __init__(self, master_board, boards, view):
        self.master_board = master_board
        self.boards = boards
        self.view = view
        self.game_over = False
        self.current_board = None
        self.current_player = BoardController.X
        self.previous_coord = None
        self.setup_boards()   # I don't want to do all this setup in the constructor but am doing it for now.

    def update_ui(self):
        self.update_view()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.handle_left_click_event(event)

    def setup_boards(self):
        #player_x, player_o = prompt_player_names()
        for i in range(0, BoardController.master_board_width, int(BoardController.master_board_width / 3)):
            for j in range(0, BoardController.master_board_width, int(BoardController.master_board_width / 3)):
                self.view.print_board(i, j, 300, Color.D_GREY)
        self.view.print_board(0, 0, 900, Color.L_GREY)
    
    def get_board_coordinate_from_x_y(self, x, y):
        game_width = BoardController.master_board_width / 3
        square_width = game_width / 3
        board_x = math.floor(x/game_width)
        board_y = math.floor(y/game_width)
        square_x = math.floor((x - board_x * game_width)/square_width)
        square_y = math.floor((y - board_y * game_width)/square_width)
        return (board_x, board_y), (square_x, square_y)


    def get_top_left_from_board_square_coords(self, board_coords, square_coords, x, y):
        game_width = BoardController.master_board_width / 3
        board_x = math.floor(x/game_width)
        board_y = math.floor(y/game_width)
        game_width = BoardController.master_board_width / 3
        square_width = game_width / 3
        square_x = board_coords[0] * game_width + square_coords[0] * square_width + 10 
        square_y = board_coords[1] * game_width + square_coords[1] * square_width + 10 
        return (square_x, square_y)

    def get_top_left_from_board_coord(self, x, y):
        x_coord = math.floor(x*(BoardController.master_board_width/3))
        y_coord = math.floor(y*(BoardController.master_board_width/3))
        return (x_coord,y_coord)

    def prompt_player_names(self, key_event, x,y):
        clock = pygame.time.Clock() 
        font = pygame.font.SysFont('chalkduster', 32)
        user_text = '' 
        input_rect = pygame.Rect(200, 200, 140, 32) 
        color_active = pygame.Color('lightskyblue3') 
        color_passive = pygame.Color('chartreuse4') 
        color = color_passive 
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if input_rect.collidepoint(event.pos): 
                    active = True
                else: 
                    active = False
            if event.type == pygame.KEYDOWN: 
                if check_for_backspace(event.key): 
                    user_text = user_text[:-1]
                else: 
                    user_text += event.unicode
        screen.fill((255, 255, 255)) 
        if active: 
            color = color_active 
        else: 
            color = color_passive 
        pygame.draw.rect(screen, color, input_rect) 
        text_surface = base_font.render(user_text, True, (255, 255, 255))  
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
        input_rect.w = max(100, text_surface.get_width()+10) 
        pygame.display.flip() 
        clock.tick(60)

    def is_game_over(self):
        return self.game_over

    def is_click_on_board (self, x,y):
        return x >= 0 and x < 900 and y >= 0 and y < 900
        
    def is_new_game_clicked (self, x,y):
        return x >= 350 and x < 555 and y >= 935 and y < 970

    def handle_left_click_event(self, event):
        small_board_width = 280
        pos = event.pos
        print (pos)
        click_x = pos[0]
        click_y = pos[1]

        if not self.is_click_on_board(click_x,click_y):
            return
        board_coord, square_coord = self.get_board_coordinate_from_x_y(pos[0], pos[1])
        selected_board = self.boards[board_coord[0]][board_coord[1]]
        if self.current_board != None and (self.current_board[0] != board_coord[0] or self.current_board[1] != board_coord[1]):
            return
        success = selected_board.play(self.current_player, square_coord[0], square_coord[1])
        if not success:
            print("not success")
            return           
        winner = selected_board.check_winner()
        print("winner: " + str(winner))
        (x, y) = self.get_top_left_from_board_coord(board_coord[0], board_coord[1])
        width = 300
        self.view.draw_square(x,y,width,Color.L_GREY)
        self.view.draw_square(0,0,900,Color.DARK_GREEN)
        
        if winner != False:
            if winner == self.O:
                self.view.draw_o(x, y, width, 15, Color.WHITE)
            if winner == self.X:
                self.view.draw_x(x, y, width, 15, Color.YELLOW)
            if winner == self.CAT:
                self.view.draw_cat(x+5, y+5, width-10)
            self.master_board.play(winner,board_coord[0],board_coord[1])
            master_winner = self.master_board.check_winner()
            if master_winner != False:
                print("master_winner")
                print(master_winner)
                self.game_over = True
            
        self.current_board = square_coord
        if self.master_board.get_symbol_at_coord(square_coord[0], square_coord[1]):
            self.current_board = None
        if self.current_board is not None:
            (x, y) = self.get_top_left_from_board_coord(self.current_board[0], self.current_board[1])
            self.view.draw_square(x,y,width, Color.GREEN)
        print(board_coord, square_coord)
        top_left = self.get_top_left_from_board_square_coords(board_coord, square_coord, click_x, click_y)

        if self.current_player == self.X:
            self.view.draw_x(top_left[0], top_left[1], small_board_width / 3 - 10, 8, Color.RED)
            self.current_player = self.O
            if self.previous_coord is not None:
                self.view.draw_o(self.previous_coord[0], self.previous_coord[1] , small_board_width / 3 - 10, 8, Color.WHITE)
            self.previous_coord = (top_left[0], top_left[1])
                
##        Nice Try, but this doesn't quite work yet
##        elif self.current_player == "CPU":
##            cpu_x = random.randint(0,2)
##            cpu_y = random.randint(0,2)
##            square_coords = (cpu_x.cpu_y)
##            board_coord = board_coord[0], board_coord[1]
##            coord = self.get_top_left_from_board_square_coords(square_coords,board_coord)
##            self.view.draw_o (coord[0],coord[1] + 10 ,small_board_width/3,8, Color.RED)
##            last_coord_x_o = coord[0]
##            last_coord_y_o = coord[1] + 10 
##            self.current_player = player_x
##            if self.previous_coord is not None:
##                self.view.draw_x(last_coord_x_x, last_coord_y_x, small_board_width / 3 - 10, 8, Color.BLACK)
        
        else:
            self.view.draw_o(top_left[0], top_left[1] , small_board_width / 3 - 10, 8, Color.RED)
            self.current_player = self.X
            if self.previous_coord is not None:
                self.view.draw_x(self.previous_coord[0], self.previous_coord[1], small_board_width / 3 - 10, 8, Color.YELLOW)
            self.previous_coord = (top_left[0], top_left[1])


    def update_view(self):
        self.view.handle_mouse_pos()
        self.view.print_game_info(self.current_player)
        self.view.update()

    def save_game(self):
        pass
