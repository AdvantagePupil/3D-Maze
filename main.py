import pygame as pg
import sys
from Settings import *
from Map import *
from Player import *
from raycastin import *
from object_rendering import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self) # Initialize the map
        self.player = Player(self) # Initialize the player
        self.object_renderer = ObjectRenderer(self) # Initialize the object renderer
        self.raycasting = RayCasting(self) # Initialize the raycasting for visibility

    def update(self):
        self.player.update() # Update player position and state
        self.raycasting.update() # Update raycasting for rendering
        pg.display.flip() # Update the full display Surface to the screen
        self.delta_time = self.clock.tick(FPS) # Cap the frame rate and get the time since the last frame
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}') # Set the window title to display current FPS

    def draw(self):
        # Clear the screen and draw all elements
        self.screen.fill('black') # Fill the screen with black before drawing
        self.object_renderer.draw() # Render objects in the scene

    def check_events(self):
        # Handle user input and events
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit() # Quit Pygame
                sys.exit() # Exit the program

    def run(self):
        # Main game loop
        while True:
            self.check_events() # Check for user input and events
            self.update() # Update the game state
            self.draw() # Draw the updated state to the screen


if __name__ == '__main__':
    game = Game() # Create a Game instance
    game.run() # Start the game loop