from vosk import Model, KaldiRecognizer
import wave
import sys

model = Model("./vosk-model-small-en-us-0.15")

if len(sys.argv) < 2:
    print("Usage: python transcribe.py <wav_file_path>")
    sys.exit(1)

wf = wave.open(sys.argv[1], "rb")
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
