# 🎹 Piano Typing

Turn your keyboard into a piano! Every key you type plays a piano note, helping you code, type, or just have fun while improving focus and motivation.

---

## Features

* Play piano notes with every key you type.
* Automatic mapping: every key cycles through all available notes.
* Works on Windows, macOS, and Linux.
* Lightweight and easy to run in the background.
* Consistent mapping: each key always plays the same note during a session.

---

## Installation (Windows)

1. **Clone the repository:**

```powershell
git clone https://github.com/parisjava/wav-piano-sound.git
cd wav-piano-sound
```

2. **Set up a Python virtual environment:**

```powershell
python -m venv venv
.\venv\Scripts\activate
```

3. **Install dependencies:**

```powershell
pip install pygame pynput
```

4. **Run the script:**

```powershell
python piano_typing.py
```

5. **Optional:** Add to startup to have it run automatically when Windows starts.

---

## How It Works

* The script loads all WAV files from the `wav/` folder.
* As you type, keys are assigned to notes from the list, cycling through them automatically.
* Each key always plays the same note during a session.

---

## Enhancing the Piano Sound for Fast Typers

If you type quickly, you might notice some notes cut off. Here’s how to improve the sound:

1. **Increase the mixer channels:**
   Pygame’s default mixer may limit how many sounds play at the same time. Edit the script:

```python
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(32)  # allows more notes to play simultaneously
```

2. **Use shorter WAV files** for faster response.

3. **Lower the latency buffer** if you feel delay (adjust `buffer` in `pygame.mixer.init`).

4. **Optional: Overlapping notes:**
   Pygame allows multiple instances of the same sound to overlap. The script already uses `pygame.mixer.Sound.play()`, which supports this.

---

## Tips for Fun & Productivity

* Map specific rows to octaves (like home row → middle C) for more musical typing.
* Combine with coding sprints to gamify typing sessions.
* Adjust your editor font size and colors for a visually rhythmic experience.

---

## License

MIT License — free to use, modify, and share.
