# TO-DO: arreglar el import desde otras carpetas (headers/header.py)
# from webscrapping.headers.headers import get_random_header  # Importa desde la carpeta headers
from headers import get_random_header  # Importa desde la carpeta headers
import requests
from bs4 import BeautifulSoup
import json
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
app_dir = os.path.dirname(parent_dir)

# Obtén un encabezado aleatorio
headers = get_random_header()

url = 'https://www.coches.net/seat-toledo-2.0-tdi-140cv-sport-5p-diesel-2006-en-madrid-58396957-covo.aspx'

# Model
# Year
# Price
# Mileage
#  HP (Horsepower)
# Number of doors
# Color
# Fuel
# Transmission
# Location
# hnw-eosx-ysm

#  Function for scraping
def obtener_datos_coche(url):
    # Web request
    response = requests.get(url, headers=headers)
    # print(f'Code Response: {response}\n\n')
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup

def obtener_datos_html_statico():
    # Abre el archivo HTML y carga el contenido como texto
    with open("seat.html", "r", encoding="utf-8") as archivo:
        contenido_html = archivo.read()

    # Ahora 'contenido_html' contiene todo el HTML como texto
    return contenido_html


def static_scraping(contenido_html):
    # Parseamos el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(contenido_html, 'html.parser')
    script_tag = soup.find('script', type='application/ld+json')
    # Extrae el contenido del script y conviértelo en un diccionario
    if script_tag:
        json_data = json.loads(script_tag.string)
    else:
        print("No se encontró el script 'application/ld+json'.")

    # Datos básicos
    nombre = json_data['name']
    marca = json_data['brand']['name']
    modelo = json_data['model']
    url = json_data['url']
    imagen = json_data['image']
    fecha_produccion = json_data['productionDate']
    tipo_carroceria = json_data['bodyType']
    descripcion = json_data['description']
    color = json_data['color']

    # Oferta y precio
    precio = json_data['offers']['price']
    moneda = json_data['offers']['priceCurrency']

    # Imprime los valores
    print("Nombre:", nombre)
    print("Marca:", marca)
    print("Modelo:", modelo)
    print("URL:", url)
    print("Imagen:", imagen)
    print("Fecha de producción:", fecha_produccion)
    print("Tipo de carrocería:", tipo_carroceria)
    print("Descripción:", descripcion)
    print("Color:", color)
    print("Precio:", precio)
    print("Moneda:", moneda)


def url_scraping(soup):
    script_tag = soup.find('script', type='application/ld+json')
    # Extrae el contenido del script y conviértelo en un diccionario
    if script_tag:
        json_data = json.loads(script_tag.string)
    else:
        print("No se encontró el script 'application/ld+json'.")

    # Datos básicos
    nombre = json_data['name']
    marca = json_data['brand']['name']
    modelo = json_data['model']
    url = json_data['url']
    imagen = json_data['image']
    fecha_produccion = json_data['productionDate']
    tipo_carroceria = json_data['bodyType']
    descripcion = json_data['description']
    color = json_data['color']

    # Oferta y precio
    precio = json_data['offers']['price']
    moneda = json_data['offers']['priceCurrency']

    # Imprime los valores
    print("Nombre:", nombre)
    print("Marca:", marca)
    print("Modelo:", modelo)
    print("URL:", url)
    print("Imagen:", imagen)
    print("Fecha de producción:", fecha_produccion)
    print("Tipo de carrocería:", tipo_carroceria)
    print("Descripción:", descripcion)
    print("Color:", color)
    print("Precio:", precio)
    print("Moneda:", moneda)


def proceso_estatico():
    contenido_html = obtener_datos_html_statico()
    static_scraping(contenido_html)


def proceso_url():
    soup = obtener_datos_coche("https://www.coches.net/opel-astra-16-cdti-81kw-110cv-business-st-5p-diesel-2019-en-madrid-59020142-covo.aspx")
    url_scraping(soup)


def main():
    proceso_url()


if __name__ == '__main__':
    main()
