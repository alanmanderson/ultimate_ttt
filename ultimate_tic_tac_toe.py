import pygame
from Board import Board
from BoardController import BoardController
from View import View

def check_for_backspace (key_event):
    return event.key == pygame.K_BACKSPACE

def createBoards():
    boards = [[Board() for i in range(3)] for j in range(3)]
    master_board = Board()
    return boards, master_board

boards, master_board = createBoards() 
view = View()
controller = BoardController(master_board, boards, view)
controller.setup_boards()
close_game = False

while not close_game:
    events = pygame.event.get()
    for event in events:
        # handle MOUSEBUTTONUP
        if event.type == pygame.QUIT:
            close_game = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            controller.handle_left_click_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                close_game = True
    controller.update_view()
    if controller.is_game_over():
        pass
pygame.quit()
