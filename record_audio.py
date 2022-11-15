import wave
import pyaudio
import logging

"""
This module will be used to record audio and create a .wav file output.
Audio signal parameters:
- number of channels (mono/stereo)
- samble width (bits per sample)
- framerate/sample_rate (samples per second -> 44,100 Hz)
- number of frames 
- values of a frame
"""

def record_sample(duration, path):
    FRAMES_PER_BUFFER = 3200
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    try:
        p = pyaudio.PyAudio()
        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=FRAMES_PER_BUFFER
        )
        logging.info("Starting recording...")
        frames = []
        for _ in range(0, int(RATE/FRAMES_PER_BUFFER*duration)):
            data = stream.read(FRAMES_PER_BUFFER)
            frames.append(data)
        logging.info("Finished recording.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        recording_object = wave.open(f"{path}/recording.wav", "wb")
        recording_object.setnchannels(CHANNELS)
        recording_object.setsampwidth(p.get_sample_size(FORMAT))
        recording_object.setframerate(RATE)
        recording_object.writeframes(b"".join(frames))
        recording_object.close()
    except Exception as e:
        logging.error("Error during the audio recording.")
        logging.error(e)
        return False
    return True