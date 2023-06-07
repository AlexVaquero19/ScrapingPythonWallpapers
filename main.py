#Imports
import os
import time
import random
import shutil
import datetime
import config as cfg
from selenium import webdriver  
from selenium.webdriver.common.by import By

def checkDirectory(directoryToCreate):
  return os.path.isdir(directoryToCreate)

def obtenerImagenes(chop):
  driver = webdriver.Chrome(cfg.PATH_WEB_DRIVER_EXE, chrome_options=chop)
  driver.get(cfg.url)
  driver.maximize_window()

  time.sleep(1)

  stylesDiv = driver.find_element(By.XPATH, cfg.styles)
  stylesImages = stylesDiv.find_elements(By.TAG_NAME, "img")

  checkedAd = False

  #Make an infinite loop to create the wallpaper
  while True:
    #We choose a random word from the array words
    wordSelected = str(random.choice(cfg.arrayWords))

    time.sleep(1)

    #We put the random word on the input
    driver.find_element(By.XPATH, cfg.input).send_keys(wordSelected)
    time.sleep(1)

    isPremium = True
    while isPremium == True:
      #We click the type for the wallpaper
      typeSelected = random.randint(0, 88)

      #Select Type
      stylesImages[typeSelected].click()

      try:
        driver.find_element(By.XPATH, cfg.adPremiumClose).click()
        isPremium = True
      except:
        isPremium = False

    if not checkedAd:
      noAds = False
      while noAds == False:
        try:
          driver.find_element(By.XPATH, cfg.adTwoClose).click()
          noAds = True
        except:
          pass

    #Press the create button
    try:
      driver.find_element(By.XPATH, cfg.createArtBtn).click()
      noAds = True
    except:
      time.sleep(1.5)
      driver.find_element(By.XPATH, cfg.adPremiumClose).click()

    clickable = False

    while clickable == False:
      try:
          #Click on "Buy Print"
          driver.find_element(By.XPATH, cfg.downloadBtn).click()
          clickable = True
      except:
          pass
      
    time.sleep(3)
    
    #We take the date and hour to put to the wallpaper name
    now = datetime.datetime.now()
    formatFileName = "_" + now.strftime("%d %m %Y %H %M %S").replace(" ", "") + ".jpg"
    #We save the wallpaper on the directory path you selected on config.py
    filename = wordSelected.lower().replace(" ", "_") + formatFileName

    fileToRename = cfg.downloadsDirectory + "\\" + "dream_TradingCard.jpg"
    fileRenamed = cfg.downloadsDirectory + "\\" + wordSelected.lower().replace(" ", "_") + formatFileName
    os.rename(fileToRename, fileRenamed)

    directoryToCreate = cfg.directoryDownloads + wordSelected.replace(" ", "_")
    if(checkDirectory(directoryToCreate)):
      shutil.move(fileRenamed, os.path.join(directoryToCreate.lower(), filename))
    else:
      os.mkdir(directoryToCreate)
      shutil.move(fileRenamed, os.path.join(directoryToCreate.lower(), filename))
    
    #Clear the input text to put the new word and start again
    driver.find_element(By.XPATH, cfg.input).clear()
    checkedAd = True

chop = webdriver.ChromeOptions()
chop.add_extension(cfg.path_to_extension)

obtenerImagenes(chop)