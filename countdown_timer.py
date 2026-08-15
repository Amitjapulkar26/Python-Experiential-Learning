"""
SMART COUNTDOWN CLOCK & TIMER
Experiential Learning Project

Course : Python Programming Language (N-PCCCM304P)
Author : Amit Gajanan Japulkar
"""

import time
import winsound


# ---------- ALARM SOUND ----------
def play_sound():
    """Play a loud repeated alarm when the timer finishes."""

    print("\n🔊 ALARM STARTED!")

    # Repeat the alarm pattern 5 times
    for _ in range(5):

        # High tone
        winsound.Beep(1400, 400)

        # Short pause
        time.sleep(0.1)

        # Low tone
        winsound.Beep(700, 400)

        # Short pause
        time.sleep(0.1)

    print("🔕 Alarm finished.")


# ---------- GET TIMER ----------
def get_time():

    print("\n╔══════════════════════════════════════╗")
    print("║          SELECT TIMER MODE           ║")
    print("╠══════════════════════════════════════╣")
    print("║  1. ⚡ 30 Seconds                    ║")
    print("║  2. ⏱️ 1 Minute                      ║")
    print("║  3. 📚 5 Minutes                     ║")
    print("║  4. 🎯 Custom Time                   ║")
    print("╚══════════════════════════════════════╝")

    while True:

        choice = input("\n👉 Enter your choice (1-4): ")

        # 30 seconds
        if choice == "1":
            return 30

        # 1 minute
        elif choice == "2":
            return 60

        # 5 minutes
        elif choice == "3":
            return 300

        # Custom timer
        elif choice == "4":

            try:
                minutes = int(input("Enter minutes: "))
                seconds = int(input("Enter seconds: "))

                # Check negative values
                if minutes < 0 or seconds < 0:
                    print("❌ Time cannot be negative.")
                    continue

                # Check seconds
                if seconds >= 60:
                    print("❌ Seconds must be less than 60.")
                    continue

                # Convert everything into seconds
                total = minutes * 60 + seconds

                # Check zero
                if total == 0:
                    print("❌ Please enter a time greater than 0.")
                    continue

                return total

            except ValueError:
                print("❌ Please enter numbers only.")

        # Invalid menu option
        else:
            print("❌ Invalid choice. Try again.")


# ---------- SHOW TIMER ----------
def show_timer(remaining, total):

    # Convert seconds into minutes and seconds
    minutes = remaining // 60
    seconds = remaining % 60

    # Calculate completed time
    completed = total - remaining

    # Calculate percentage
    percent = completed * 100 // total

    # Progress bar size
    bar_size = 25

    # Calculate filled part
    filled = percent * bar_size // 100

    # Create progress bar
    bar = "█" * filled + "░" * (bar_size - filled)

    # Display timer
    print(
        f"\r⏳ {minutes:02d}:{seconds:02d} "
        f"[{bar}] {percent}%",
        end="",
        flush=True
    )


# ---------- COUNTDOWN ----------
def countdown(total):

    remaining = total

    print("\n🚀 Starting in...")

    # 3-second preparation countdown
    for number in [3, 2, 1]:

        print(f"   {number}")

        time.sleep(1)

    print("\n⏱️ TIMER RUNNING")
    print("─" * 55)

    # Main countdown
    while remaining > 0:

        # Display remaining time
        show_timer(remaining, total)

        # Wait one second
        time.sleep(1)

        # Decrease time by one second
        remaining -= 1

    # Display final 00:00
    show_timer(0, total)

    print("\n\n" + "═" * 55)

    print("             🔔 TIME'S UP!")

    print("═" * 55)

    # Play alarm
    play_sound()

    print("✅ Timer completed successfully!")


# ---------- MAIN PROGRAM ----------
def main():

    print("\n")

    print("╔════════════════════════════════════════════╗")
    print("║        ⏰ SMART COUNTDOWN TIMER            ║")
    print("║                                            ║")
    print("║   Python Experiential Learning Project     ║")
    print("╚════════════════════════════════════════════╝")

    # Get timer from user
    total_time = get_time()

    print("\n📌 Timer selected successfully!")

    # Start countdown
    countdown(total_time)

    print("\n👋 Thank you for using Smart Countdown Timer!")


# ---------- START PROGRAM ----------
if __name__ == "__main__":
    main()