import pyaudio
import wave

from micstream import MicrophoneStream

SAMPLE_RATE = 44100
FORMAT = pyaudio.paInt16
CHANNELS = 1
CHUNK = int(SAMPLE_RATE/10)
WAVE_OUTPUT_FILENAME = "output3.wav"

p = pyaudio.PyAudio()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setframerate(SAMPLE_RATE)

try:
    with MicrophoneStream(SAMPLE_RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        for content in audio_generator:
            wf.writeframes(content)
except: pass

wf.close()

p.terminate() 
