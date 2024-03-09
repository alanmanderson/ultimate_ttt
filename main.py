import asyncio
from GameController import GameController

async def main():
    game_controller = GameController()
    game_controller.init()

    while not game_controller.close_game:
        game_controller.run_event_loop()
        game_controller.update_ui()
        await asyncio.sleep(0)

asyncio.run(main())
