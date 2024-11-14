import pyaudio
from scipy.io import wavfile

sr, wdata=wavfile.read('/home/itibcn/Desktop/MachineLearningClassic/PracticaAudio/AudioClasse.wav')

p = pyaudio.PyAudio()
stream = p.open(format = p.get_format_from_width(1), channels = 1, rate = sr, output = True)
stream.write(wdata)
stream.stop_stream()
stream.close()
p.terminate()