import pygame as pg
from Controller import Controller
from MenuView import MenuView
from Event import Event

class MenuController(Controller):

    def __init__(self, view: MenuView):
        self.view = view

    def update_ui(self):
        self.view.update()

    def handle_event(self, event):
        if event.type == Event.MENU_CLICK_EVENT:
            if event.pos[0] < 100:
                self._click_restart()
            elif event.pos[0] < 200:
                self._click_quit()

    def _click_restart(self):
        e = pg.event.Event(Event.RESTART_GAME_EVENT, {})
        pg.event.post(e)

    def _click_quit(self):
        e = pg.event.Event(Event.QUIT_GAME_EVENT, {})
        pg.event.post(e)
