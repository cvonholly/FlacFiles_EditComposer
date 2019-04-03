"""This file will edit the Composer value of a single file, which is needed to aply it to all files.

Important Information:

1. Read the description in 'RunAllDirectories.py'

2. This File is made for '.flac' files. It is currently not optimised for other file formats.

3.  The final line of the script (line 86) will run the function you want to apply to all the files.
    By default it is set to 'reverseComposerFinal()' which will reverse all Composers name.
    (e.g.: Johann Sebastain Bach --> Bach, Johann Sebastain)
    Other functions will do different actions, here a quick overview:
    
    1. 'cleanComposer()' will extract any unwanted symbols out of your composers name.
        (e.g.: ['Strauss,  Johann'] --> Strauss Johann)
        If you want to look or edit the list of unwanted symbols, go to 'basicFunction.py' and look at 'cleanComposer'

    2. 'changeComposer()' will give a file a new composer. You will have to enter that name into the 'newComposer' variable before the function
        (e.g.: The Beatles --> John Lennon)

    3. 'changeLabel()' will move the composer value to a new tag (here: 'Creator') and empty the composer value. This is usefull if you want to keep the Compsers Name somewhere but not in the composer Value.
        (e.g.: audio["composer"] = "Roling Stones" --> audio["composer"] = "", audio["Creator"] = "Roling Stones")

4. If you want to apply this to a directory, run 'RunAllDirectories.py'
"""

from mutagen import *
from mutagen.flac import FLAC
import sys
from basicFunctions import cleanup, reverseWords

newComposer = "ComposerName" # Enter the wanted Composers name here (e.g.: "Anton Bruckner")

def editComposer(x):
    audio = FLAC(x)
    composer = str(audio["composer"])
    def cleanComposer():
        cleanCom = cleanup(composer)
        audio["composer"] = cleanCom
        audio.pprint()
        audio.save()
        print("Composername has been 'cleaned'.")

    def printComposer():
        print (composer)

    def reverseComposer(x):
        z = cleanup(str(audio["composer"]))
        audio["composer"] = reverseWords(z)
        audio.pprint()
        audio.save()
        print ("Your composers Name has been successfully reversed to ", reverseWords(z))

    def reverseComposerFinal():
        if cleanup(composer) == "":
            print ("Composer's Name {} is already reversed or not existing.".format(cleanup(composer)))
        else:
            reverseComposer(audio)

    def deleteComposer():
        if cleanup(composer) == "":
            print ("Composer's Name {} is already reversed or not existing.".format(cleanup(composer)))
        else:
            audio["Creator"] = cleanup(composer)
            audio["composer"] = ""
            audio.pprint()
            audio.save()
            print("Composername{} has been deleted.".format(cleanup(composer)))
    
    def changeComposer():
        audio["composer"] = newComposer
        print("The Composers name has been changed to {}".format(str(audio["composer"])))
        audio.pprint()
        audio.save()

    def changeLabel():
        if cleanup(composer) == "":
            print ("Composer name empty. ")
        else:
            audio["Creator"] = cleanup(str(audio["composer"]))
            audio["composer"] = ""
            print ("Composer's name {} has been transfered to 'soloists'.".format(str(audio["soloists"])))
            audio.pprint()
            audio.save()

    reverseComposerFinal()
