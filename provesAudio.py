import json
import numpy as np #aqui hi ha les estructures de dades que faig servir
import matplotlib.pyplot as plt #per dibuixar
import scipy.io as sio #el input output d'audio (wavfile.read)
from IPython.display import Audio #el reproductor d'audio
from numpy.fft import fft, ifft #podria fer numpy.fft en comptes de fer aquest import
from wav2vec import cutvowel, wav2vec #el nostre modul

llistavocals = []
llistamaxims = []
llista3 = []

def frequencia(muestra, Fs, muestraTotal):
    return muestra * Fs/muestraTotal

def mostraFreq(freq, Fs, muestraTotal):
    return freq * muestraTotal / Fs

for select in range(len(data)): #Parametre del dataset

    print(data[select]['Vocal'])
    print(' ')
    start = float(data[select]["Start"])
    print(start)
    end=float(data[select]["End"])
    print(end)
    print(len(audio)) #per mirar si és estero o mono

    llistavocals.append(data[select]['Vocal'])

    Fs, audio = sio.wavfile.read("/home/itibcn/Desktop/MachineLearningClassic/PracticaAudio/AudioClasse.wav")
    #Fs, audio = cutvowel("vowels/alex.wav"), float(data[select]["start"]), float(data[select]["end"]))
    cut = audio[int(start*Fs):int(end*Fs)]

    print("Llargada audio: " + str(len(cut)))
    #print(Fs)
    #print(type(audio))
    #print(type(audio[0]))

    #start=4.4 #realment ho agafariem del fitxer json
    #end=4.6

    #framesentrada = int(float(start)*Fs) #calculem la mostra d'entrada
    #framesalida = int(float(end)*Fs)
    #cut=audio[framesentrada:framesalida] #retallem

    #cut = audio
    #data[select]["vocal"]
   
    print(' ')

    #Audio retallat
    Audio(cut, rate=Fs)

    #dibuixem l'audio retallat
    #plt.figure()
    #plt.plot(cut)
    #plt.title("")
    #plt.xlabel("time")
    #plt.ylabel("Amplitud")
    #plt.show()

    #Dificil entendre algo. mirem fourier
    fourier = fft(cut)
    #plt.figure()
    #plt.plot(fourier)
    #plt.title("FFT")
    #plt.xlabel("frequency")
    #plt.ylabel("Amplitud")
    #plt.show()

    #només importa el que pasa a prop de zero
    #Fsmall = fourier[0:300]
    Fsmall = fourier[0:int(mostraFreq(3000, Fs, len(cut)))]
    plt.figure()
    plt.plot(Fsmall)
    plt.title("FFT")
    plt.xlabel("frequency")
    plt.ylabel("Amplitud")
    plt.show()

    #No m'importa la fase, només el módul.
    toprocess = np.sqrt((np.real(Fsmall)**2+np.imag(Fsmall)**2))
    #plt.figure()
    #plt.plot(toprocess)
    #plt.show()


    #-----------------------------------------------------------------------
    #Aplico un filtre per quedar eliminar soroll

    filter = int(mostraFreq(200, Fs, len(cut)))
    out = np.zeros(len(toprocess)-filter, dtype=np.float64)
    for i in range(len(toprocess)-filter):
        for j in range(filter):
            out[i] += toprocess[i+j]

            
    out[0:15] = 0
            
    #plt.figure()
    #plt.plot(out)
    #plt.show()

    np.argmax(out)

    #----------------------------------------------------------------------

    #filter2 = 25
    filter2 = int(mostraFreq(200, Fs, len(cut)))
    #print("FILTRO2: " + str(filter2))
    
    maxim1 = np.argmax(out)
    print(maxim1)

    filmin = filter2
    if maxim1 < filter2:
        filmin = maxim1

    out[maxim1-filmin:maxim1+filter2] = 0
    #plt.figure()
    #plt.plot(out)
    #plt.show()

    maxim2 = np.argmax(out)
    #print(maxim2)

    out[maxim2-filter2:maxim2+filter2] = 0
    #plt.figure()
    #plt.plot(out)
    #plt.show()


    maxim3 = np.argmax(out)
    #print(maxim3)

    out[maxim3-filter2:maxim3+filter2] = 0
    #plt.figure()
    #plt.plot(out)
    #plt.show()

    #---------------------------------------------------------------------

    print(fourier.size)
    print(Fs)
    print(cut)
    print((maxim1)*Fs/fourier.size, "Hz")
    print((maxim2)*Fs/fourier.size, "Hz")
    print((maxim3)*Fs/fourier.size, "Hz")
    
    llistamaxims.append(maxim1)
    llistamaxims.append(maxim2)
    llistamaxims.append(maxim3)

    print(' ')


print(llistavocals)
print(llistamaxims)
print(len(llistavocals))
print(len(llistamaxims))

"""
if data[select['Vocal']] == 'A':
    print('A')
elif data[select['Vocal']] == 'E':
    print('E')
elif data[select['Vocal']] == 'I':
    print('I')
elif data[select['Vocal']] == 'O':
    print('O')
elif data[select['Vocal']] == 'U':
    print('U')
"""