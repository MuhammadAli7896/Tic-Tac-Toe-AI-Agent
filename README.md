# Tic Tac Toe with AI

A Python implementation of Tic Tac Toe with AI opponents using the Minimax algorithm and Alpha-Beta Pruning optimization.

## Features

- Play Tic Tac Toe against an unbeatable AI opponent
- Toggle between two AI algorithms:
  - Basic Minimax algorithm
  - Optimized Alpha-Beta Pruning algorithm
- Visual game interface using Pygame
- Performance statistics displayed in the console

## Requirements

- Python 3.6+
- Pygame library

## Installation

1. Clone this repository or download the source files
2. Install the required dependency:
   ```
   pip install pygame
   ```

## Project Structure

The game consists of four Python files:

- `game.py`: Main game loop and interface
- `board.py`: Game board representation and logic
- `minimax_agent.py`: Basic Minimax AI implementation
- `alphabeta_agent.py`: Optimized Alpha-Beta Pruning AI implementation

## How to Play

1. Run the game:
   ```
   python game.py
   ```

2. Game Controls:
   - Click on any empty cell to place your mark (X)
   - Press 'R' to restart the game
   - Press 'T' to toggle between AI algorithms

## AI Algorithms

### Minimax

The Minimax algorithm works by:
- Recursively exploring all possible game states
- Evaluating each position by assuming optimal play from both sides
- Selecting the move that maximizes the AI's minimum guaranteed score

### Alpha-Beta Pruning

Alpha-Beta Pruning optimizes the Minimax algorithm by:
- Maintaining alpha (best score for maximizer) and beta (best score for minimizer) bounds
- Skipping evaluation of moves that cannot influence the final decision
- Providing the same optimal play as Minimax but with improved performance

## Performance Comparison

Alpha-Beta Pruning typically provides:
- 5-10x speedup for the opening move
- 2-4x speedup for mid-game positions
- Both algorithms provide optimal play (the AI is unbeatable)

## Implementation Details

- The game uses a 3x3 grid
- Player plays as X (moves first)
- AI plays as O
- Console output shows AI thinking time for performance comparison
- Game messages display when a player wins or the game ends in a tie

## Credits

Created as a demonstration of game AI techniques using the Minimax algorithm and its optimization through Alpha-Beta Pruning.
