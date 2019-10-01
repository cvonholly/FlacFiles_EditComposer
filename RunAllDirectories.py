"""This File will import the editComposerFunction and apply the chosen Function to all files in the chosen Directory.

For Example: Johann Sebastain Bach --> Bach, Johann Sebastain

Steps:

1. You will have to install the mutagen module: https://mutagen.readthedocs.io/en/latest/user/index.html#

2. Edit the directory the code should be apllied to (in "C:yourDirectory/).

3. In the 'editComposerFunction.py', enter the function you want to run.

5. Run this file.  
"""

import os
from editComposerFunction import editTag


for root, dirs, files in os.walk(r"Z:\24Bit\1. Classical"):      
    for filename in files:
        if filename.endswith(".flac"):
            try:
                editTag(os.path.join(root, filename)) 
            except KeyError:
                print ("Tag Value is empty.")
