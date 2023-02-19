import wave
import pyaudio
import openai
import whisper

class voice:
    #定义数据流块
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    #录音时间
    RECORD_SECONDS = 5
    frames = []

    def push_stream(self):
        #打开数据流    
        self.p = pyaudio.PyAudio()
        #设定捕获参数
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        print("* recording")        
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            self.frames.append(data)

        stream.stop_stream()
        stream.close()
        self.p.terminate()

    def save(self,Path):
        #写入录音文件
        wf = wave.open(Path, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def convert(self,Path):
        model = whisper.load_model("base")
        result = model.transcribe("audio.wav")
        return result["text"]
        
    def chat(text):
        # Set your API key
        openai.api_key = ""
        # Use the GPT-3 model
        completion = openai.Completion.create(
            engine="text-davinci-002",
            prompt=text,
            max_tokens=1024,
            temperature=0.5
        )
        # Print the generated text
        return completion.choices[0].text

if __name__ == "__main__":
    r = voice()
    r.push_stream()
    r.save('audio.wav')
    text = r.convert('audio.wav')
    print(text)
    #reply = r.chat(text)
    #print(reply)