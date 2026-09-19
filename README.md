# ⏰ Smart Countdown Clock & Timer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Project-Experiential%20Learning-purple?style=for-the-badge" alt="Experiential Learning">
  <img src="https://img.shields.io/badge/Phase-02-orange?style=for-the-badge" alt="Phase 2">
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <b>A simple, practical and modular Python-based Countdown Clock & Timer</b>
</p>

<p align="center">
  Developed as an Experiential Learning Project for<br>
  <b>Python Programming Language (N-PCCCM304P)</b>
</p>

---

## 👨‍💻 Project Information

| Details | Information |
|---|---|
| 👨‍🎓 **Author** | Amit Gajanan Japulkar |
| 🆔 **USN** | CM25005 |
| 📚 **Course** | Python Programming Language (N-PCCCM304P) |
| 🏫 **Department** | CSE (AI & ML) |
| 📅 **Session** | 2026-27 (ODD) |
| 📌 **Project** | Countdown Clock and Timer |
| 🚀 **Current Phase** | Phase II |
| 💻 **Platform** | Windows |
| 🐍 **Language** | Python |

---

# 📖 About the Project

**Smart Countdown Clock & Timer** is a Python command-line application
developed to provide a simple and practical way to track a fixed
amount of time.

The application allows the user to select a predefined timer or
enter a custom duration. The timer then counts down in real time,
displays the remaining time and progress, and produces an audible
alarm when the countdown reaches zero.

The project was initially developed during **Phase I** and is being
improved during **Phase II** while retaining the original project
concept and functionality.

---

# 🎯 Problem Statement

We often need to track a fixed amount of time while:

- 📚 Studying
- 🏋️ Exercising
- 🍳 Cooking
- 🎤 Giving presentations
- ☕ Taking a short break
- ⏱️ Performing time-based activities

Watching a clock manually can be distracting, and a phone timer may
not always be convenient.

This project provides a lightweight countdown timer that runs
directly in the Python terminal.

---

# 💡 Project Objectives

The main objectives of this project are:

- Develop a practical Python-based countdown timer.
- Accept time input from the user.
- Convert minutes and seconds into total seconds.
- Display the remaining time in real time.
- Provide predefined and custom timer options.
- Display countdown progress.
- Provide an audible alarm when the timer finishes.
- Validate user input.
- Apply Python programming concepts in a practical project.
- Improve the code through incremental development.
- Test the core timer logic.
- Maintain the project using Git and GitHub.

---

# ✨ Features

## 🔹 Phase I Features

- ⚡ 30-second preset timer
- ⏱️ 1-minute preset timer
- 📚 5-minute preset timer
- 🎯 Custom timer
- ⌛ Live countdown
- 📊 Progress bar
- 🔢 MM:SS time format
- 🚀 3-2-1 starting countdown
- 🔊 Audible alarm
- 🔔 "TIME'S UP!" notification
- ✅ Basic input validation
- ❌ Negative-value rejection
- ❌ Invalid-input rejection
- ❌ Invalid seconds rejection

---

## 🚀 Phase II Improvements

Phase II does **not replace the Phase-I project**.

Instead, the existing project has been improved through better code
organization, validation, testing and error handling.

### 🧩 Modular Programming

The program is divided into separate reusable functions such as:

```text
print_header()
print_timer_menu()
format_time()
create_progress_bar()
play_sound()
validate_custom_time()
get_custom_time()
get_time()
show_timer()
show_completion_message()
start_sequence()
countdown()
run_timer()
```

This makes the program easier to:

- Read
- Understand
- Maintain
- Debug
- Test
- Extend

---

### ✅ Improved Input Validation

The program checks:

- Negative minutes
- Negative seconds
- Seconds greater than or equal to 60
- Zero duration
- Non-numeric input
- Invalid menu choices

Example:

```text
❌ Time cannot be negative.
❌ Seconds must be less than 60.
❌ Please enter a time greater than 0.
❌ Please enter numbers only.
```

---

### 📊 Improved Progress Display

The timer displays both remaining time and completed progress.

Example:

```text
⏳ 00:30 [████████████░░░░░░░░░░░] 50%
```

The progress calculation is separated into its own function so that
the logic can be tested independently.

