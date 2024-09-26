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
            self.handle_click(event)

    def handle_click(self, event):
        for item in self.view.menu_rects:
            if self.view.menu_rects[item].collidepoint(event.pos):
                if item == "Restart":
                    self._click_restart()
                elif item == "Save":
                    self._click_save()
                elif item == "Load":
                    self._click_load()
                elif item == "Quit":
                    self._click_quit()
         

    def _click_restart(self):
        e = pg.event.Event(Event.RESTART_GAME_EVENT, {})
        pg.event.post(e)


    def _click_save(self):
        e = pg.event.Event(Event.SAVE_GAME_EVENT, {})
        pg.event.post(e)


    def _click_load(self):
        fn = self.prompt_file()
        e = pg.event.Event(Event.LOAD_GAME_EVENT, {'fn': fn})
        pg.event.post(e)


    def _click_quit(self):
        e = pg.event.Event(Event.QUIT_GAME_EVENT, {})
        pg.event.post(e)

    def prompt_file(self):
        file_name = "games/X_O_IP_1710980833.ttt"
        return file_name
