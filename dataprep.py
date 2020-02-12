def read_osu(name):
    f = open(name, 'r')
    print(f.readline())
    osufile = []
    for line in f:
        osufile.append(line)
        print(line)
    print(osufile[105])
    version = 0
    return 0

class key():
    key = 0
    time = 0
    def __init__(self,key,time):
        self.key = key
        self.time = time
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
    
    #[Metadata]	Information used to identify the beatmap
    
    #[Difficulty]	Difficulty settings
    
    #[Events]	Beatmap and storyboard graphic events
    
    #[TimingPoints]	Timing and control points
    
    #[Colours]	Combo and skin colours
    
    #[HitObjects]
    
    def __init__(self):
        """Constructor"""
        


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
          
