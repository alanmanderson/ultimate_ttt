from GameController import GameController

game_controller = GameController()
game_controller.generateControllers()

while not game_controller.close_game:
    game_controller.run_event_loop()
    game_controller.update_ui()
