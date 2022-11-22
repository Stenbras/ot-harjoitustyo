import wave,math
import numpy
import frequencyToNote as noty
import struct
from scipy.io import wavfile

    
def GetPeakAmplitude(a,b):
    fft_spectrum = numpy.fft.rfft(a)
    freq =numpy.fft.rfftfreq(a.size,d=1/b)
    for i,f in enumerate(freq):
        if f < 62 and f > 58:
            fft_spectrum[i] = 0.0
        if f < 21 or f > 20000:
            fft_spectrum[i] = 0.0
    fft_spectrum_abs =numpy.abs(fft_spectrum)
    return max(fft_spectrum_abs)

def GetAvarageAmplitude(a,b):
    fft_spectrum = numpy.fft.rfft(a)
    freq =numpy.fft.rfftfreq(a.size,d=1/b)
    for i,f in enumerate(freq):
        if f < 62 and f > 58:
            fft_spectrum[i] = 0.0
        if f < 21 or f > 20000:
            fft_spectrum[i] = 0.0
    fft_spectrum_abs =numpy.abs(fft_spectrum)
    return sum(fft_spectrum_abs)/len(fft_spectrum_abs)


#TODO split up into functions
def main():
    td=4
    amp=200000
    freqLimMax=5000
    freqLimMin=200
    maxFqsPerTd=5
    sensitivity = 0.005
    af = wave.open("testsound.wav","r")
    signal_ = numpy.frombuffer(af.readframes(-1), dtype="int16")
    framerate_= af.getframerate()
    duration_ = len(signal_)/framerate_
    j=0
    p= GetAvarageAmplitude(signal_,framerate_)
    print(p)
    k= GetPeakAmplitude(signal_,framerate_)
    print(k)
    print(str(int(len(signal_)/(framerate_/td))))

    for s in range(int(len(signal_)/(framerate_/td))-1):
        j+=int(framerate_/td)
        print(str(j)+" / "+str(len(signal_)))
        time_ = numpy.linspace(start=j,stop=int(j+framerate_/td),num=int(framerate_/td))
        time_ =time_.astype(int)

        fft_spectrum = numpy.fft.rfft(signal_[time_],)
        freq =numpy.fft.rfftfreq(time_.size,d=1/framerate_)
        
        for i,f in enumerate(freq):
            if f < freqLimMin or f > freqLimMax:
                fft_spectrum[i] = 0.0
                
        fft_spectrum_abs =numpy.abs(fft_spectrum)
        frames=int(framerate_/td)
        tdDur=frames/framerate_
        print("length td: "+str(tdDur))
        print("length frames td: "+str(frames))
        
        frqPerTD=0
        freqSet= set()
        for i,f in enumerate(fft_spectrum_abs):
            if numpy.round(f) > k*sensitivity:
                if frqPerTD>=maxFqsPerTd:
                    break
                note= noty.GetFrequencyNote(numpy.round(freq[i],1))
                frqPerTD +=1
                print("Note: "+ str(note))
                
        print("---------------------------------------------------------------")
    g=numpy.linspace(start=0,stop=duration_,num=int(framerate_))



if __name__ =="__main__":
    main()
