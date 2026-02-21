import speech_recognition as sr
from openai import OpenAI

# Client reads API key from environment variable
client = OpenAI()

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)

        text = r.recognize_google(audio)
        print("You:", text)
        return text

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Speech service error")
        return ""

def ask_gpt(question):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=question
    )
    return response.output_text

if __name__ == "__main__":
    print("🎤 Voice Assistant Started")

    while True:
        command = listen().lower()

        if not command:
            continue

        if "exit" in command or "stop" in command:
            print("Goodbye 👋")
            break

        reply = ask_gpt(command)
        print("Assistant:", reply)
