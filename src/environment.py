import pygame
import random
import numpy as np
from enum import Enum
from collections import namedtuple
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

pygame.init()
font = pygame.font.SysFont('arial', 25)
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

class SnakeGameAI:
    
    def __init__(self, w=config.SCREEN_WIDTH, h=config.SCREEN_HEIGHT):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Autonomous Nav Agent')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-config.BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*config.BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0 
        
    def _place_food(self):
        x = random.randint(0, (self.w-config.BLOCK_SIZE )//config.BLOCK_SIZE )*config.BLOCK_SIZE 
        y = random.randint(0, (self.h-config.BLOCK_SIZE )//config.BLOCK_SIZE )*config.BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()
    def play_step(self, action):
        self.frame_iteration += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        self._move(action) 
        self.snake.insert(0, self.head)
        
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score
            
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()
        
        self._update_ui()
        self.clock.tick(config.SPEED)
        
        return reward, game_over, self.score

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        
        # Check boundary collision
        if pt.x > self.w - config.BLOCK_SIZE or pt.x < 0 or pt.y > self.h - config.BLOCK_SIZE or pt.y < 0:
            return True
        
        # Check self collision
        if pt in self.snake[1:]:
            return True
        return False

    def _update_ui(self):
        self.display.fill(config.BLACK)
        
        for pt in self.snake:
            pygame.draw.rect(self.display, config.BLUE1, pygame.Rect(pt.x, pt.y, config.BLOCK_SIZE, config.BLOCK_SIZE))
            pygame.draw.rect(self.display, config.BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
            
        pygame.draw.rect(self.display, config.RED, pygame.Rect(self.food.x, self.food.y, config.BLOCK_SIZE, config.BLOCK_SIZE))
        
        text = font.render("Score: " + str(self.score), True, config.WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def _move(self, action):
        # Action: [straight, right, left]
        
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)
        
        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # Right turn
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # Left turn
            
        self.direction = new_dir
        
        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += config.BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= config.BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += config.BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= config.BLOCK_SIZE
            
        self.head = Point(x, y)