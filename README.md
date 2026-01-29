# Autonomous Navigation Agent using Deep Q-Networks 

An autonomous AI agent that learns to navigate a constrained environment (Snake) using **Reinforcement Learning**. 
Built from scratch using **Python** and **PyTorch**, implementing a Deep Q-Network (DQN) with Experience Replay.

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-orange)

##  Key Features 
* **Deep Q-Network (DQN):** Implements a neural network (Linear Layers + ReLU) to predict the optimal action (Q-value) for any given state.
* **Experience Replay:** Utilizes a `deque` buffer to store past 100,000 moves, training on random mini-batches to break data correlation and stabilize learning.
* **Epsilon-Greedy Strategy:** Balances exploration (random moves) and exploitation (AI moves) with an adaptive decay rate.
* **Bellman Equation:** Optimizes future rewards using the Q-Learning formula:
    $$Q_{new} = R + \gamma \cdot \max(Q_{next})$$
* **Live Analytics:** Real-time Matplotlib dashboard tracking Loss, Mean Score, and Record performance.

## Tech Stack
* **Core Logic:** Python 3.x
* **ML Framework:** PyTorch (Torch + TorchVision)
* **Simulation:** Pygame
* **Data Processing:** NumPy
* **Visualization:** Matplotlib / IPython

How to Run Locally:-

1. clone the repo in terminal
2. create virtual environment
3. install dependencies
``` python main.py ```
4. launch the agent
``` python main.py ```

Performance:

-> 0 - 50 Games: Exploration phase (High crashes).

-> 50 - 100 Games: Pattern recognition begins.

-> 100+ Games: The agent develops optimal pathing strategies, averaging scores of 40+.


