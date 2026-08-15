# Countdown Clock and Timer

A simple Python command-line program that counts down from a
user-given time (minutes and seconds) and alerts the user once the
time is up.

## Course Details

- **Subject:** Python Programming Language (N-PCCCM304P)
- **Assessment:** Experiential Learning – Project Assessment
- **Department:** CSE (AI & ML)
- **Session:** 2026-27 (ODD)
- **Author:** Amit Gajanan Japulkar

## Problem Statement

We often need to track a fixed amount of time while studying,
exercising, cooking, presenting, or taking a short break. Watching a
clock manually is distracting, and a phone timer isn't always handy.
This program solves that with a lightweight countdown timer that runs
directly in the terminal.

## Features

- Accepts minutes and seconds as input
- Converts entered time into total seconds
- Displays the remaining time live, updating every second
- Decreases the timer by 1 second each cycle
- Plays a sound alert and shows **"Time's Up!"** when the timer ends
- Basic input validation (rejects negative numbers and invalid entries)

## How It Works (Algorithm)

1. Start the program
2. Take minutes and seconds as input from the user
3. Convert the input into total seconds (`minutes × 60 + seconds`)
4. Repeat while total seconds is greater than 0:
   - Display the remaining time in `MM:SS` format
   - Wait for 1 second
   - Decrease total seconds by 1
5. When total seconds reaches 0, play a sound alert
6. Display the message `"Time's Up!"`
7. Stop the program

## Python Concepts Used

- Variables
- `input()`
- `while` loop
- `if` condition
- Functions
- `time.sleep()`
- Basic exception handling (`try` / `except`)

## How to Run

```bash
python countdown_timer.py
```

You will be prompted to enter minutes and seconds, then the countdown
will start automatically.

## Requirements

- Python 3.x
- No external libraries needed (uses only the standard library)

## Project Status

This repository currently reflects **Phase I + Phase II** work
(problem understanding, logic design, and the working countdown
logic). Testing and deployment are planned for **Phase III**.

## Future Scope

- Graphical User Interface (GUI)
- Start / Pause / Resume / Reset buttons
- Custom sound options
- Support for multiple timers
- Stronger input validation
- Proper automated testing
- Deployment as a standalone/usable app

## Commit History (Suggested)

- Initial project setup
- Added countdown logic
- Added timer display
- Added sound alert
- Added input validation
- Updated README
