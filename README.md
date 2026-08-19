# BeatMatch

A 2D rhythm game rebuilt in Visual Studio Code using Python's pygame library.

# Overview

BeatMatch is a rhythm game where players press the corresponding
keys (askl) as falling beats reach their targets.

The original version was created in CMU CS Academy. I am independently rebuilding
and expanding the project independently in VS Code's Pygame to learn a more
flexible game-development framework and strengthen my Python skills.

# Current Features

- 4-lane rhythm game layout
- Keyboard input using A, S, K, and L
- Dynamically created Beat objects
- Pygame Sprite classes and Sprite groups 
- Smooth downward Beat movement
- Timed Beat spawning
- Randomized Beat patterns
- Multiple Beats can spawn simultaneously
- Beats are removed when they reach the bottom of the screen
- Custom game graphics
- Win screen
- Event-driven game loop
- Frame-rate control using Pygame Clock

# In Progress

- Hit/miss detection
- Score tracking
- Win/lose conditions
- In-game UI
- Difficulty progression

# Technologies

- Python
- Pygame

# What I Learned

- Pygame game loops
- Event-driven programming
- Sprite classes and sprite groups
- Surfaces and images
- Rectangles and sprite positioning
- Object-oriented programming
- Frame-rate control
- Timed object spawning
- Randomized game events
- Managing multiple game objects
- Translating a project from one programming framework to another

# Project Evolution

This project was originally developed from scratch in CMU CS Academy
using Python and course lessons. I am independently rebuilding and
expanding it in Pygame to improve my understanding of Python,
object-oriented programming, game loops, sprite management, and game architecture.

The Pygame version is being developed incrementally rather than directly
copying the original implementation. I am translating each feature into
Pygame and adapting it to Pygame's Sprite and event systems.

# Planned Improvements

- Add a start screen
- Add sound effects/music
- Add difficulty progression
- Improve hit feedback
- Add restart functionality

# How to Run

1. Clone or download the repository.
2. Make sure Python is installed.
3. Install Pygame:

   ```bash
   pip install pygame
4. Open project in Visual Studio Code.
5. Run the main Python file:

   ```bash
   python BeatMatch.py
   
