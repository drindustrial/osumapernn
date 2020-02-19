import osumap as om
import numpy as np
import h5py as h5
import pydub
from pydub import AudioSegment
import matplotlib.pyplot as plt
import pyfftw

division = 4
pydub.AudioSegment.ffmpeg  = "D:\\Program files\\ffmpeg\\bin"

def read_music(name):
    return 0
def convert_osu(omap):
    offset = 0
    
    if (omap.multibpm == 0):
        shape = (m.floor(division * (omap.notes[len(omap.notes) - 1].time - omap.timingpoints[0].time)/omap.timingpoints[0].beatLength + offset * omap.timingpoints[0].beatLength), int(omap.CircleSize))
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
def convert_music(osuf):
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
    print("size =",len(samples))
    '''window_size = m.floor(osuf.timingpoints[0].beatLength * (frame_rate / (division * 1000))) #that's wrong every 1000 osu frames, offset increase on 78ms
    print("window size =", window_size)
    print("time mtime otime",time_converter(
                                    b = osuf.timingpoints[0].beatLength,
                                    d = division,
                                    of = osuf.timingpoints[0].time,
                                    fr = frame_rate,
                                    t = osuf.notes[len(osuf.notes) - 1].time/1000))
    fsample_count = (time_converter(
                                    b = osuf.timingpoints[0].beatLength,
                                    d = division,
                                    of = osuf.timingpoints[0].time,
                                    fr = frame_rate,
                                    t = (osuf.notes[len(osuf.notes) - 1].time - osuf.timingpoints[0].time)/1000)[1])
    print("windows count =",fsample_count/window_size)
    out = np.zeros((int(fsample_count/window_size),int(window_size)))'''
    window_size = 0# ms
    windows_count = 0
    
    '''
    plt.figure(1)
    plt.title("Signal Wave...")
    plt.plot(samples[sound.frame_rate * 25:sound.frame_rate * 27])
    plt.show()'''
    return 0
def make_dataset():
    return 0
def get_files_list():
    return 0
def time_converter( b, d, of, fr, t = -1.4588, mt = -1.4588, ot = -1.4588):
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