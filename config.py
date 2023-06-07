import os
from pathlib import Path

dir = os.getcwd() #Get directory
downloadsDirectory = os.path.expanduser('~\\Downloads')
homePath = str(Path.home())
path_to_extension =  r""+dir+"\\Files\\adblock.crx"
PATH_WEB_DRIVER_EXE = r""+dir+"\Files\chromedriver.exe" #Chrome Web Driver
url = 'https://dream.ai/create/' #URL page AI wallpapers

#XPATHs
input = "/html/body/div/div/div[4]/div/div[2]/div[1]/div[1]/div/div[3]/div[1]/div[1]/input"
styles = "/html/body/div/div/div[4]/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/div/div[2]"
createArtBtn = "/html/body/div/div/div[4]/div/div[2]/div[1]/div[2]/button"
downloadBtn = "/html/body/div/div/div[4]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div/div[3]"

adPremiumClose = "/html/body/div[1]/div/div[3]/div/div/div[1]/button"
adClose = "/html/body/div[1]/div/div[1]/div/div/div[1]/button"

#Directory in Spanish and English
directoryDownloads = os.path.expanduser('~\\OneDrive\\Fotos\\FondosIANew\\') #str(Path.home()) + "\\OneDrive\\Fotos\\FondosIANew\\"

#Array Words to create random wallpapers
arrayWords = ['Urban Painting', 'Cloudy Day',
    'Yellow Frog','Reflection Lake','Planets Artwork','Colored Spirals','Neon Spiral','Clouds Mountains','Lightning','Mosaic','Colourful Explosion',
    'Play Station Abstract','Glitch Abstract','Clouds Shaped','Volcano','Waves Distorsion','Colored Drops','Sun Desert','Swirl', 'Lines Moving'
]