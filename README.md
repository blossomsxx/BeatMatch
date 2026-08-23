# BeatMatch

A 2D rhythm game rebuilt in Visual Studio Code using Python's pygame library.

# Overview

BeatMatch is a rhythm game where players press the corresponding
keys (A, S, K, and L) as falling beats reach their targets.

The original version was created in CMU CS Academy. I am independently rebuilding
and expanding the project in Pygame using Visual Studio Code to learn a more
flexible game-development framework and strengthen my Python and object-oriented programming skills.

# Current Features

- 4-lane rhythm game layout
- Keyboard input using A, S, K, and L
- Dynamically created Beat objects
- Pygame Sprite classes and Sprite groups 
- Smooth downward Beat movement
- Timed Beat spawning
- Randomized Beat patterns
- Multiple Beats can spawn simultaneously
- Hit detection based on Beat proximity to targets
- Hit and miss tracking
- Win condition at 50 hits
- Loss condition at 50 misses
- In-game hit/miss score display
- Win and game-over screens
- Beats are removed after successful hits 
- Beats are removed when they reach the bottom of the screen (after a miss)
- Custom game graphics
- Event-driven game loop
- Frame-rate control using Pygame Clock

# Tools

- Python
- Pygame
- Visual Studio Code

# What I Learned

- Pygame game loops
- Event-driven programming
- Sprite classes and sprite groups
- Surfaces and images
- Rectangles and sprite positioning
- Object-oriented programming
- Keyboard event handling
- Collision/proximity detection
- Frame-rate control
- Timed object spawning
- Randomized game events
- Managing multiple game objects
- Game state management
- Translating a project from one programming framework to another

# Technical Highlights
- Designed a reusable `Beat` class using object-oriented programming.
- Used Pygame Sprite Groups to manage multiple falling objects.
- Implemented an event-driven game loop for keyboard input and game updates.
- Created randomized Beat spawning patterns using Python's `random` module.
- Implemented hit detection using positional distance checks.
- Implemented game-state management using win/loss conditions and Boolean state.
- Used modular helper functions for score tracking, label creation, and game states.
- Controlled animation timing and movement using Pygame's Clock and frame rate.

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
   
