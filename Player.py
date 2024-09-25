from Settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game  # Store the game instance for access to game components
        self.x, self.y = PLAYER_POS  # Initialize player's position from settings
        self.angle = PLAYER_ANGLE  # Initialize player's facing angle from settings

    def movement(self):
        # Calculate the player's movement based on input
        sin_a = math.sin(self.angle)  # Sine of the current angle for movement calculation
        cos_a = math.cos(self.angle)  # Cosine of the current angle for movement calculation
        dx, dy = 0, 0  # Initialize change in position
        speed = PLAYER_SPEED * self.game.delta_time  # Calculate speed based on frame time
        speed_sin = speed * sin_a  # Speed in the y direction
        speed_cos = speed * cos_a  # Speed in the x direction

        keys = pg.key.get_pressed()  # Get the state of all keyboard keys
        num_key_pressed = -1  # Initialize key press counter
        if keys[pg.K_w]:  # Move forward
            num_key_pressed += 1
            dx += speed_cos  # Update change in x
            dy += speed_sin  # Update change in y
        if keys[pg.K_s]:  # Move backward
            num_key_pressed += 1
            dx += -speed_cos  # Update change in x
            dy += -speed_sin  # Update change in y
        if keys[pg.K_a]:  # Strafe left
            num_key_pressed += 1
            dx += speed_sin  # Update change in x (rotate left)
            dy += -speed_cos  # Update change in y (rotate left)
        if keys[pg.K_d]:  # Strafe right
            num_key_pressed += 1
            dx += -speed_sin  # Update change in x (rotate right)
            dy += speed_cos  # Update change in y (rotate right)

        self.check_wall_collision(dx, dy)  # Check for wall collisions before moving

        # Rotate the player based on left/right key presses
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time  # Rotate left
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time  # Rotate right
        self.angle %= math.tau  # Keep the angle within [0, 2π]

    def check_wall(self, x, y):
        # Check if a position (x, y) is not a wall
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        # Check for wall collisions before moving
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx  # Move in x direction if there's no wall
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy  # Move in y direction if there's no wall

    def draw(self):
        # Draw the player as a green circle on the screen
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        # Update the player's state
        self.movement()  # Call movement method to handle input

    @property
    def pos(self):
        # Return the player's position as a tuple
        return self.x, self.y

    @property
    def map_pos(self):
        # Return the player's position in the map grid as a tuple of integers
        return int(self.x), int(self.y)
