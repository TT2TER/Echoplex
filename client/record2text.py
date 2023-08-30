import pyaudio
import wave
import os
import whisper
from lib.public import shared_module


def record2text():
    # 配置录音参数
    FORMAT = pyaudio.paInt16  # 采样格式为16位整数
    CHANNELS = 1  # 单声道
    RATE = 44100  # 采样率：44100 Hz
    CHUNK = 1024  # 每次读取的音频块大小
    RECORD_SECONDS = 5  # 录制时长：5秒
    OUTPUT_PATH = "files/recordings"
    OUTPUT_FILENAME = "recorded_audio.wav"

    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    # 初始化录音设备
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("开始录音...")
    shared_module.main_page.show_start_record()

    frames = []

    # 录制音频
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音结束.")
    #shared_module.main_page.hide_start_record()
    # 停止录音流
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 将录制的音频保存为WAV文件
    output_filepath = os.path.join(OUTPUT_PATH, OUTPUT_FILENAME)
    print(f"output path is {output_filepath}")
    with wave.open(output_filepath, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    print(f"音频已保存为 {OUTPUT_FILENAME}")
    whisper_model = whisper.load_model("base")
    result = whisper_model.transcribe(output_filepath)
    final_text = ", ".join([i["text"] for i in result["segments"] if i is not None])
    print(final_text)
    return final_text


