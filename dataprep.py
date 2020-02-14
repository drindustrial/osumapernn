import math as m
def read_osu(name):
    f = open(name, 'r')
    osufile = []
    for line in f:
        osufile.append(line)
    omap = osumap(osufile)
    print(osufile[105])
    version = 0
    return 0

class note():
    key = 0
    time = 0
    length = 0
    def __init__(self,key,time,leng):
        self.key = int(key)
        self.time = int(time)
        self.length = int(leng)
        pass
    def printall(self):
        print("key = ", self.key,"time = ", self.time,"length = ",self.length)
    
    
    
class hitobject():
    x = 0
    y = 0
    time = 0
    typeo = 0
    hitSound = 0
    endTime = 0
    hitSample = ''
    def __init__(self,x,y,time,typeo,hitSound,endTime,hitSample):
        self.x = int(x)
        self.y = int(y)
        self.time = int(time)
        self.typeo = int(typeo)
        self.hitSound = int(hitSound)
        self.endTime = int(endTime)
        self.hitSample = hitSample
        pass    
    

class osumap():
    #[General]	General information about the beatmap
    AudioFilename = ''        #String	Location of the audio file relative to the current folder	
    AudioLeadIn = ''     #Integer	Milliseconds of silence before the audio starts playing	0
    AudioHash = ''     #String	Deprecated	
    PreviewTime = 0    #Integer	Time in milliseconds when the audio preview should start	-1
    Countdown = 0  #Integer	Speed of the countdown before the first hit object (0 = no countdown, 1 = normal, 2 = half, 3 = double)	1
    SampleSet = '' #String	Sample set that will be used if timing points do not override it (Normal, Soft, Drum)	Normal
    StackLeniency = 0   #Decimal	Multiplier for the threshold in time where hit objects placed close together stack (0–1)	0.7
    Mode = 0   #Integer	Game mode (0 = osu!, 1 = osu!taiko, 2 = osu!catch, 3 = osu!mania)	0
    LetterboxInBreaks = 0   #0 or 1	Whether or not breaks have a letterboxing effect	0
    StoryFireInFront = 0   #0 or 1	Deprecated	1
    UseSkinSprites = 0   #0 or 1	Whether or not the storyboard can use the user's skin images	0
    AlwaysShowPlayfield = 0  #0 or 1	Deprecated	0
    OverlayPosition = ''  #String	Draw order of hit circle overlays compared to hit numbers (NoChange = use skin setting, Below = draw overlays under numbers, Above = draw overlays on top of numbers)	NoChange
    SkinPreference = ''   #String	Preferred skin to use during gameplay	
    EpilepsyWarning = 0    #0 or 1	Whether or not a warning about flashing colours should be shown at the beginning of the map	0
    CountdownOffset = 0   #Integer	Time in beats that the countdown starts before the first hit object	0
    SpecialStyle = 0   #0 or 1	Whether or not the "N+1" style key layout is used for osu!mania	0
    WidescreenStoryboard = 0   #0 or 1	Whether or not the storyboard allows widescreen viewing	0
    SamplesMatchPlaybackRate = 0   #0 or 1	Whether or not sound samples will change rate when playing with speed-changing mods
    
    #[Editor]	Saved settings for the beatmap editor
    Bookmarks  = ''  #Comma-separated list of integers	Time in milliseconds of bookmarks
    DistanceSpacing = 0  #Decimal	Distance snap multiplier
    BeatDivisor = 0  #Decimal	Beat snap divisor
    GridSize = 0  #Integer	Grid size
    TimelineZoom = 0  #Decimal	Scale factor for the object timeline
    
    #[Metadata]	Information used to identify the beatmap
    Title = ''   #String	Romanised song title
    TitleUnicode = ''   #String	Song title
    Artist = ''   #String	Romanised song artist
    ArtistUnicode = ''   #String	Song artist
    Creator = ''   #String	Beatmap creator
    Version = ''   #String	Difficulty name
    Source = ''   #String	Original media the song was produced for
    Tags = ''   #Space-separated list of strings	Search terms
    BeatmapID = 0    #Integer	Beatmap ID
    BeatmapSetID = 0    #Integer	Beatmapset ID
    
    #[Difficulty]	Difficulty settings
    HPDrainRate = 0    #Decimal	HP setting (0–10)
    CircleSize = 0    #Decimal	CS setting (0–10)
    OverallDifficulty = 0    #Decimal	OD setting (0–10)
    ApproachRate = 0    #Decimal	AR setting (0–10)
    SliderMultiplier = 0    #Decimal	Base slider velocity in hecto-osu! pixels per beat
    SliderTickRate = 0    #Decimal	Amount of slider ticks per beat
    
    #[Events]	Beatmap and storyboard graphic events
    events = []
    #[TimingPoints]	Timing and control points
    timingpoints = []
    #[Colours]	Combo and skin colours
    colours = []
    #[HitObjects]
    hitobjects = []
    notes = []
    bpm = 0
    offset = 0
    version = 0
    def __init__(self,file):
        for i in range(len(file)):
            cur = file[i]
            print(cur)
            if(cur[:3] == "osu"):
                self.version = int(cur[-3:-1])
            if(cur == "[General]\n"):
                for j in range(i+1,len(file)):
                print("ok")
            if(cur == "[Editor]\n"):
                print("ok")
            if(cur == "[Metadata]\n"):
                print("ok")
            if(cur == "[Difficulty]\n"):
                print("ok")
            if(cur == "[Events]\n"):
                print("ok")
            if(cur == "[TimingPoints]\n"):
                print("ok")
            if(cur == "[Colours]\n"):
                print("ok")
            if(cur == "[HitObjects]\n"):
                for j in range(i+1,len(file)):
                    cur = file[j]
                    hit = hitobject(cur.split(',')[0],
                                    cur.split(',')[1],
                                    cur.split(',')[2],
                                    cur.split(',')[3],
                                    cur.split(',')[4],
                                    cur.split(',')[5].split(':')[0],
                                    cur.split(',')[5])
                    if(hit.typeo == 128):
                        n = note(m.floor(hit.x * self.CircleSize / 512),hit.time,hit.endTime - hit.time)
                    else:
                        n = note(m.floor(hit.x * self.CircleSize / 512),hit.time,0)
                    self.hitobjects.append(hit)
                    self.notes.append(n)
                    n.printall()
        
            
        


def read_music(name):
    return 0
def convert_osu():
    return 0
def convert_music():
    return 0
def make_dataset():
    return 0
def get_files_list():
    return 0
          

