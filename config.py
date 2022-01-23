import os
import getpass

dir = os.getcwd() #Obtenemos el Directorio
dir_ficheros = dir + '\Ficheros' #Obtenemos el Directorio donde están lños Ficheros SQL y JSON
PATH_WEB_DRIVER_EXE = r""+dir+"\Ficheros\chromedriver.exe" #Chrome Web Driver
url = 'https://app.wombo.art/'

input = '/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/input'
buttonSubmit = '/html/body/div/div/div[3]/div/div/div[1]/div[2]/div/button'
buttonBuy = '/html/body/div/div/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/button'
backButton = '/html/body/div/div/div[3]/div/div/div[1]/div[1]/button'

directoryDownloadsES = 'C:\\Usuarios\\'+getpass.getuser()+"\\Descargas\\"
directoryDownloadsEN = 'C:\\Users\\'+getpass.getuser()+"\\Downloads\\"

arrayWords = ['HeadPhones', 'Trees', 'Birds', 'Fire', 'Roses', 'Forest', 'Volcano', 'Paint', 'Paint Drops']