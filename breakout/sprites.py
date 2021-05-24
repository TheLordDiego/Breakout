import pygame
import math
import random

# colors
COLOR_DARKBLUE = (36, 90, 190)
COLOR_LIGHTBLUE = (0, 176, 240)


class Player:
    def __init__(self, screen_width):
        self.x = screen_width / 2.0
        self.y = 700
        self.dx = 0
        self.width = 200
        self.height = 25
        self.score = 0

    def left(self):
        self.dx = - 12

    def right(self):
        self.dx = 12

    def move(self, screen_width):
        self.x = self.x + self.dx

        # Check for border collision
        if self.x < 0 + self.width / 2.0:
            self.x = 0 + self.width / 2.0
            self.dx = 0

        elif self.x > screen_width - self.width / 2.0:
            self.x = screen_width - self.width / 2.0
            self.dx = 0

    def render(self, screen, color):
        pygame.draw.rect(screen, color, pygame.Rect(int(self.x - self.width / 2.0), int(self.y - self.height / 2.0),
                                                    self.width, self.height))


class Ball:
    def __init__(self, screen_width, screen_height):
        self.x = screen_width / 2.0
        self.y = screen_height / 2.0
        self.dx = 0
        self.dy = 5
        self.width = 20
        self.height = 20

    def move(self, screen_width, screen_height):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        # Check for border collision
        if self.x < 0 + self.width / 2.0:
            self.x = 0 + self.width / 2.0
            self.dx *= - 1

        elif self.x > screen_width - self.width / 2.0:
            self.x = screen_width - self.width / 2.0
            self.dx *= - 1

        if self.y < 0 + self.height / 2.0:
            self.y = 0 + self.height / 2.0
            self.dy *= - 1

        elif self.y > screen_height - self.height / 2.0:
            self.y = screen_height - self.height / 2.0
            self.x = screen_width / 2.0
            self.y = screen_height / 2.0

    def render(self, screen, color):
        pygame.draw.rect(screen, color,
                         pygame.Rect(int(self.x - self.width / 2.0), int(self.y - self.height / 2.0), self.width,
                                     self.height))

    def collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)

        return x_collision and y_collision


class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 25
        self.color = random.choice([COLOR_DARKBLUE, COLOR_LIGHTBLUE])

    def render(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(int(self.x - self.width / 2.0),
                                                         int(self.y - self.height / 2.0), self.width, self.height))
