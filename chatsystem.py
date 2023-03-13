import wave
import pyaudio
import openai
import whisper
import numpy as np

def Monitor_MIC(th, filename):
    CHUNK = 512
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000 	#录音时的采样率
    WAVE_OUTPUT_FILENAME = filename + ".wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    while (True):
        for i in range(0, 10):
            data = stream.read(CHUNK)
            frames.append(data)
        audio_data = np.fromstring(data, dtype=np.short)
        temp = np.max(audio_data)
        if temp > th :
            print("detected a signal")
            print('current threshold: ',temp)
            less = []
            frames2 = []
            while (True):
                print("recording")
                for i in range(0, 30):
                    data2 = stream.read(CHUNK)
                    frames2.append(data2)
                audio_data2 = np.fromstring(data2, dtype=np.short)
                temp2 = np.max(audio_data2)
                if temp2 < th:
                    less.append(-1)
                    print("below threshold, counting: ", less)
                    #如果有连续5个循环的点，都不是声音信号，就认为音频结束了
                    if len(less) == 5:
                        break
                else:
                    less = []
            break
        else: return 0
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames2))
    wf.close()
    return 1

def convert(Path,model):
    m = whisper.load_model(model)
    return m.transcribe(Path)

def chat(text):
        # Set your API key
        openai.api_key = "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"
        # Use the GPT-3 model
        completion = openai.Completion.create(
            engine="text-davinci-002",
            prompt=text,
            max_tokens=1024,
            temperature=0.5
        )
        # Print the generated text
        return completion.choices[0].text
