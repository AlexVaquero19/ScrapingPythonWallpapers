import os
import random
import time
import config as cfg
from selenium import webdriver

def obtenerImagenes():
    counter = int(input("Input a Counter: "))

    driver = webdriver.Chrome(cfg.PATH_WEB_DRIVER_EXE)
    driver.get(cfg.url)
    driver.maximize_window()

    time.sleep(2)

    while True:
        divImages = driver.find_element_by_class_name("XIGWN")
        numImages = len(divImages.find_elements_by_tag_name("img"))
        typesToSelectImages = divImages.find_elements_by_tag_name("img")

        typeSelected = random.randrange(0, numImages-1)
        wordSelected = random.choice(cfg.arrayWords)
        
        driver.find_element_by_xpath(cfg.input).send_keys(wordSelected)
        time.sleep(1)
        typesToSelectImages[typeSelected].click()
        time.sleep(1)
        driver.find_element_by_xpath(cfg.buttonSubmit).click()
        time.sleep(20)

        driver.find_element_by_xpath(cfg.buttonBuy).click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        imgUrl = driver.find_element_by_xpath('/html/body/main/section/section/div/div[1]/slider-component/ul/li[2]/modal-opener/div/img').get_attribute("src")
        driver.get(imgUrl)

        time.sleep(3)
        
        filename = str(counter) + "_" + wordSelected.lower() + ".jpg"
        try:
            os.rename(cfg.directoryDownloadsES+"final.jpg", cfg.directoryDownloadsES+filename)
        except:
            os.rename(cfg.directoryDownloadsEN+"final.jpg", cfg.directoryDownloadsEN+filename)

        counter += 1

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath(cfg.backButton).click()
        time.sleep(1)
        driver.find_element_by_xpath(cfg.input).clear()

obtenerImagenes()