---

### ⏱️ Improved Time Formatting

The `format_time()` function converts total seconds into readable
`MM:SS` format.

Examples:

```text
30 seconds  → 00:30
60 seconds  → 01:00
150 seconds → 02:30
300 seconds → 05:00
```

---

### 🚀 3-2-1 Start Sequence

Before the timer begins:

```text
🚀 Starting in...
   3
   2
   1
   GO!
```

This provides a short preparation period before the actual countdown.

---

### 🔊 Alarm System

When the timer reaches zero:

```text
═══════════════════════════════════════════════════════
             🔔 TIME'S UP!
═══════════════════════════════════════════════════════
```

A repeated high-low alarm is then played using Python's
`winsound` module.

---

### 🛡️ Safe Error Handling

Phase II includes safer program execution.

If the user interrupts the timer using:

```text
Ctrl + C
```

the program handles the interruption cleanly instead of displaying a
long Python traceback.

---

### 🧪 Logic Testing

Phase II introduces testing functions for important parts of the
program.

The project tests:

- Time formatting
- Input validation
- Progress calculation

Example:

```python
assert format_time(150) == "02:30"
```

Another example:

```python
assert validate_custom_time(1, 30) is True
```

Invalid input is also tested:

```python
assert validate_custom_time(-1, 10) is False
```

---

# 🖥️ Application Flow

```text
                ┌───────────────────────┐
                │       START APP       │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   Display Main Menu   │
                └───────────┬───────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   Select Timer Mode   │
                └───────────┬───────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
      ┌───────────────┐          ┌────────────────┐
      │ Preset Timer  │          │  Custom Timer  │
      └───────┬───────┘          └───────┬────────┘
              │                          │
              │                          ▼
              │                  ┌────────────────┐
              │                  │ Validate Input │
              │                  └───────┬────────┘
              │                          │
              └────────────┬─────────────┘
                           ▼
                  ┌──────────────────┐
                  │ 3-2-1 Countdown  │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │  Timer Running   │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Update Display   │
                  │ + Progress Bar   │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Remaining > 0 ?  │
                  └───────┬───┬──────┘
                          │   │
                        YES   NO
                          │   │
                          │   ▼
                          │ ┌────────────────┐
                          │ │   TIME'S UP!   │
                          │ └───────┬────────┘
                          │         │
                          │         ▼
                          │ ┌────────────────┐
                          │ │  Play Alarm    │
                          │ └───────┬────────┘
                          │         │
                          └─────────┘
                                    │
                                    ▼
                           ┌────────────────┐
                           │      END       │
                           └────────────────┘
```

---

# 🧠 Algorithm

1. Start the program.
2. Display the project heading.
3. Display the timer selection menu.
4. Take the user's choice.
5. If a preset is selected, load the predefined duration.
6. If custom mode is selected:
   - Take minutes.
   - Take seconds.
   - Validate the values.
7. Convert the selected time into total seconds.
8. Start the 3-2-1 preparation countdown.
9. Start the main countdown.
10. Display remaining time in `MM:SS`.
11. Calculate the completed percentage.
12. Display the progress bar.
13. Wait for one second.
14. Decrease the remaining time by one second.
15. Repeat until the remaining time becomes zero.
16. Display `TIME'S UP!`.
17. Play the alarm.
18. Display the completion message.
19. End the program.

---

# 🧪 Phase II Testing

The following test cases are used during Phase II development.

| ID | Test Case | Expected Result |
|---|---|---|
| TC01 | Select 30-second timer | Timer starts correctly |
| TC02 | Select 1-minute timer | Timer starts correctly |
| TC03 | Select 5-minute timer | Timer starts correctly |
| TC04 | Enter custom `1:30` | Input accepted |
| TC05 | Enter negative time | Input rejected |
| TC06 | Enter seconds = 60 | Input rejected |
| TC07 | Enter seconds > 60 | Input rejected |
| TC08 | Enter `0:00` | Input rejected |
| TC09 | Enter text instead of number | Input rejected |
| TC10 | Timer reaches zero | Alarm starts |
| TC11 | Check progress calculation | Correct percentage displayed |
| TC12 | Press Ctrl+C | Program exits safely |

---

