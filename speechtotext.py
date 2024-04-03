import speech_recognition as sr

r = sr.Recognizer()

def record_text():
    try:
        with sr.Microphone() as source2:
            print("Listening...")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            return MyText

    except sr.RequestError as e:
        print(f"Could not request results; {e}")

    except sr.UnknownValueError as e:
        print(f"Unknown error has occurred; {e}")

    return None

def output_text(text):
    if text:
        with open("output.txt", "a") as f:
            f.write(text)
            f.write("\n")
        print("Recorded:", text)

while True:
    text = record_text()
    if text:
        output_text(text)
