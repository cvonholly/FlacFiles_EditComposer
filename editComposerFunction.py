"""This file will edit the Tag value of a single file, which is needed to aply it to all files.

Important Information:

1. Read the description in 'RunAllDirectories.py'

2. This File is made for '.flac' files. It is currently not optimised for other file formats.

3.  The final line of the script will run the function you want to apply to all the files.
    By default it is set to 'reverseTagFinal()' which will reverse all Tags name.
    (e.g.: Johann Sebastain Bach --> Bach, Johann Sebastain)
    Other functions will do different actions, here a quick overview:
    
    1. 'cleanTag()' will extract any unwanted symbols out of your Tags name.
        (e.g.: ['Strauss,  Johann'] --> Strauss Johann)
        If you want to look or edit the list of unwanted symbols, go to 'basicFunction.py' and look at 'cleanTag'

    2. 'changeTag()' will give a file a new Tag. You will have to enter that name into the 'newTag' variable before the function
        (e.g.: The Beatles --> John Lennon)

    3. 'changeLabel()' will move the Tag value to a new tag (here: 'Creator') and empty the Tag value. This is usefull if you want to keep the Compsers Name somewhere but not in the Tag Value.
        (e.g.: audio[Tag] = "Roling Stones" --> audio[Tag] = "", audio["Creator"] = "Roling Stones")

4. If you want to apply this to a directory, run 'RunAllDirectories.py'
"""

from mutagen import *
from mutagen.flac import FLAC
import sys
from basicFunctions import *



newTag = "The Beatles" # Enter the wanted Tags name here (e.g.: "Anton Bruckner")

certainTag = 'Johann, Sebastian Bach'

def editTag(x):
    audio = FLAC(x)
    tag = "artist"
    Tag = str(audio[tag])
    def cleanTag():
        cleanCom = cleanup(Tag)
        audio[Tag] = cleanCom
        audio.pprint()
        audio.save()
        print("Tagname has been 'cleaned'.")
    
    def comma():
        inpWords = Tag.split(" ")
        outWords = ", ".join((inpWords[0],inpWords[1]))
        print("Artist has been changed to {}".format(cleanupNoComma(Tag)))
        return cleanupNoComma(outWords)

    def printTag():
        print (Tag)

    def reverseTag(x):
        z = cleanup(str(audio[tag]))
        audio[tag] = reverseWords(z)
        audio.pprint()
        audio.save()
        print ("Your Tags Name has been successfully reversed to ", reverseWords(z))

    def reverseTagFinal():
        if cleanup(Tag) == "":
            print ("Tag's Name {} is already reversed or not existing.".format(cleanup(Tag)))
        else:
            reverseTag(audio)
    
    def reverseSpecificTag():
        if cleanup(Tag) == "":
            print ("Tag's Name {} is already reversed or not existing.".format(cleanup(Tag)))
        else:
            if cleanupNoComma(Tag) == certainTag:
                reverseTag(audio)
            else:
                print("Tag does not match name.")

    def deleteTag():
        if cleanup(Tag) == "":
            print ("Tag's Name {} is already reversed or not existing.".format(cleanup(Tag)))
        else:
            audio["Creator"] = cleanup(Tag)
            audio[tag] = ""
            audio["Album Artist"] = ""
            audio.pprint()
            audio.save()
            print("{} {} has been deleted.".format(tag, cleanup(Tag)))
    
    def changeTag():
        audio[tag] = cleanup(newTag)
        print("The Tags name has been changed to {}".format(cleanup(Tag)))
        audio.pprint()
        audio.save()

    def changeLabel():
        if cleanup(Tag) == "":
            print ("Tag name empty. ")
        else:
            audio["Creator"] = cleanup(str(audio[Tag]))
            audio[tag] = ""
            print ("Tag's name {} has been transfered to 'soloists'.".format(str(audio["soloists"])))
            audio.pprint()
            audio.save()

    deleteTag()
