import osumap as om
import numpy as np
import h5py as h5

def read_music(name):
    return 0
def convert_osu(omap):
    offset = 0
    division = 4
    if (omap.multibpm == 0):
        shape = (m.floor(division * omap.notes[len(omap.notes) - 1].time/omap.timingpoints[0].beatLength + offset * omap.timingpoints[0].beatLength) + 1, int(omap.CircleSize))
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
def convert_music():
    
    return 0
def make_dataset():
    return 0
def get_files_list():
    return 0
          