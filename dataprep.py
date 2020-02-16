import math as m
def read_osu(name):
    f = open(name, 'r')
    osufile = []
    for line in f:
        osufile.append(line)
    omap = osumap(osufile)
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
    eventType = ''  # (String or Integer): Type of the event. Some events may be referred to by either a name or a number.
    startTime = 0  # (Integer): Start time of the event, in milliseconds from the beginning of the beatmap's audio. For events that do not use a start time, the default is 0.
    eventParams = []  # (Comma-separated list): Extra parameters specific to the event's type.
    def __init__(self,eventType,startTime,eventParams):
        self.eventType = eventType
        self.startTime = int(startTime)
        self.eventParams = eventParams
        
class timingpoint():
    time = 0   #(Integer): Start time of the timing section, in milliseconds from the beginning of the beatmap's audio. The end of the timing section is the next timing point's time (or never, if this is the last timing point).
    beatLength = 0   #beatLength (Decimal): This property has two meanings:
                                #*For uninherited timing points, the duration of a beat, in milliseconds.
                                #*For inherited timing points, a negative inverse slider velocity multiplier, as a percentage. For example, -50 would make all sliders in this timing section twice as fast as SliderMultiplier.
    meter = 0    #(Integer): Amount of beats in a measure. Inherited timing points ignore this property.
    sampleSet = 0   #(Integer): Default sample set for hit objects (0 = beatmap default, 1 = normal, 2 = soft, 3 = drum).
    sampleIndex = 0   #(Integer): Custom sample index for hit objects. 0 indicates osu!'s default hitsounds.
    volume = 0   # Volume percentage for hit objects.
    uninherited = 0   #(0 or 1): Whether or not the timing point is uninherited.
    effects = 0   #(Integer): Bit flags that give the timing point extra effects. See the effects section.
    def __init__(self,time,beatLength,meter,sampleSet,sampleIndex,volume,uninherited,effects):
        self.time = int(time)
        self.beatLength = int(beatLength)
        self.meter = int(meter)
        self.sampleSet = int(sampleSet)
        self.sampleIndex = int(sampleIndex)
        self.volume = int(volume)
        self.uninherited = int(uninherited)
        self.effects = int(effects)
        
        
        
