from Controller import Controller
from MenuView import MenuView

class MenuController(Controller):

    def __init__(self, view: MenuView):
        self.view = view

    def update_ui(self):
        self.view.update()

    def handle_event(self, event):
        pass
