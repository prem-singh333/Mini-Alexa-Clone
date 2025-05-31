# Mini-Alexa-Clone - Voice Assistant (Jarvis)

**"Jarvis"** is a  simple voice assistant built using Python. It Listens for the wake world **"Jarvis"** and performs basic voice-activated tasks like opening website or playing songs.

## Features

- Wake world activation: **"Jarvis"**
- Opens websites like **Google** and **YouTube**
- Plays songs from a predefined library (`songLibrary.py`)
- Speaks responses using text-to-speech

## Technologies used

- `Speech_recognition` - for voice input
- `pyttsx` - for speech output
- `webbrowser` - to open web pages

## Exmple `songLibrary.py`

```python
music = {
    "song1": "https://youtube.com/link1",
    "song2": "https://youtube.com/link2"
}