class background():
    filename = '' #filename (String): Location of the background image relative to the beatmap directory. Double quotes are usually included surrounding the filename, but they are not required.
    offset_x = 0   #Offset in osu! pixels from the center of the screen. For example, an offset of 50,100 would have the background shown 50 osu! pixels to the right and 100 osu! pixels down from the center of the screen. If the offset is 0,0, writing it is optional.
    offset_y = 0
    img = 0
    def __init__(self,filename,offset_x,offset_y, img):
        self.filename = filename
        self.offset_x = int(offset_x)
        self.offset_y = int(offset_y)
        self.img = img
        
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
    CircleSize = 4    #Decimal	CS setting (0–10)
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
    beatLength = 0
    offset = 0
    version = 0
    bg = background(0,0,0,0)
    multibpm = 0
    def __init__(self,file):
        for i in range(len(file)):
            cur = file[i]
            #print(cur)
            if(cur[:3] == "osu"): #version
                self.version = int(cur[-3:-1])
            if(cur == "[General]\n"):
                for j in range(i+1,len(file)):
                    cur = file[j]
                    
                    if(cur.count("AudioFilename") > 0):
                        self.AudioFilename = cur[cur.find(':') + 1:]
                    if(cur.count("AudioLeadIn") > 0):
                        self.AudioLeadIn = cur[cur.find(':') + 1:]
                    if(cur.count("AudioHash") > 0):
                        self.AudioHash = cur[cur.find(':') + 1:]
                    if(cur.count("PreviewTime") > 0):
                        self.PreviewTime = int(cur[cur.find(':') + 1:])
                    if(cur.count("Countdown") > 0):
                        self.Countdown = int(cur[cur.find(':') + 1:])
                    if(cur.count("SampleSet") > 0):
                        self.SampleSet = cur[cur.find(':') + 1:]
                    if(cur.count("StackLeniency") > 0):
                        self.StackLeniency = float(cur[cur.find(':') + 1:])
                    if(cur.count("Mode") > 0):
                        self.Mode = int(cur[cur.find(':') + 1:])
                    if(cur.count("LetterboxInBreaks") > 0):
                        self.LetterboxInBreaks = int(cur[cur.find(':') + 1:])
                    if(cur.count("StoryFireInFront") > 0):
                        self.StoryFireInFront = int(cur[cur.find(':') + 1:])
                    if(cur.count("UseSkinSprites") > 0):
                        self.UseSkinSprites = int(cur[cur.find(':') + 1:])
                    if(cur.count("AlwaysShowPlayfield") > 0):
                        self.AlwaysShowPlayfield = int(cur[cur.find(':') + 1:])
                    if(cur.count("OverlayPosition") > 0):
                        self.OverlayPosition = cur[cur.find(':') + 1:]
                    if(cur.count("SkinPreference") > 0):
                        self.SkinPreference = cur[cur.find(':') + 1:]
                    if(cur.count("EpilepsyWarning") > 0):
                        self.EpilepsyWarning = int(cur[cur.find(':') + 1:])
                    if(cur.count("CountdownOffset") > 0):
                        self.CountdownOffset = int(cur[cur.find(':') + 1:])
                    if(cur.count("SpecialStyle") > 0):
                        self.SpecialStyle = int(cur[cur.find(':') + 1:])
                    if(cur.count("WidescreenStoryboard") > 0):
                        self.WidescreenStoryboard = int(cur[cur.find(':') + 1:])
                    if(cur.count("SamplesMatchPlaybackRate") > 0):
                        self.SamplesMatchPlaybackRate = int(cur[cur.find(':') + 1:])
                print("ok")
            if(cur == "[Editor]\n"):
                for j in range(i+1,len(file)):
                    cur = file[j]
                    if(cur.count("Bookmarks") > 0):
                        self.Bookmarks = cur[cur.find(':') + 1:]
                    if(cur.count("DistanceSpacing") > 0):
                        self.DistanceSpacing = float(cur[cur.find(':') + 1:])
                    if(cur.count("BeatDivisor") > 0):
                        self.BeatDivisor = float(cur[cur.find(':') + 1:])
                    if(cur.count("GridSize") > 0):
                        self.GridSize = int(cur[cur.find(':') + 1:])
                    if(cur.count("TimelineZoom") > 0):
                        self.TimelineZoom = float(cur[cur.find(':') + 1:])
                print("ok")
            if(cur == "[Metadata]\n"):
                for j in range(i+1,len(file)):
                    cur = file[j]
                    if(cur.count("Title") > 0):
                        self.Title = cur[cur.find(':') + 1:]
                    if(cur.count("TitleUnicode") > 0):
                        self.TitleUnicode = cur[cur.find(':') + 1:]
                    if(cur.count("Artist") > 0):
                        self.Artist = cur[cur.find(':') + 1:]
                    if(cur.count("ArtistUnicode") > 0):
                        self.ArtistUnicode = cur[cur.find(':') + 1:]
                    if(cur.count("Version") > 0):
                        self.Version = cur[cur.find(':') + 1:]
                    if(cur.count("Source") > 0):
                        self.Source = cur[cur.find(':') + 1:]
                    if(cur.count("Tags") > 0):
                        self.Tags = cur[cur.find(':') + 1:]
                    if(cur.count("BeatmapID") > 0):
                        self.BeatmapID = int(cur[cur.find(':') + 1:])
                    if(cur.count("BeatmapSetID") > 0):
                        self.BeatmapSetID = int(cur[cur.find(':') + 1:])
                print("ok")
            if(cur == "[Difficulty]\n"):
                for j in range(i+1,len(file)):
                    cur = file[j]
                    if(cur.count("HPDrainRate") > 0):
                        self.HPDrainRate = float(cur[cur.find(':') + 1:])
                    if(cur.count("CircleSize") > 0):
                        self.CircleSize = float(cur[cur.find(':') + 1:])
                    if(cur.count("OverallDifficulty") > 0):
                        self.OverallDifficulty = float(cur[cur.find(':') + 1:])
                    if(cur.count("ApproachRate") > 0):
                        self.ApproachRate = float(cur[cur.find(':') + 1:])
                    if(cur.count("SliderMultiplier") > 0):
                        self.SliderMultiplier = float(cur[cur.find(':') + 1:])
                    if(cur.count("SliderTickRate") > 0):
                        self.SliderTickRate = float(cur[cur.find(':') + 1:])
                print("ok")
            if(cur == "[Events]\n"):
                 for j in range(i+1,len(file)):
                    cur = file[j]
                    if((cur[:2] != '//') and (len(cur.split(',')) > 2)):
                        #print("i'm gonna read it - ", cur)
                        self.events.append(event(cur.split(',')[0],cur.split(',')[1],cur.split(',')[2:]))
                        if((cur.split(',')[0] == '0') and (cur.split(',')[1] == '0')):
                            self.bg = background(cur.split(',')[2],cur.split(',')[3],cur.split(',')[4],0)
                    if(file[j + 1] == "[TimingPoints]\n"):
                        break
                 print(len(self.events)," events")
                    
                
            
     
            if(cur == "[TimingPoints]\n"):
                for j in range(i+1,len(file)):
                    cur = file[j]
                    if((cur[:2] != '//') and (len(cur.split(',')) > 7)):
                        self.timingpoints.append(timingpoint(cur.split(',')[0],
                                                             cur.split(',')[1],
                                                             cur.split(',')[2],
                                                             cur.split(',')[3],
                                                             cur.split(',')[4],
                                                             cur.split(',')[5],
                                                             cur.split(',')[6],
                                                             cur.split(',')[7],))
                print(len(self.timingpoints)," timing points")
                
                    
                    
            if(cur == "[Colours]\n"):
                print("mb later")
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
                        n = note(m.floor((hit.x * self.CircleSize)*(1/512)),hit.time,hit.endTime - hit.time)
                    else:
                        n = note(m.floor((hit.x * self.CircleSize)*(1/512)),hit.time,0)
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
          
