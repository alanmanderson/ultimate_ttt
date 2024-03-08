class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_ui(self):
        self.view.update()

    def handle_event(self, event):
        raise NotImplementedError
