from webscraping.headers.headers import get_random_header
import requests
from bs4 import BeautifulSoup
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
app_dir = os.path.dirname(parent_dir)


headers = get_random_header()



#  Function for scraping
def obtener_datos_coche(url):
    response = requests.get(url, headers=headers) 
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup


def obtener_datos_html_statico():

    with open("seat.html", "r", encoding="utf-8") as archivo:
        contenido_html = archivo.read()


    return contenido_html


def static_scraping(contenido_html):
    # Parseamos el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(contenido_html, 'html.parser')
    script_tag = soup.find('script', type='application/ld+json')
    # Extrae el contenido del script y conviértelo en un diccionario
    if script_tag:
        json_data = json.loads(script_tag.string)
        print(json_data)
    else:
        print("No se encontró el script 'application/ld+json'.")


    nombre = json_data['name']
    marca = json_data['brand']['name']
    modelo = json_data['model']
    url = json_data['url']
    imagen = json_data['image']
    fecha_produccion = json_data['productionDate']
    tipo_carroceria = json_data['bodyType']
    descripcion = json_data['description']
    color = json_data['color']


    precio = json_data['offers']['price']
    moneda = json_data['offers']['priceCurrency']


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



    nombre = json_data['name']
    marca = json_data['brand']['name']
    modelo = json_data['model']
    url = json_data['url']
    imagen = json_data['image']
    fecha_produccion = json_data['productionDate']
    tipo_carroceria = json_data['bodyType']
    descripcion = json_data['description']
    color = json_data['color']


    precio = json_data['offers']['price']
    moneda = json_data['offers']['priceCurrency']

    datos = {
        "nombre": nombre,
        "marca": marca,
        "modelo": modelo,
        "url": url,
        "imagen": imagen,
        "fecha_produccion": fecha_produccion,
        "tipo_carroceria": tipo_carroceria,
        "descripcion": descripcion,
        "color": color,
        "precio": precio,
        "moneda": moneda
    }

    return datos


def static_process():
    contenido_html = obtener_datos_html_statico()
    static_scraping(contenido_html)


def dynamic_process(url):
    soup = obtener_datos_coche(url)
    return url_scraping(soup)



def run_coches_net(url):
    return dynamic_process(url)


if __name__ == '__main__':
    run_coches_net()