# 🐍 Python Concepts Used

The project demonstrates:

- Variables
- Constants
- Data types
- Dictionaries
- Input/output
- `input()`
- `print()`
- `if-elif-else`
- `while` loop
- `for` loop
- Functions
- Function parameters
- Return values
- String formatting
- f-strings
- Integer arithmetic
- `time.sleep()`
- Exception handling
- `try-except`
- Assertions
- Modular programming
- Basic software testing

---

# 📦 Python Modules

## `time`

The `time` module is used to create one-second delays during the
countdown.

```python
import time
```

## `winsound`

The `winsound` module is used to generate the alarm sound.

```python
import winsound
```

> ⚠️ `winsound` is a Windows-specific Python module, so the alarm
> functionality is designed for Windows.

No third-party Python packages are required.

---

# 📁 Project Structure

```text
Countdown-Clock-and-Timer/
│
├── countdown_timer.py
├── README.md
│
└── screenshots/
    ├── phase1-output.png
    ├── phase2-output.png
    └── phase2-testing.png
```

---

# ▶️ How to Run

### Step 1 — Install Python

Install Python 3.x on your Windows system.

Verify the installation:

```bash
python --version
```

---

### Step 2 — Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

---

### Step 3 — Open the Project

```bash
cd Countdown-Clock-and-Timer
```

---

### Step 4 — Run the Program

```bash
python countdown_timer.py
```

---

# 🖥️ Sample Program Output

```text
╔════════════════════════════════════════════╗
║        ⏰ SMART COUNTDOWN TIMER            ║
║                                            ║
║   Python Experiential Learning Project     ║
╚════════════════════════════════════════════╝


╔══════════════════════════════════════╗
║          SELECT TIMER MODE           ║
╠══════════════════════════════════════╣
║  1. ⚡ 30 Seconds                    ║
║  2. ⏱️ 1 Minute                      ║
║  3. 📚 5 Minutes                     ║
║  4. 🎯 Custom Time                   ║
╚══════════════════════════════════════╝

👉 Enter your choice (1-4): 4

Enter minutes: 1
Enter seconds: 30

📌 Timer selected successfully!
⏱️ Selected time: 01:30

🚀 Starting in...
   3
   2
   1
   GO!

⏱️ TIMER RUNNING
───────────────────────────────────────────────────────

⏳ 01:00 [████████░░░░░░░░░░░░░░░] 33%
```

When the timer finishes:

```text
═══════════════════════════════════════════════════════
             🔔 TIME'S UP!
═══════════════════════════════════════════════════════

🔊 ALARM STARTED!
🔕 Alarm finished.
✅ Timer completed successfully!

👋 Thank you for using Smart Countdown Timer!
```

---

# 🧪 Running Phase II Logic Tests

Phase II includes logic-level tests for:

```text
✓ Time formatting
✓ Input validation
✓ Progress calculation
```

Example:

```python
assert format_time(150) == "02:30"
assert format_time(60) == "01:00"

assert validate_custom_time(1, 30) is True
assert validate_custom_time(-1, 10) is False
assert validate_custom_time(1, 60) is False
```

These tests help verify important parts of the application without
requiring the complete countdown to run.

---

# 🌿 GitHub Development

GitHub is used to maintain:

- Source code
- README documentation
- Project progress
- Testing evidence
- Development history
- Phase-wise updates

## Phase II Commit Progression

The recommended meaningful commit progression is:

```text
01. Prepare project for Phase II
02. Improve timer input validation
03. Improve countdown and progress display
04. Organize countdown timer functions
05. Add safe timer interruption handling
06. Add Phase II logic tests
07. Update README for Phase II
08. Add Phase II testing screenshots
09. Complete Phase II project update
```

### Example Commit

```bash
git add countdown_timer.py
git commit -m "feat: improve timer input validation"
git push origin main
```

### Documentation Commit

```bash
git add README.md
git commit -m "docs: update project progress for phase 2"
git push origin main
```

> 💡 Each commit should represent a real development change.
> Avoid creating duplicate or meaningless commits only to increase
> the commit count.

---

# 📊 Phase-Wise Development

## 🟢 Phase I — Initial Development

### Completed

