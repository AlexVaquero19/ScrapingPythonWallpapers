import os
from pathlib import Path

dir = os.getcwd() #Get directory
homePath = str(Path.home())
dir_ficheros = homePath + "\\OneDrive\\Fotos\\FondosIA\\"
PATH_WEB_DRIVER_EXE = r""+dir+"\Ficheros\chromedriver.exe" #Chrome Web Driver
url = 'https://app.wombo.art/' #URL page AI wallpapers

#XPATHs
input = '/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/input'
buttonSubmit = '/html/body/div/div/div[3]/div/div/div[1]/div[2]/div/button'
buttonBuy = '/html/body/div/div/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/button'
backButton = '/html/body/div/div/div[3]/div/div/div[1]/div[1]/button'
imgDownloadPath = '/html/body/main/section/section/div/div[1]/slider-component/ul/li[2]/modal-opener/div/img'

#Directory in Spanish and English
directoryDownloadsES = str(Path.home()) + "\\OneDrive\\Fotos\\FondosIA\\"
directoryDownloadsEN = str(Path.home()) + "\\OneDrive\\Fotos\\FondosIA\\"

#Array Words to create random wallpapers
arrayWords = [
             'Abstract Clouds', '3D Paints', 'Paint Drops', 'Abstract Patterns', 'Abstract Cubes', 'Magic Sunset', 'Water Droplets', 'Sky', 'Marble Wallpaper', 'HDR Space Cloud',
             'Dark Moonlight', 'Wolfs', 'Neon Glow', 'Puzzle', 'Skullpaper', 'Ink Colour', 'Trippy Sky'
]
arrayTypes = [3,4,5,6,8,9,11,12,14,16]