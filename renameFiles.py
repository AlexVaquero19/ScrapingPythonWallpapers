import os
from pathlib import Path

fileName = ""
homePath = str(Path.home())
dirs = [homePath + "\\Downloads\\Wallpapers\\", homePath + "\\OneDrive\\Fotos\\FondosIA\\"]

for dir in dirs:
    counter = 1
    for file in os.listdir(dir):
        fileNameSplit = file.split("_", 1)
        fileName = str(counter) + "_" + fileNameSplit[1]
        counter += 1
        os.rename(dir+file, dir+fileName)