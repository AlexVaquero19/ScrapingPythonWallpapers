import os
from pathlib import Path

fileName = ""
homePath = str(Path.home())
#dirs = [homePath + "\\Downloads\\Wallpapers\\", homePath + "\\OneDrive\\Fotos\\FondosIA\\"]
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