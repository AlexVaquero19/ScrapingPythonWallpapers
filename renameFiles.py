import os
import shutil
from pathlib import Path

#This file we only use if you delete some image and you don't want images with no correlative numbers

fileName = ""
homePath = str(Path.home())
dirs = [homePath + "\\OneDrive\\Fotos\\FondosIA\\"]

for dir in dirs:
    for file in os.listdir(dir):
        fileNameSplit = file.split("_")
        if isinstance(fileNameSplit, int):
            fileName = fileNameSplit[(len(fileNameSplit[0]) + 1)]