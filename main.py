#Importamos todo lo necesario
import time
import random
import datetime
import urllib.request
import config as cfg
from selenium import webdriver  
from selenium.webdriver.common.by import By

def obtenerImagenes():
    #Ponemos el Contador según el valor que nosotros queramos que empieze
    counter = int(input("Input a Counter: "))

    #Creamos la Instancia del Navegador
    driver = webdriver.Chrome(cfg.PATH_WEB_DRIVER_EXE)
    driver.get(cfg.url)
    driver.maximize_window()

    time.sleep(2)

    #Ponemos un while True: para que sea un bucle infinito y descargue imágenes hasta que nosotros queramos pararlo
    while True:
        #Desde el Array de Tipo cogemos uno al Azar, lo hacemos de esta forma porque a lo mejor hay tipos que no quieres que toquen nunca
        divImages = driver.find_element(By.CLASS_NAME, ("XIGWN"))
        typesToSelectImages = divImages.find_elements(By.TAG_NAME, "img")

        #Seleccionamos el Tipo con el Click de manera aleatoria
        typeSelected = int(random.choice(cfg.arrayTypes))
        #Obtenemos una palabra también aleatoria pero del array que tenemos en el fichero de Configuración
        wordSelected = str(random.choice(cfg.arrayWords)).replace("b'", "").replace("'","")

        time.sleep(1)
        
        #Ponemos en el Input donde va a ir la Palabara, la que hemos escogido de manera aleatoria
        driver.find_element(By.XPATH, cfg.input).send_keys(wordSelected)
        time.sleep(1)
        #Seleccionamos el Tipo
        typesToSelectImages[typeSelected].click()
        time.sleep(1)
        #Pulsamos en el botón de generar la imagen
        driver.find_element(By.XPATH, cfg.buttonSubmit).click()
        time.sleep(25)

        #Pulsamos en "Comprar la Imágen"
        driver.find_element(By.XPATH, cfg.buttonBuy).click()
        time.sleep(5)
        #Nos movemos con el Driver a la pestaña que se ha abierto
        driver.switch_to.window(driver.window_handles[1])

        #Cogemos la Fecha y Hora y se la añadimos al nombre de la Imagen
        now = datetime.datetime.now()
        formatFileName = "_" + now.strftime("%d %m %Y %H %M %S").replace(" ", "") + ".jpg"

        filename = str(counter) + "_" + wordSelected.lower().replace(" ", "_") + formatFileName
        imgUrl = driver.find_element(By.XPATH, cfg.imgDownloadPath).get_attribute("src")

        #Guardamos la Imagen en el Directorio de Descargas
        urllib.request.urlretrieve(imgUrl, cfg.directoryDownloadsEN + filename)

        #Sumamos el Contador
        counter += 1

        time.sleep(0.5)

        #Cerramos la ventana
        driver.close()
        #Volvemos a la ventana anterior
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element(By.XPATH, cfg.backButton).click()
        time.sleep(1)
        #Borramos lo que hubiese en el Input para escribir de nuevo
        driver.find_element(By.XPATH, cfg.input).clear()

obtenerImagenes()
