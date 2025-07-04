import sounddevice as sd
import numpy as np
import time
import os

DURATION = 0.2
SAMPLE_RATE = 4410
THRESHOLD_MIN = 300
THRESHOLD_MAX = 5000
COOLDOWN = 1
ALERT_TIME= 0

def notify_mac():
    os.system('terminal-notifier -title "Noise Alert 🚨" -message "🔔 Detected something!!"')


def find_macbook_mic():
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if "MacBook Air Microphone" in device["name"]:
            return i
    raise RuntimeError("MacBook Air Microphone not found!")

def get_volume_level(indata):
    volume=np.sqrt(np.mean(indata**2))
    return volume*(10**5)

mac_mic_index = find_macbook_mic()

with sd.InputStream(device=mac_mic_index, channels=1, samplerate=SAMPLE_RATE, blocksize=int(SAMPLE_RATE*DURATION)) as stream:
    print("All ears 👂")
    while True:
        audio_data, _ =stream.read(int(SAMPLE_RATE*DURATION))
        volume=get_volume_level(audio_data)
        print("Volume: ",volume)

        current_time = time.time()

        if THRESHOLD_MIN < volume < THRESHOLD_MAX:
            if current_time - ALERT_TIME > COOLDOWN:
                print("🔔 Detected something!!")
                notify_mac()
                ALERT_TIME = current_time