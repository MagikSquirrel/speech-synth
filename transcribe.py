from vosk import Model, KaldiRecognizer
import wave

model = Model("./vosk-model-small-en-us-0.15")
wf = wave.open("./hello.wav", "rb")
rec = KaldiRecognizer(model, wf.getframerate())

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())
print(rec.FinalResult())
