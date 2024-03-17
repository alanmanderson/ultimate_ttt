import pygame as pg

class Event:
    BOARD_CLICK_EVENT = pg.event.custom_type()
    MENU_CLICK_EVENT = pg.event.custom_type()
    RESTART_GAME_EVENT = pg.event.custom_type()
    QUIT_GAME_EVENT = pg.event.custom_type()
    UPDATE_CURRENT_PLAYER_EVENT = pg.event.custom_type()
