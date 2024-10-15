import numpy as np
import pydub
import pydub.playback
from pydub import AudioSegment


def envelope_sample(sample_array):
    # Sample to 100 Hz
    n = 320
    sampled = np.zeros(sample_array.size // 160, dtype=np.int8)
    # print(sampled.size)
    magnitudes = np.abs(sample_array)
    max_amplitude = np.max(magnitudes)
    # print(max_amplitude)
    for i in range(magnitudes.size // n):
        peak = np.max(magnitudes[i * n : (i + 1) * n])
        sampled[2 * i] = peak / (max_amplitude // 127)
        sampled[2 * i + 1] = -peak / (max_amplitude // 127)
    # print("Looped")
    return sampled

playback = None

def play_audio(sample):
    playback = pydub.playback.play(AudioSegment.from_mp3(sample))
    
def pause_audio():
    #playback.stop()
    return
