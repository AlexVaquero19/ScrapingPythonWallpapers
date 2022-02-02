import os
import getpass
from pathlib import Path

dir = os.getcwd() #Obtenemos el Directorio
dir_ficheros = dir + '\Ficheros' #Obtenemos el Directorio donde están lños Ficheros SQL y JSON
PATH_WEB_DRIVER_EXE = r""+dir+"\Ficheros\chromedriver.exe" #Chrome Web Driver
url = 'https://app.wombo.art/' #URL de la página de fondos AI

#XPATH Completos
input = '/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/input'
buttonSubmit = '/html/body/div/div/div[3]/div/div/div[1]/div[2]/div/button'
buttonBuy = '/html/body/div/div/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/button'
backButton = '/html/body/div/div/div[3]/div/div/div[1]/div[1]/button'
imgDownloadPath = '/html/body/main/section/section/div/div[1]/slider-component/ul/li[2]/modal-opener/div/img'

#Directorio por si está en Español o Inglés
directoryDownloads = str(Path.home()) + "\\Descargas\\"
directoryDownloadsEN = str(Path.home()) + "\\Downloads\\"

#Array de Palabras para los fondos aleatorios y Tipos
arrayWords = [
             'Crow Wings Bird Swing', 'Paint Drops', 'Squares Shape Light', 'Air Ballon Sky Clouds', 'Triangle Shape Dark', 
             'Abstraction Geometry Shapes', 'Landscape Blue Tree', 'Triangle Light Blurred', 'Abstraction Light Neon',
             'Background Light Spot', 'Clouds Sky Abstract', 'Paint Water Liquid', 'Shards Stone Basckground', 'Wolf Face Drawing',
             'Flower Background Dark', 'Glow Neon Light', 'Circles Rotation Red', 'Nebula Sparkles Light', 'Forest Abstraction Shadows'
]
arrayTypes = [3,4,5,6,8,9,11,12,14,16]