from Controller import Controller
from GameInfoView import GameInfoView

class GameInfoController(Controller):

    def __init__(self, view: GameInfoView):
        self.view = view

    def update_ui(self):
        pass

    def handle_event(self, event):
        pass
