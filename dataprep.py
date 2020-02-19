import osumap as om
import numpy as np
import h5py as h5
import pydub
from pydub import AudioSegment
import matplotlib.pyplot as plt
import pyfftw
from scipy.fftpack import fft

division = 4
pydub.AudioSegment.ffmpeg  = "D:\\Program files\\ffmpeg\\bin"

def read_music(name):
    return 0
def convert_osu(omap):
    offset = 0
    
    if (omap.multibpm == 0):
        shape = (m.floor(division * (omap.notes[len(omap.notes) - 1].time - omap.timingpoints[0].time + omap.notes[len(omap.notes) - 1].length)/omap.timingpoints[0].beatLength + offset * omap.timingpoints[0].beatLength) + 2, int(omap.CircleSize))
        print(shape)
        binosumap = np.zeros(shape,np.bool)
        stats = [0, 0]
        for n in omap.notes:
            stats[0] = stats[0] + 1
            note = n
            note.length = m.floor((division * note.length)/omap.timingpoints[0].beatLength)
            while(note.length > 0):
                binosumap[m.floor(division * note.time/omap.timingpoints[0].beatLength)][note.key] = 1
                note.length -= 1
                stats[1] += 1
        print("notes, lnparts",stats)
        return binosumap
    
    return -1
def convert_music(osuf, windows_count):
    sound = AudioSegment.from_mp3(osuf.AudioFilename)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(10000)
    print("sound channels", sound.channels)
    frame_count = sound.frame_count()
    frame_rate = sound.frame_rate
    sample_width = sound.sample_width
    print("frame count:", frame_count,"\nframe rate: ",frame_rate,"\nsample width:",sample_width)
    #sound.export("test.wav", format="wav")
    samples = sound.get_array_of_samples()
    samples = np.array(samples)
    mus_offset = frame_rate * 50
    samples = np.append(np.zeros((mus_offset)), samples)
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
        window = samples[int(start_time - window_size * frame_rate / 2000 + mus_offset):int(start_time + window_size * frame_rate / 2000 + mus_offset)]
        #fftw
        #print("window mean =", window.mean())
        a = pyfftw.empty_aligned(len(window), dtype='complex128')
        b = pyfftw.empty_aligned(len(window), dtype='complex128')
        a[:] = np.array(window) + 1j*np.zeros((len(window)))
        b = fft(a)
        c = abs(b)
        #print("c mean =", c.mean())
        out[i] = np.log(c[:int(len(window)/2)])
           
    plt.figure(figsize=(15,8))
    plt.imshow(out, interpolation="nearest", origin="upper")
    plt.colorbar()
    plt.show()


    '''
    
        break 
    '''
    return 0
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