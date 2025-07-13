#!/usr/bin/env python3
"""
Simple Console Stopwatch
Commands: start | stop | lap | reset | quit
"""

import time


def fmt(seconds: float) -> str:
    """Convert seconds to HH:MM:SS format."""
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def main():
    start_time = None      # Holds the start timestamp while running
    laps = []              # List of lap times

    while True:
        cmd = input("\n[start / stop / lap / reset / quit] > ").strip().lower()

        # 1️⃣ START / RESUME
        if cmd == "start":
            if start_time is None:
                start_time = time.time()
                print("⏱️  Stopwatch started.")
            else:
                print("It’s already running.")

        # 2️⃣ STOP / PAUSE
        elif cmd == "stop":
            if start_time is not None:
                elapsed = time.time() - start_time
                print("⏸️  Paused. Total time:", fmt(elapsed))
                start_time = None
            else:
                print("It hasn’t started yet.")

        # 3️⃣ LAP
        elif cmd == "lap":
            if start_time is None:
                print("Start the stopwatch first.")
            else:
                lap = time.time() - start_time
                laps.append(lap)
                print(f"🏁 Lap {len(laps)}:", fmt(lap))

        # 4️⃣ RESET
        elif cmd == "reset":
            start_time = None
            laps.clear()
            print("🔄 Stopwatch reset.")

        # 5️⃣ QUIT
        elif cmd == "quit":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid command.")

        # Display lap list (if any)
        if laps:
            print("Lap list:")
            for i, lap in enumerate(laps, 1):
                print(f"  {i:02d}. {fmt(lap)}")


if __name__ == "__main__":
    main()
