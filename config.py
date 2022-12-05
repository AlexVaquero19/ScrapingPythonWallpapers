import os
from pathlib import Path

dir = os.getcwd() #Get directory
homePath = str(Path.home())
PATH_WEB_DRIVER_EXE = r""+dir+"\Files\chromedriver.exe" #Chrome Web Driver
url = 'https://dream.ai/create/' #URL page AI wallpapers

#XPATHs
input = '/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/input'
buttonSubmit = '/html/body/div/div/div[3]/div/div/div[1]/div[2]/button'
buttonBuy = '/html/body/div/div/div[3]/div/div/div[1]/div[2]/div[1]/div[5]/div[2]/div[2]/button'
images = '/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]'
backButton = '/html/body/div/div/div[3]/div/div/div[1]/div[1]/div/button'
imgDownloadPath = '/html/body/main/section/section/div/div[1]/slider-component/ul/li[2]/modal-opener/div/img'

#Directory in Spanish and English
directoryDownloadsES = str(Path.home()) + "\\OneDrive\\Fotos\\FondosIA\\"
directoryDownloadsEN = str(Path.home()) + "\\OneDrive\\Fotos\\FondosIA\\"

#Array Words to create random wallpapers
arrayWords = ['Urban Painting', 'Cloudy Day',
    'Yellow Frog','Reflection Lake','Planets Artwork','Colored Spirals','Neon Spiral','Clouds Mountains','Lightning','Mosaic','Colourful Explosion',
    'Play Station Abstract','Glitch Abstract','Clouds Shaped','Volcano','Waves Distorsion','Colored Drops','Sun Desert','Swirl', 'Lines Moving'
]