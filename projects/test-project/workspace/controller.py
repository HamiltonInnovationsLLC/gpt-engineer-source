import pygame
import random
from model import Snake, Food, Point
from view import GameView

class GameController:
    def __init__(self):
        self.snake = Snake(Point(10, 10), 3)
        self.food = Food(self.generate_food_position())
        self.view = GameView(self.snake, self.food, (640, 480), 20)

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_keydown(event.key)

            self.snake.move()
            self.check_collision()
            self.view.draw()
            clock.tick(10)

        self.view.quit()

    def handle_keydown(self, key):
        if key == pygame.K_UP:
            self.snake.change_direction(Point(0, -1))
        elif key == pygame.K_DOWN:
            self.snake.change_direction(Point(0, 1))
        elif key == pygame.K_LEFT:
            self.snake.change_direction(Point(-1, 0))
        elif key == pygame.K_RIGHT:
            self.snake.change_direction(Point(1, 0))

    def check_collision(self):
        head = self.snake.body[0]
        if head == self.food.position:
            self.snake.grow()
            self.food.position = self.generate_food_position()

    def generate_food_position(self):
        return Point(random.randint(0, 31), random.randint(0, 23))
