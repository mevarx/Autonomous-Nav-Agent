from src.environment import SnakeGameAI
import random

game = SnakeGameAI()

while True:
    action = [0, 0, 0]
    action[random.randint(0, 2)] = 1
    
    reward, done, score = game.play_step(action)
    print(f"Reward: {reward} | Score: {score}")
    
    if done:
        game.reset()
