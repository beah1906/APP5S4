import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from scipy import signal
from scipy.fft import *
from scipy.io import wavfile

class Wave:
    # initialisation
    def __init__(self, wav_fname=None):
        self.export_signal = (None, None, None)
        self.sinusFFT = None
        self.frequency = None
        self.sinusFFTdB = None
        self.peak_32 = None
        self.fname = wav_fname
        if self.fname is not None:
            self.read_wav()
            plt.plot(self.time, self.signal)
            plt.title("LA# signal")
            plt.show()

    #lecture
    def read_wav(self):
        self.samplerate, self.signal = wavfile.read(self.fname)
        self.length = self.signal.shape[0] / self.samplerate                             ##secondes
        self.N = self.signal.shape[0]
        print("N = " + str(self.signal.shape[0]))
        self.time = np.linspace(0., self.length, self.signal.shape[0], endpoint=False)
        return self.samplerate, self.signal, self.time, self.length

    # ecriture
    def write_wav(self, name, data):
        wavfile.write(name + ".wav", self.samplerate, data)

    #fenetre hanning
    def hanning(self):
        self.window = np.hanning(160000)
        plt.plot(self.window)
        plt.title("hanning window")
        plt.show()

    def windowing(self):
        self.windowed = fft(self.signal*self.window)

        axe_x = ((np.arange(0, (len(self.windowed))) / len(self.signal))*self.samplerate)
        plt.plot(axe_x, 20*np.log10(abs(self.windowed)))
        plt.xlabel("Frequence (Hz)")
        plt.ylabel("Amplitude (dB)")
        plt.xlim(0,20000)
        plt.title("signal windowed")
        plt.show()
        #xf = fftfreq(N, T)[:N // 2]
        #plt.plot(self.time, abs(self.signal), 'b')
if __name__ == '__main__':
    print('App5 DSP')
    LAd = Wave("note_guitare_LAd.wav")
    LAd.hanning()
    LAd.windowing()
   # print('Sample rate = ', Wave.samplerate)
