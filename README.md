# Noise Notifier for macOS

Noise Notifier is a Python-based sound detection utility built for macOS. It continuously monitors ambient noise using the MacBook’s built-in microphone and triggers a native macOS notification when a loud sound is detected within a calibrated threshold.

This project was originally created to solve a common problem: when using noise-cancelling headphones at home, it's easy to miss important sounds like knocks on the door, phone rings, or kitchen alerts. Noise Notifier helps ensure that critical sounds don't go unnoticed.

## Features

- Real-time sound level monitoring
- Automatically selects MacBook’s internal microphone, ignoring external Bluetooth devices
- Threshold-based sound detection with tunable volume sensitivity
- Cooldown system to prevent repeated or spammy notifications
- Native macOS notifications using `terminal-notifier`

## How It Works

- Uses the `sounddevice` library to access audio input
- Captures short audio segments (default: 0.2 seconds) at a defined sample rate
- Calculates the Root Mean Square (RMS) volume to estimate sound intensity
- Compares the volume to user-defined thresholds
- Sends a notification if the volume is within a specified range and cooldown has passed

## Code Structure

- `main.py`: The core script that initializes audio input, calculates volume, and handles notifications
- `requirements.txt`: Python dependencies (`sounddevice`, `numpy`)
- `.gitignore`: Standard ignores for virtual environments and Python bytecode

## Configuration

You can modify the following parameters in `main.py` to suit your environment:

THRESHOLD_MIN = 300       # Minimum volume to trigger notification
THRESHOLD_MAX = 5000      # Maximum volume to ignore overly loud spikes
COOLDOWN = 1              # Seconds to wait before sending another notification
SAMPLE_RATE = 4410        # Sampling rate in Hz
DURATION = 0.2            # Audio block duration in seconds

## How to Run

1. Install the required Python packages using:
   ```pip install -r requirements.txt```
2. Make sure terminal-notifier is installed (for macOS notifications):
   ```brew install terminal-notifier```
3. Run the program:
   ```python main.py```
