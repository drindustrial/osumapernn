from osumap import read_osu, note, event, timingpoint, hitobject, osumap
import numpy as np
import h5py as h5
import pydub
import math as m 
from pydub import AudioSegment
import matplotlib.pyplot as plt
import pyfftw
from scipy.fftpack import fft
from scipy.interpolate import interp1d

eps = 0.001
division = 4
#pydub.AudioSegment.ffmpeg  = "D:\\Program files\\ffmpeg\\bin"

def read_music(name):
    return 0
def convert_osu(omap):
    offset = 0
    
    if (omap.multibpm == 0):
        shape = (m.floor(division * (omap.notes[len(omap.notes) - 1].time - omap.timingpoints[0].time + omap.notes[len(omap.notes) - 1].length)/omap.timingpoints[0].beatLength + offset * omap.timingpoints[0].beatLength) + 8, int(omap.CircleSize))
        print(shape)
        binosumap = np.zeros(shape,np.int)
        stats = [0, 0]
        for n in omap.notes:
            stats[0] = stats[0] + 1
            note1 = n
            binosumap[time_converter(omap.timingpoints[0].beatLength,division,omap.timingpoints[0].time,10000,t = note1.time/1000)[2]][note1.key] = 1
            note1.length = m.floor((division * note1.length)/omap.timingpoints[0].beatLength)
            '''while(note1.length > 0):
                binosumap[m.floor(division * note1.time/omap.timingpoints[0].beatLength)][note1.key] = 1
                note1.length -= 1
                stats[1] += 1'''
        print("notes, lnparts",stats)
        return binosumap
    
    return -1
def convert_music(osuf, windows_count):
    sound = AudioSegment.from_mp3(osuf.AudioFilename)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(int((44100*200)/osuf.timingpoints[0].beatLength)) #window size in fftw will be the same and frame rate [4410(60 bpm),44100(300 bpm)]
    print("sound channels", sound.channels)
    frame_count = sound.frame_count()
    frame_rate = sound.frame_rate
    sample_width = sound.sample_width
    print("frame count:", frame_count,"\nframe rate: ",frame_rate,"\nsample width:",sample_width)
    #sound.export("test.wav", format="wav")
    samples = sound.get_array_of_samples()
    samples = np.array(samples)
    mus_offset = frame_rate * 50  #few zeros befor raw data music
    samples = np.append(np.zeros((mus_offset)), samples)
    samples = np.append(samples, np.zeros((mus_offset)))
    print("size =",len(samples))
    window_size = osuf.timingpoints[0].beatLength/division# ms
    print("window size =", int(window_size * frame_rate / 1000), "windows count", windows_count)
    out = np.zeros((int(windows_count),int(window_size * frame_rate / 2000)))
    print("out[1].shape =", len(out[1]))
    print("raw data mean =", samples.mean())
    for i in range(windows_count):
        window = np.zeros((int(window_size * frame_rate / 1000)))
        start_time = time_converter(b = osuf.timingpoints[0].beatLength,
                                    d = division,
                                    of = osuf.timingpoints[0].time,
                                    fr = frame_rate,
                                    ot = i)[1]
        #print("window - [",int(start_time - window_size * frame_rate / 2000 + mus_offset),' , ',int(start_time + window_size * frame_rate / 2000 + mus_offset))
        window = samples[int(start_time + mus_offset):int(start_time + window_size * frame_rate / 1000 + mus_offset)]
        #fftw
        #print("window mean =", window.mean())
        a = pyfftw.empty_aligned(len(window), dtype='complex128')
        b = pyfftw.empty_aligned(len(window), dtype='complex128')
        a[:] = np.array(window) + 1j*np.zeros((len(window)))
        b = fft(a)
        c = abs(b) + eps
        #print("len(window)", len(window))
        #print("len(c)", len(c))
        #print("c mean =", c.mean())
        out[i] = np.log(c[:int(len(window)/2)])
        '''x = np.linspace(0, 10, num=25, endpoint=True)
        y = out[i][:25]
        print("x len = ",len(x),"y len = ", len(y))
        f = interp1d(x, y)
        f2 = interp1d(x, y, kind='nearest')
        xnew = np.linspace(0, 10, num=41, endpoint=True)
        plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
        plt.legend(['data', 'linear', 'nearest'], loc='best')
        plt.show()
        return -1'''
           
    plt.figure(figsize=(15,8))
    out1 = out.transpose()
    print("shapes out out1",out.shape[0],out.shape[1], " , ",out1.shape[0],out1.shape[1])
    plt.imshow(out1, interpolation="nearest", origin="upper")
    plt.colorbar()
    plt.show()


    '''
    
        break 
    '''
    return out
def make_dataset():
    return 0
def get_files_list():
    return 0
def time_converter( b, d, of, fr, t = -1.4588, mt = -1.4588, ot = -1.4588):
    #print(" b, d, of, fr, ot", b, d, of, fr, ot)
    if ((t == -1.4588) and (mt == -1.4588)):
        otime = ot
        time = (ot * (b/d) + of) / 1000
        mtime = time * fr
    if ((ot == -1.4588) and (mt == -1.4588)):
        time = t
        mtime = t * fr
        otime = (t * 1000 - of) * (d/b)
    if ((ot == -1.4588) and (t == -1.4588)):
        mtime = mt
        time = mt/fr
        otime = (time * 1000 - of) * (d/b)
        
    return m.floor(time), m.floor(mtime), m.floor(otime)

def bool_to_omap(boolmap):
    notes = []
    for i in range(boolmap.shape[0]):
        for j in range(boolmap.shape[1]):
            if(boolmap[i][j] > 0.8):
                n = note(j,time_converter(314.1361256,4,366%314.1361256,10000,ot = i)[0] * 1000,0)
                notes.append(n)
                n.printall()
    return notes
                
def out_osu_file(notes, name):
    f = open(name, "w")
    for n in notes:
        f.write(str(m.floor((n.key + 0.5)*512/4)))
        f.write(',192,')
        f.write(str(n.time))
        f.write(",1,0,0:0:0:0:\n")
    f.close()
            