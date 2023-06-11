#Imports
import os
import time
import random
import shutil
import datetime
import config as cfg
from selenium import webdriver  
from selenium.webdriver.common.by import By

def obtenerImagenes():
  chop = webdriver.ChromeOptions()
  chop.add_extension(cfg.path_to_extension)

  driver = webdriver.Chrome(cfg.PATH_WEB_DRIVER_EXE, chrome_options=chop)
  driver.get(cfg.url)
  driver.maximize_window()

  time.sleep(1)

  stylesDiv = driver.find_element(By.XPATH, cfg.styles)
  stylesImages = stylesDiv.find_elements(By.TAG_NAME, "img")

  #Make an infinite loop to create the wallpaper
  while True:
    #We choose a random word from the array words
    wordSelected = str(random.choice(cfg.arrayWords))

    time.sleep(1)

    #We put the random word on the input
    driver.find_element(By.XPATH, cfg.input).send_keys(wordSelected)
    wordSelected = wordSelected.lower().replace(" ", "_")

    time.sleep(1)

    checkAds(driver, False)

    isPremium = True
    while isPremium == True:
      #We click the type for the wallpaper
      typeSelected = random.randint(0, 88)

      #Select Type
      stylesImages[typeSelected].click()
      time.sleep(1.5)

      try:
        driver.find_element(By.XPATH, cfg.adPremiumClose).click()
        isPremium = True
      except:
        checkAds(driver, True)
        isPremium = False
        driver.find_element(By.XPATH, cfg.createArtBtn).click()

    downloadable = False
    while downloadable == False:
      try:
          driver.find_element(By.XPATH, cfg.downloadBtn).click()
          downloadable = True
      except:
          checkAds(driver, True)
          pass
      
    time.sleep(3)
    
    #We take the date and hour to put to the wallpaper name
    now = datetime.datetime.now()
    formatFileName = now.strftime("_%d%m%Y%H%M%S.jpg")

    #We save the wallpaper on the directory path you selected on config.py
    filename = wordSelected + formatFileName

    fileToRename = os.path.join(cfg.downloadsDirectory,"dream_TradingCard.jpg")
    fileRenamed = os.path.join(cfg.downloadsDirectory, filename)

    time.sleep(1)

    os.rename(fileToRename, fileRenamed)
    moveDownload(fileRenamed, wordSelected, filename)    
    
    #Clear the input text to put the new word and start again
    driver.find_element(By.XPATH, cfg.input).clear() 

def moveDownload(fileRenamed, wordSelected, filename):
  directoryToCreate = os.path.join(cfg.directoryDownloadsEN, wordSelected)
  if(checkDirectory(directoryToCreate)):
    shutil.move(fileRenamed, os.path.join(directoryToCreate.lower(), filename))
  else:
    os.mkdir(directoryToCreate)
    shutil.move(fileRenamed, os.path.join(directoryToCreate.lower(), filename))

def checkDirectory(directoryToCreate):
  return os.path.isdir(directoryToCreate)

def checkAds(driver: webdriver.Chrome, waitAttempts: bool):
  attempts = 0
  noAds = False
  if waitAttempts:
    while noAds == False and attempts < 15:
      try:
        driver.find_element(By.XPATH, cfg.adClose).click()
        noAds = True
      except:
        pass
      attempts += 1
  else:
    while noAds == False and attempts < 200:
      try:
        driver.find_element(By.XPATH, cfg.adClose).click()
        noAds = True
      except:
        pass
      attempts += 1

obtenerImagenes()