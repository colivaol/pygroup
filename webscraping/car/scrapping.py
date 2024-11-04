from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


def main():
    # Configura la ruta del ChromeDriver
    service = Service('ruta/a/chromedriver')  # Asegúrate de reemplazar 'ruta/a/chromedriver' con la ruta correcta

    # Inicia el navegador usando el servicio
    driver = webdriver.Chrome(service=service)

    # Abre la URL
    driver.get("https://www.coches.net/opel-astra-1.4-turbo-excellence-4p-gasolina-2014-en-madrid-58673276-covo.aspx")

    # Espera unos segundos para que se ejecute el JavaScript
    sleep(5)

    # Obtiene el HTML de la página cargada
    contenido_html = driver.page_source

    # Opcional: Guarda el HTML en un archivo
    with open("pagina.html", "w", encoding="utf-8") as file:
        file.write(contenido_html)

    # Cierra el navegador
    driver.quit()

if __name__ == '__main__':
    main()