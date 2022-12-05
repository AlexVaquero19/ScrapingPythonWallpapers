#Imports
import os
import time
import random
import datetime
import urllib.request
import config as cfg
from selenium import webdriver  
from selenium.webdriver.common.by import By

def obtenerImagenes():
    #Create Chrome instance
    driver = webdriver.Chrome(cfg.PATH_WEB_DRIVER_EXE)
    driver.get(cfg.url)
    driver.maximize_window()

    time.sleep(1)

    #Make an infinite loop to create the wallpaper
    while True:
        #We choose a random word from the array types
        divImages = driver.find_element(By.XPATH, cfg.images)
        typesToSelectImages = divImages.find_elements(By.TAG_NAME, "img")

        #We click the type for the wallpaper
        typeSelected = random.randint(0, 42)
        #We choose a random word from the array words
        wordSelected = str(random.choice(cfg.arrayWords))

        time.sleep(1)
        
        #We put the random word on the input
        driver.find_element(By.XPATH, cfg.input).send_keys(wordSelected)
        time.sleep(1)
        #Select type
        typesToSelectImages[typeSelected].click()
        time.sleep(1)
        #Press the create button
        driver.find_element(By.XPATH, cfg.buttonSubmit).click()

        clickable = False

        while clickable == False:
            try:
                #Click on "Buy Print"
                driver.find_element(By.XPATH, cfg.buttonBuy).click()
                driver.switch_to.window(driver.window_handles[1])
                clickable = True
            except:
                pass

        time.sleep(2.5)
        #We move to the second window
        driver.switch_to.window(driver.window_handles[1])

        #We take the date and hour to put to the wallpaper name
        now = datetime.datetime.now()
        formatFileName = "_" + now.strftime("%d %m %Y %H %M %S").replace(" ", "") + ".jpg"

        filename = wordSelected.lower().replace(" ", "_") + formatFileName
        imgUrl = driver.find_element(By.XPATH, cfg.imgDownloadPath).get_attribute("src")

        #We save the wallpaper on the directory path you selected on config.py
        directoryToCreate = cfg.directoryDownloadsEN + wordSelected.replace(" ", "_")
        if(checkDirectory(directoryToCreate)):
            urllib.request.urlretrieve(imgUrl, directoryToCreate.lower() + "\\" + filename)
        else:
            os.mkdir(directoryToCreate)
            urllib.request.urlretrieve(imgUrl, directoryToCreate.lower() + "\\" + filename)

        time.sleep(1.5)

        #Close the window
        driver.close()

        #Come back to the main window
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element(By.XPATH, cfg.backButton).click()
        time.sleep(0.5)
        #Clear the input text to put the new word and start again
        driver.find_element(By.XPATH, cfg.input).clear()
    
def checkDirectory(directoryToCreate):
    return os.path.isdir(directoryToCreate)
    

obtenerImagenes()
