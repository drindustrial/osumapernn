x = []
target = []
os.chdir("/home/crazebull7/maps/")
for flo in os.listdir():
    os.chdir("/home/crazebull7/maps/" + flo)
    for file_path in os.listdir():
        if file_path.endswith(".osu"):
            #name = "D:\\osunn\\1002819 Roselia - MIIRO [no video]\\Roselia - MIIRO (-Mikan) [Shana\'s MX].osu"
            print("trying to pars that: ",file_path)
            result = read_osu(file_path)
            print('read_osu: ',result[0])
            if(result[0] == 0):
                result[1].timingpoints[0].time = (result[1].timingpoints[0].time + result[1].timingpoints[0].beatLength * 100) % result[1].timingpoints[0].beatLength
                binosumap = convert_osu(result[1])
                print("binosumap: mean max min sum", binosumap.mean(), binosumap.max(), binosumap.min(), binosumap.sum() )
                target.append(binosumap)
                print("opening and converting -",result[1].AudioFilename)
                x.append(convert_music(result[1], binosumap.shape[0]))
                
                
        
                
