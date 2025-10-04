from pynput import keyboard
import pygame
import os
import itertools

pygame.mixer.init()

sound_dir = os.path.join(os.path.dirname(__file__), "wav")
notes = []

for file in sorted(os.listdir(sound_dir)):
    if file.endswith(".wav"):
        note_name = file.replace(".wav", "").lower()
        notes.append((note_name, pygame.mixer.Sound(os.path.join(sound_dir, file))))

if not notes:
    raise RuntimeError("No .wav files found in wav/ directory!")

note_cycle = itertools.cycle(notes)

key_to_note = {}

def on_press(key):
    try:
        k = key.char
    except AttributeError:
        return

    if k not in key_to_note:
        key_to_note[k] = next(note_cycle)

    note_name, sound = key_to_note[k]
    sound.play()
    #print(f"Key '{k}' -> {note_name}")

print("🎹 Piano typing is running! Type anything, each key plays a note. Ctrl+C to quit.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
