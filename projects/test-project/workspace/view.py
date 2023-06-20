import pygame
from model import Snake, Food

class GameView:
    def __init__(self, snake: Snake, food: Food, screen_size: tuple, block_size: int):
        pygame.init()
        self.snake = snake
        self.food = food
        self.screen = pygame.display.set_mode(screen_size)
        self.block_size = block_size

    def draw(self):
        self.screen.fill((0, 0, 0))
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (255, 255, 255), (segment.x * self.block_size, segment.y * self.block_size, self.block_size, self.block_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.food.position.x * self.block_size, self.food.position.y * self.block_size, self.block_size, self.block_size))
        pygame.display.flip()

    def quit(self):
        pygame.quit()
