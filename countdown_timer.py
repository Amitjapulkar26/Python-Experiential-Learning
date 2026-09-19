"""
SMART COUNTDOWN CLOCK & TIMER
Experiential Learning Project - Phase II

Course : Python Programming Language (N-PCCCM304P)
Author : Amit Gajanan Japulkar
USN    : CM25005
Session: 2026-27 (ODD)

Phase-II purpose:
- Preserve all Phase-I functionality.
- Improve code organization and readability.
- Strengthen input validation.
- Improve progress calculation and display.
- Add structured testing functions.
- Keep the original project concept unchanged.
"""

import time
import winsound


# ============================================================
# PROJECT CONSTANTS
# ============================================================

APP_TITLE = "SMART COUNTDOWN CLOCK & TIMER"
AUTHOR = "Amit Gajanan Japulkar"
USN = "CM25005"

# Preset timer values in seconds.
PRESET_TIMERS = {
    "1": 30,
    "2": 60,
    "3": 300,
}

# Progress bar configuration.
PROGRESS_BAR_SIZE = 25

# Alarm configuration.
ALARM_REPEAT = 5
HIGH_TONE_FREQUENCY = 1400
LOW_TONE_FREQUENCY = 700
TONE_DURATION = 400
TONE_PAUSE = 0.1


# ============================================================
# DISPLAY / UI FUNCTIONS
# ============================================================

def print_header():
    """Display the main application heading."""

    print("\n")
    print("╔════════════════════════════════════════════╗")
    print("║        ⏰ SMART COUNTDOWN TIMER            ║")
    print("║                                            ║")
    print("║   Python Experiential Learning Project     ║")
    print("╚════════════════════════════════════════════╝")


def print_timer_menu():
    """Display the available timer modes."""

    print("\n╔══════════════════════════════════════╗")
    print("║          SELECT TIMER MODE           ║")
    print("╠══════════════════════════════════════╣")
    print("║  1. ⚡ 30 Seconds                    ║")
    print("║  2. ⏱️ 1 Minute                      ║")
    print("║  3. 📚 5 Minutes                     ║")
    print("║  4. 🎯 Custom Time                   ║")
    print("╚══════════════════════════════════════╝")


def format_time(total_seconds):
    """
    Convert total seconds into MM:SS format.

    Example:
        150 seconds -> 02:30
    """

    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f"{minutes:02d}:{seconds:02d}"


def create_progress_bar(remaining, total):
    """
    Create a 25-character progress bar.

    The percentage represents completed time.
    """

    if total <= 0:
        return "░" * PROGRESS_BAR_SIZE, 0

    completed = total - remaining
    percent = completed * 100 // total

    filled = percent * PROGRESS_BAR_SIZE // 100

    bar = "█" * filled + "░" * (PROGRESS_BAR_SIZE - filled)

    return bar, percent


# ============================================================
# ALARM
# ============================================================

def play_sound():
    """Play a repeated high-low alarm when the timer finishes."""

    print("\n🔊 ALARM STARTED!")

    for _ in range(ALARM_REPEAT):

        # High-frequency beep.
        winsound.Beep(
            HIGH_TONE_FREQUENCY,
            TONE_DURATION
        )

        # Small pause between tones.
        time.sleep(TONE_PAUSE)

        # Low-frequency beep.
        winsound.Beep(
            LOW_TONE_FREQUENCY,
            TONE_DURATION
        )

        # Small pause before the next pattern.
        time.sleep(TONE_PAUSE)

    print("🔕 Alarm finished.")


# ============================================================
# INPUT VALIDATION
# ============================================================

def validate_custom_time(minutes, seconds):
    """
    Validate custom timer values.

    Returns:
        True  -> valid input
        False -> invalid input
    """

    if minutes < 0 or seconds < 0:
        print("❌ Time cannot be negative.")
        return False

    if seconds >= 60:
        print("❌ Seconds must be less than 60.")
        return False

    total = minutes * 60 + seconds

    if total == 0:
        print("❌ Please enter a time greater than 0.")
        return False

    return True


def get_custom_time():
    """Read and validate custom minutes and seconds."""

    while True:

        try:
            minutes = int(input("Enter minutes: "))
            seconds = int(input("Enter seconds: "))

            if validate_custom_time(minutes, seconds):
                return minutes * 60 + seconds

        except ValueError:
            print("❌ Please enter numbers only.")


# ============================================================
# TIMER SELECTION
# ============================================================

def get_time():
    """
    Display the timer menu and return the selected time.

    Presets:
        1 -> 30 seconds
        2 -> 1 minute
        3 -> 5 minutes
        4 -> Custom timer
    """

    print_timer_menu()

    while True:

        choice = input("\n👉 Enter your choice (1-4): ").strip()

        # Preset timer selection.
        if choice in PRESET_TIMERS:
            return PRESET_TIMERS[choice]

        # Custom timer selection.
        if choice == "4":
            return get_custom_time()

        # Invalid menu selection.
        print("❌ Invalid choice. Try again.")


