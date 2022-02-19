import urllib3
import config as cfg
import os

#os.mkdir(cfg.directoryDownloadsEN + "\\Prueba")
filename = "18_marble_wallpaper_09022022122016"
directoryToCreate = cfg.directoryDownloadsEN + filename.capitalize()
if(checkDirectory(directoryToCreate)):    
    urllib3.request.urlretrieve(imgUrl, directoryToCreate.lower())
else:
    os.mkdir(directoryToCreate)
    urllib.request.urlretrieve(imgUrl, directoryToCreate.lower())

def checkDirectory(directoryToCreate):
    return os.path.isdir(directoryToCreate)