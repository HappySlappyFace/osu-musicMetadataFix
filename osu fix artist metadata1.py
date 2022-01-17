import os
import eyed3

# assign directory
directory = 'C:/Users/Happy/AppData/Local/osu!/Songs/'

# iterate over files in
# that directory
errorcount = 0


def artistchanger(xee, ress):
    audiofilee = eyed3.load(xee)
    if ress == "":
        pass
    else:
        try:
            print(ress)
            audiofilee.tag.artist = ress
            audiofilee.tag.save()
        except:
            pass


for root, dirs, files in os.walk(directory):
    for filename in files:
        # print(os.path.join(root, filename))
        if filename.endswith('.mp3'):
            xe = root + "/" + filename
            audiofile = eyed3.load(xe)
            try:
                if audiofile.info.time_secs > 20:
                    try:
                        if audiofile.tag.artist == "":
                            print(xe)
                            a = xe.index("Songs")
                            b = xe[a + 6:]
                            try:
                                c = b.index(" ")
                                d = b.index(" -")
                                res = b[c + 1:d]
                                artistchanger(xe, res)
                            except ValueError:
                                try:
                                    c = b.index(" ")
                                    res = b[c + 1:]
                                    artistchanger(xe, res)
                                except:
                                    print("file uncapable of being changed")
                                    res = ""
                                    artistchanger(xe, res)
                            else:
                                pass
                    except AttributeError:
                        errorcount += 1

                else:
                    pass
            except AttributeError:
                pass
        else:
            pass
print(errorcount)

