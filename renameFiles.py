import os
from pathlib import Path

#This file we only use if you delete some image and you don't want images with no correlative numbers

fileName = ""
homePath = str(Path.home())
dirs = [homePath + "\\OneDrive\\Fotos\\FondosIA\\"]

for dir in dirs:
    counter = 1
    counter_duplicate = 1
    for file in os.listdir(dir):
        fileNameSplit = file.split("_", 1)
        fileName = str(counter) + "_" + fileNameSplit[1]
        counter += 1
        try:
            os.rename(dir+file, dir+fileName)
        except:
            pass