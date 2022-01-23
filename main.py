#Importamos todo lo necesario
import os
import random
import time
import requests
import config as cfg
from selenium import webdriver  

def obtenerImagenes():
    #Ponemos el Contador según el valor que nosotros queramos que empieze
    counter = int(input("Input a Counter: "))

    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    dictionary = response.content.splitlines()

    WORDS = []
    for sub in dictionary:
        sub = str(sub)
        WORDS.append(sub.replace("'b", "").replace("'", ""))

    #Creamos la Instancia del Navegador
    driver = webdriver.Chrome(cfg.PATH_WEB_DRIVER_EXE)
    driver.get(cfg.url)
    driver.maximize_window()

    time.sleep(2)

    #Ponemos un while True: para que sea un bucle infinito y descargue imágenes hasta que nosotros queramos pararlo
    while True:
        #Obtenemos los Tipos de Imagenes que queremos a través de una Clase CSS que solo tiene ese DIV, obtenemos
        #el número de imagenes que podemos seleccionar -1 y ese es el tipo de la imágen que vamos a crear
        divImages = driver.find_element_by_class_name("XIGWN")
        numImages = len(divImages.find_elements_by_tag_name("img"))
        typesToSelectImages = divImages.find_elements_by_tag_name("img")

        #Seleccionamos el Tipo con el Click de manera aleatoria
        typeSelected = random.randrange(0, numImages-1)
        #Obtenemos una palabra también aleatoria pero del array que tenemos en el fichero de Configuración
        wordSelected = str(random.choice(WORDS)).replace("b'", "").replace("'","")

        WORDS.pop(WORDS.index(wordSelected))

        time.sleep(1)
        
        #Ponemos en el Input donde va a ir la Palabara, la que hemos escogido de manera aleatoria
        driver.find_element_by_xpath(cfg.input).send_keys(wordSelected)
        time.sleep(1)
        #Seleccionamos el Tipo
        typesToSelectImages[typeSelected].click()
        time.sleep(1)
        #Pulsamos en el botón de generar la imagen
        driver.find_element_by_xpath(cfg.buttonSubmit).click()
        time.sleep(20)

        #Pulsamos en "Comprar la Imágen"
        driver.find_element_by_xpath(cfg.buttonBuy).click()
        time.sleep(5)
        #Nos movemos con el Driver a la pestaña que se ha abierto
        driver.switch_to.window(driver.window_handles[1])
        #Se generará un Div con la Imágen y cogemos el SRC y descargamos esa imágen
        imgUrl = driver.find_element_by_xpath('/html/body/main/section/section/div/div[1]/slider-component/ul/li[2]/modal-opener/div/img').get_attribute("src")
        driver.get(imgUrl)

        time.sleep(3)
        
        #Después cogemos esa imágenn que siempre se llama igual y la reemplazamos el nombre por el Contador mas la palabra seleccionada mas la extensión
        filename = str(counter) + "_" + wordSelected.lower() + ".jpg"
        try:
            os.rename(cfg.directoryDownloadsES+"final.jpg", cfg.directoryDownloadsES+filename)
        except:
            os.rename(cfg.directoryDownloadsEN+"final.jpg", cfg.directoryDownloadsEN+filename)
        
        #Sumamos el Contador
        counter += 1

        #Cerramos la ventana
        driver.close()
        #Volvemos a la ventana anterior
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath(cfg.backButton).click()
        time.sleep(1)
        #Borramos lo que hubiese en el Input para escribir de nuevo
        driver.find_element_by_xpath(cfg.input).clear()

obtenerImagenes()