# ============================================================
# TIMER DISPLAY
# ============================================================

def show_timer(remaining, total):
    """Display remaining time, progress bar and percentage."""

    bar, percent = create_progress_bar(
        remaining,
        total
    )

    print(
        f"\r⏳ {format_time(remaining)} "
        f"[{bar}] {percent}%",
        end="",
        flush=True
    )


def show_completion_message():
    """Display the completion message."""

    print("\n\n" + "═" * 55)
    print("             🔔 TIME'S UP!")
    print("═" * 55)


# ============================================================
# START COUNTDOWN
# ============================================================

def start_sequence():
    """Run the 3-2-1 preparation countdown."""

    print("\n🚀 Starting in...")

    for number in [3, 2, 1]:

        print(f"   {number}")
        time.sleep(1)

    print("\n   GO!")


# ============================================================
# MAIN COUNTDOWN LOGIC
# ============================================================

def countdown(total):
    """
    Run the main countdown.

    The timer decreases by one second until zero.
    """

    remaining = total

    start_sequence()

    print("\n⏱️ TIMER RUNNING")
    print("─" * 55)

    while remaining > 0:

        # Show the current timer state.
        show_timer(
            remaining,
            total
        )

        # Wait for one second.
        time.sleep(1)

        # Decrease remaining time.
        remaining -= 1

    # Display final 00:00 state.
    show_timer(
        0,
        total
    )

    show_completion_message()

    # Play the alarm after reaching zero.
    play_sound()

    print("✅ Timer completed successfully!")


# ============================================================
# ERROR-SAFE TIMER EXECUTION
# ============================================================

def run_timer(total_time):
    """
    Run the countdown safely.

    Ctrl+C is handled so the program exits cleanly instead
    of showing a long traceback.
    """

    try:
        countdown(total_time)

    except KeyboardInterrupt:
        print("\n\n⚠️ Timer interrupted by the user.")
        print("ℹ️ Program stopped safely.")

    except Exception as error:
        print("\n❌ An unexpected error occurred.")
        print(f"Details: {error}")


# ============================================================
# PHASE-II TEST FUNCTIONS
# ============================================================

def test_time_format():
    """Test the time-formatting function."""

    assert format_time(0) == "00:00"
    assert format_time(30) == "00:30"
    assert format_time(60) == "01:00"
    assert format_time(150) == "02:30"

    print("✅ Time-format test passed.")


def test_custom_time_validation():
    """Test valid and invalid custom timer values."""

    assert validate_custom_time(1, 30) is True
    assert validate_custom_time(0, 1) is True

    # These should be rejected.
    assert validate_custom_time(-1, 10) is False
    assert validate_custom_time(1, 60) is False
    assert validate_custom_time(0, 0) is False

    print("✅ Input-validation tests passed.")


def test_progress_calculation():
    """Test progress-bar calculations."""

    bar, percent = create_progress_bar(
        100,
        100
    )

    assert percent == 0
    assert len(bar) == PROGRESS_BAR_SIZE

    bar, percent = create_progress_bar(
        50,
        100
    )

    assert percent == 50
    assert len(bar) == PROGRESS_BAR_SIZE

    bar, percent = create_progress_bar(
        0,
        100
    )

    assert percent == 100
    assert len(bar) == PROGRESS_BAR_SIZE

    print("✅ Progress-bar tests passed.")


def run_phase2_tests():
    """
    Run Phase-II functional tests.

    These tests do not start the alarm or countdown.
    They verify the core logic safely.
    """

    print("\n" + "=" * 55)
    print("           PHASE-II LOGIC TESTING")
    print("=" * 55)

    test_time_format()
    test_custom_time_validation()
    test_progress_calculation()

    print("\n🎉 All Phase-II logic tests passed successfully!")


# ============================================================
# PROJECT INFORMATION
# ============================================================

def show_project_info():
    """Display project information."""

    print("\n" + "─" * 55)
    print("PROJECT INFORMATION")
    print("─" * 55)
    print(f"Project : {APP_TITLE}")
    print(f"Author  : {AUTHOR}")
    print(f"USN     : {USN}")
    print("Course  : Python Programming Language (N-PCCCM304P)")
    print("Phase   : Experiential Learning - Phase II")
    print("─" * 55)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    """Main entry point of the Smart Countdown Timer."""

    print_header()

    show_project_info()

    # Get timer duration from the user.
    total_time = get_time()

    print("\n📌 Timer selected successfully!")
    print(
        f"⏱️ Selected time: "
        f"{format_time(total_time)}"
    )

    # Start the selected timer.
    run_timer(total_time)

    print(
        "\n👋 Thank you for using "
        "Smart Countdown Timer!"
    )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
