
SOURCE = "/home/olivier/Documents/gedcom/20240402landry.ged"




def analyze(sourcefile):
    # leveltags = [ { "TAG1" : nboftags1, "TAG2" = nboftags2, ...}, {...}, ...]
    # levels 0, 1, 2, 3, 4, 5
    leveltags = [{},{},{},{},{},{},{}]
    with open(sourcefile, "r") as f:
        slines = f.readlines()
        strange = []
        for roughline in slines:
            line = roughline.strip()
            tokens = line.split(" ")
            if tokens[0] == "0":
                if len(tokens) < 3:
                    strange.append(line)
                    continue
                else:
                    if not tokens[2] in leveltags[0]:
                        leveltags[0][tokens[2]] = 1
                        continue
                    else:
                        leveltags[0][tokens[2]] += 1
                        continue
            for i in range(1,6):
                if tokens[0] == str(i):
                    if not tokens[1] in leveltags[i]:
                        leveltags[i][tokens[1]] = 1
                        continue
                    else:
                        leveltags[i][tokens[1]] += 1
                        continue
            #this is the place for strange lines
            if tokens[0] not in ['0','1','2','3','4','5']:
                strange.append(line)

    print("Strange lines:") 
    print(strange)
    for i in range(6):
        print("Tags level " + str(i))
        print(leveltags[i])
        print("==> Nb of " + str(i) +"-level tags: " + str(len(leveltags[i])))
    return leveltags
                        
                    
                
            
            



def main():
    analyze(SOURCE)


if __name__ == '__main__':
    main()


