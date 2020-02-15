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
    
class event():
    eventType = ''
    startTime = 0
    eventParams = []
    def __init__(self,eventType,startTime,eventParams):
        self.eventType = eventType
        self.startTime = startTime
        self.eventParams = eventParams
        
    
    
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
            if(cur[:3] == "osu"): #version
                self.version = int(cur[-3:-1])
            if(cur == "[General]\n"):
                for j in range(i+1,len(file)):
                    cur = file[j]
                    if(cur.count("AudioFilename") > 0):
                        self.AudioFilename = cur[cur.find(':') + 2:]
                    if(cur.count("AudioLeadIn") > 0):
                        self.AudioLeadIn = cur[cur.find(':') + 2:]
                    if(cur.count("AudioHash") > 0):
                        self.AudioHash = cur[cur.find(':') + 2:]
                    if(cur.count("PreviewTime") > 0):
                        self.PreviewTime = cur[cur.find(':') + 2:]
                    if(cur.count("Countdown") > 0):
                        self.Countdown = cur[cur.find(':') + 2:]
                    if(cur.count("SampleSet") > 0):
                        self.SampleSet = cur[cur.find(':') + 2:]
                    if(cur.count("StackLeniency") > 0):
                        self.StackLeniency = cur[cur.find(':') + 2:]
                    if(cur.count("Mode") > 0):
                        self.Mode = cur[cur.find(':') + 2:]
                    if(cur.count("LetterboxInBreaks") > 0):
                        self.LetterboxInBreaks = cur[cur.find(':') + 2:]
                    if(cur.count("StoryFireInFront") > 0):
                        self.StoryFireInFront = cur[cur.find(':') + 2:]
                    if(cur.count("UseSkinSprites") > 0):
                        self.UseSkinSprites = cur[cur.find(':') + 2:]
                    if(cur.count("AlwaysShowPlayfield") > 0):
                        self.AlwaysShowPlayfield = cur[cur.find(':') + 2:]
                    if(cur.count("OverlayPosition") > 0):
                        self.OverlayPosition = cur[cur.find(':') + 2:]
                    if(cur.count("SkinPreference") > 0):
                        self.SkinPreference = cur[cur.find(':') + 2:]
                    if(cur.count("EpilepsyWarning") > 0):
                        self.EpilepsyWarning = cur[cur.find(':') + 2:]
                    if(cur.count("CountdownOffset") > 0):
                        self.CountdownOffset = cur[cur.find(':') + 2:]
                    if(cur.count("SpecialStyle") > 0):
                        self.SpecialStyle = cur[cur.find(':') + 2:]
                    if(cur.count("WidescreenStoryboard") > 0):
                        self.WidescreenStoryboard = cur[cur.find(':') + 2:]
                    if(cur.count("SamplesMatchPlaybackRate") > 0):
                        self.SamplesMatchPlaybackRate = cur[cur.find(':') + 2:]
                print("ok")
            if(cur == "[Editor]\n"):
                for j in range(i+1,len(file)):
                    cur = file[j]
                    if(cur.count("Bookmarks") > 0):
                        self.Bookmarks = cur[cur.find(':') + 2:]
                    if(cur.count("DistanceSpacing") > 0):
                        self.DistanceSpacing = cur[cur.find(':') + 2:]
                    if(cur.count("BeatDivisor") > 0):
                        self.BeatDivisor = cur[cur.find(':') + 2:]
                    if(cur.count("GridSize") > 0):
                        self.GridSize = cur[cur.find(':') + 2:]
                    if(cur.count("TimelineZoom") > 0):
                        self.TimelineZoom = cur[cur.find(':') + 2:]
                print("ok")
            if(cur == "[Metadata]\n"):
                for j in range(i+1,len(file)):
                    cur = file[j]
                    if(cur.count("Title") > 0):
                        self.Title = cur[cur.find(':') + 2:]
                    if(cur.count("TitleUnicode") > 0):
                        self.TitleUnicode = cur[cur.find(':') + 2:]
                    if(cur.count("Artist") > 0):
                        self.Artist = cur[cur.find(':') + 2:]
                    if(cur.count("ArtistUnicode") > 0):
                        self.ArtistUnicode = cur[cur.find(':') + 2:]
                    if(cur.count("Version") > 0):
                        self.Version = cur[cur.find(':') + 2:]
                    if(cur.count("Source") > 0):
                        self.Source = cur[cur.find(':') + 2:]
                    if(cur.count("Tags") > 0):
                        self.Tags = cur[cur.find(':') + 2:]
                    if(cur.count("BeatmapID") > 0):
                        self.BeatmapID = cur[cur.find(':') + 2:]
                    if(cur.count("BeatmapSetID") > 0):
                        self.BeatmapSetID = cur[cur.find(':') + 2:]
                print("ok")
            if(cur == "[Difficulty]\n"):
                for j in range(i+1,len(file)):
                    cur = file[j]
                    if(cur.count("HPDrainRate") > 0):
                        self.HPDrainRate = cur[cur.find(':') + 2:]
                    if(cur.count("CircleSize") > 0):
                        self.CircleSize = cur[cur.find(':') + 2:]
                    if(cur.count("OverallDifficulty") > 0):
                        self.OverallDifficulty = cur[cur.find(':') + 2:]
                    if(cur.count("ApproachRate") > 0):
                        self.ApproachRate = cur[cur.find(':') + 2:]
                    if(cur.count("SliderMultiplier") > 0):
                        self.SliderMultiplier = cur[cur.find(':') + 2:]
                    if(cur.count("SliderTickRate") > 0):
                        self.SliderTickRate = cur[cur.find(':') + 2:]
                print("ok")
            if(cur == "[Events]\n"):
                 for j in range(i+1,len(file)):
                    cur = file[j]
                    if(cur.)
                    self.events.append(event(cur.split(',')[0],cur.split(',')[1],cur.split(',')[2:]))
     
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
          
