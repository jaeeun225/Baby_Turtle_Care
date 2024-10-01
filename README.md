# Baby Turtle Care Game 🐢

## Overview

**Baby Turtle Care** is an interactive game where players control a "caring turtle" tasked with keeping two baby turtles safe. It's dangerous outside, so make sure the baby turtles stay in a safe area and take good care of it so that it doesn't get hurt! 🌳❤️

## Features

- 🐢 **Turtle Characters**:

  - Two baby turtles that move randomly.
  - A caring turtle that the player controls.

- 🎮 **Gameplay Mechanics**:

  - The caring turtle must catch the baby turtles before they go out of bounds.
  - If the caring turtle goes outside before the end of working hours, it goes back to its initial position.
  - When the working hours end, the player will receive their level of care.

- 📊 **Score Tracking**:

  - If the player catches the baby turtle before it goes out of bounds, it will return to its initial position, and the player's level of care goes up.
  - If a baby turtle goes outside, it will return to its initial position, and the player's level of care goes down.

- ⏱️ **Timer**:

  - The task of taking care of the baby turtle is 60 seconds.

## Controls

- The caring turtle can be controlled using the keyboard:
  - **Up Arrow**: Move Forward ⬆️
  - **Down Arrow**: Move Backward ⬇️
  - **Left Arrow**: Turn Left ⬅️
  - **Right Arrow**: Turn Right ➡️

## Game Objective

- Ensure the baby turtles remain within the safe area and do not venture outside.
- Monitor the remaining time and aim to maximize your caring level by catching the baby turtles.

## Development

This game is built using Python's `turtle` and `tkinter` libraries.

## Game Execution Screen

1. Start Screen

   <img src="game_execution_screen/start_screen.JPG" alt="start_screen" width="300">

2. When the baby turtle goes out

   <img src="game_execution_screen/baby_goes_out.JPG" alt="baby_goes_out" width="300">

3. When the caring turtle goes out

   <img src="game_execution_screen/caregiver_goes_out.JPG" alt="caregiver_goes_out" width="300">

4. When you get the high level on result

   <img src="game_execution_screen/high_level.JPG" alt="high_level" width="300">

5. When you get the low level on result

   <img src="game_execution_screen/low_level.JPG" alt="low_level" width="300">
