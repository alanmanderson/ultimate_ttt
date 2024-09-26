import pygame as pg

class Event:
    BOARD_CLICK_EVENT = pg.event.custom_type()
    MENU_CLICK_EVENT = pg.event.custom_type()
    RESTART_GAME_EVENT = pg.event.custom_type()
    SAVE_GAME_EVENT = pg.event.custom_type()
    LOAD_GAME_EVENT = pg.event.custom_type()
    QUIT_GAME_EVENT = pg.event.custom_type()
    NEXT_PLAYER_EVENT = pg.event.custom_type()
    PLAY_EVENT = pg.event.custom_type()
