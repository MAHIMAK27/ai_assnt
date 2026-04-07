# 🎤 Voice Assistant using Python & OpenAI

## 📌 Overview

This project is a simple **Voice Assistant** built using Python.
It listens to your voice, converts speech into text, sends the query to an AI model, and prints the response.

---

## ⚙️ Features

* 🎙️ Speech-to-text using `speech_recognition`
* 🤖 AI responses using OpenAI API
* 🔁 Continuous listening loop
* 🛑 Exit command support ("stop" or "exit")
* ⚡ Lightweight and easy to run

---

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* OpenAI API

---

## 📦 Installation

### 1. Clone the repository

```bash id="z9l2kx"
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
```

### 2. Install dependencies

```bash id="a7m1qp"
pip install SpeechRecognition openai pyaudio
```

> ⚠️ Note: `pyaudio` may require additional setup depending on your OS.

---

## 🔑 Setup API Key

Set your OpenAI API key as an environment variable:

### Windows

```bash id="o1n2vb"
setx OPENAI_API_KEY "your_api_key_here"
```

### macOS / Linux

```bash id="c8d4jk"
export OPENAI_API_KEY="your_api_key_here"
```

---

## ▶️ Usage

Run the script:

```bash id="x5pt8m"
python voice_assistant.py
```

---

## 💡 How It Works

1. The microphone captures your voice input
2. Speech is converted to text using Google Speech Recognition
3. The text is sent to the OpenAI model
4. The AI response is printed in the console

---

## 🗣️ Commands

* Say anything → Get AI response
* Say **"exit"** or **"stop"** → Quit the program

---

## ⚠️ Requirements

* Working microphone 🎤
* Internet connection 🌐
* OpenAI API key

---

## 🚧 Limitations

* No text-to-speech (output is printed only)
* Depends on internet for speech recognition & AI
* Background noise may affect accuracy

---

## 🔮 Future Improvements

* Add text-to-speech (voice replies)
* Wake word detection (e.g., "Hey Assistant")
* GUI interface
* Multi-language support

---

## 🤝 Contributing

Feel free to fork this repository and improve it!

---

## 📜 License

This project is open-source and available under the MIT License.
