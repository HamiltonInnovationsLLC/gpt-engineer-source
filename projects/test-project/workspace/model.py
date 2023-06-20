from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

class Snake:
    def __init__(self, initial_position: Point, initial_length: int):
        self.body = [initial_position] * initial_length
        self.direction = Point(1, 0)

    def move(self):
        head = self.body[0]
        new_head = Point(head.x + self.direction.x, head.y + self.direction.y)
        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, new_direction: Point):
        self.direction = new_direction

    def grow(self):
        self.body.append(self.body[-1])

class Food:
    def __init__(self, position: Point):
        self.position = position