- Problem understanding
- Project idea
- Basic algorithm
- Timer logic
- Preset timers
- Custom timer
- Input validation
- Progress bar
- Alarm system
- Initial GitHub repository
- Initial README
- Project presentation

---

## 🟡 Phase II — Project Progress

### Current Development

- Existing Phase-I functionality retained
- Code modularization
- Improved validation
- Improved progress calculation
- Improved time formatting
- Safe interruption handling
- Logic-level testing
- README documentation
- GitHub commit progression
- Phase-II presentation update

### Phase-II Goal

Demonstrate substantial progress toward the final project while
keeping the original Countdown Clock and Timer problem statement.

---

## 🔵 Phase III — Final Implementation

### Planned Work

- Final testing
- Final debugging
- Final documentation
- Final output verification
- Deployment/packaging where appropriate
- Final presentation
- Viva preparation
- Final project submission

---

# 📈 Development Roadmap

```text
PHASE I
   │
   ├── Problem Identification
   ├── Algorithm
   ├── Basic Timer
   ├── Input Validation
   ├── Progress Bar
   ├── Alarm
   └── GitHub Setup
          │
          ▼
PHASE II
   │
   ├── Code Refactoring
   ├── Modular Functions
   ├── Improved Validation
   ├── Progress Calculation
   ├── Error Handling
   ├── Logic Testing
   ├── README Update
   └── GitHub Development
          │
          ▼
PHASE III
   │
   ├── Final Testing
   ├── Debugging
   ├── Documentation
   ├── Final Presentation
   ├── Viva
   └── Submission
```

---

# 🔮 Future Scope

The project can be extended in future versions with:

- 🖥️ Graphical User Interface (GUI)
- ▶️ Start button
- ⏸️ Pause button
- ▶️ Resume button
- 🔄 Reset button
- 🔊 Custom alarm sounds
- ⏱️ Multiple timers
- 📜 Timer history
- 🔔 Desktop notifications
- ⚙️ Configurable timer presets
- 📦 Standalone application packaging
- 🧪 More automated test cases
- 🌐 Cross-platform sound/notification support

These features are considered future extensions and are not required
to change the current Phase-II project concept.

---

# 🎓 Learning Outcomes

Through this Experiential Learning project, the following skills are
developed:

### Technical Skills

- Python programming
- Functions and modular programming
- Input validation
- Exception handling
- Time-based programming
- Basic testing
- Debugging
- Git and GitHub
- Documentation

### Project Skills

- Problem identification
- Algorithm design
- Incremental development
- Testing and validation
- Version control
- Project presentation
- Viva preparation

---

# 📌 Project Status

```text
╔══════════════════════════════════════════╗
║         PROJECT DEVELOPMENT STATUS       ║
╠══════════════════════════════════════════╣
║ Phase I                  ✅ Completed    ║
║ Phase II Development     🟡 In Progress ║
║ Phase III                🔵 Planned     ║
╚══════════════════════════════════════════╝
```

The original Phase-I functionality is retained while Phase-II focuses
on improving code quality, testing, validation, documentation and
GitHub development.

---

# 👨‍🎓 Author

## Amit Gajanan Japulkar

**USN:** CM25005  
**Department:** CSE (AI & ML)  
**Course:** Python Programming Language (N-PCCCM304P)  
**Academic Session:** 2026-27 (ODD)

---

# 📚 Academic Project

This project is developed as part of the **Experiential Learning
Project Assessment** for the Python Programming Language course.

**Project Topic:** Countdown Clock and Timer

**Project Title:** Smart Countdown Clock & Timer

---

# 🏁 Conclusion

The **Smart Countdown Clock & Timer** demonstrates how Python can be
used to develop a practical command-line utility for time management.

The project began with a basic countdown implementation during
Phase I. During Phase II, the existing implementation was retained
and improved through modular programming, stronger input validation,
progress calculation, safe error handling and logic-level testing.

The project will continue toward Phase III with final testing,
documentation, presentation, viva preparation and final submission.

---

<p align="center">
  <b>⏰ Smart Countdown Clock & Timer</b>
</p>

<p align="center">
  Made with 🐍 Python
</p>

<p align="center">
  <b>Amit Gajanan Japulkar • CM25005</b>
</p>
