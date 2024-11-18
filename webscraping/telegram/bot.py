import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from config.encrypted_decrypted import decrypt_telegram_token

# BotFather token // refactor
TOKEN = '7317962628:AAHAebUzfe048cCmrFPwZfPUugETqXmVtYo'
url = 'https://www.coches.net/seat-toledo-1.0-tsi-70kw-stsp-reference-edition-5p-gasolina-2018-en-guipuzcoa-58932064-covo.aspx'


# Function for scraping
def obtener_datos_coche(url):
    try:
        # Web request
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get specific data
        name = soup.find('h1', {
            'class': 'mt-TitleBasic-title mt-TitleBasic-title--s mt-TitleBasic-title--black'}).text.strip()
        list_items = soup.find_all('li', class_='mt-PanelAdDetails-dataItem')
        cv: None
        for item in list_items:
            if 'cv' in item.text:  # Filtrar el elemento que contiene 'cv'
                cv = item.text.strip()  # Extraer el texto de ese elemento
                break

        # Print name
        return f"Nombre: {name}\n Año: {cv}"

    except Exception as e:
        return f"Error al obtener los datos: {e}"


# Función que maneja el comando /start
def start(update, context):
    update.message.reply_text("Hola! Envíame la URL de la página del coche y te devolveré los datos.")


# Función que maneja los mensajes con URLs
def handle_message(update, context):
    url = update.message.text
    if url.startswith("http"):
        # Llamar a la función para obtener los datos del coche
        datos = obtener_datos_coche(url)
        update.message.reply_text(datos)
    else:
        update.message.reply_text("Por favor, envíame una URL válida.")


# Configuración del bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Comandos del bot
    dp.add_handler(CommandHandler("start", start))

    # Manejador de mensajes (URLs)
    dp.add_handler(MessageHandler(filters.text, handle_message))

    # Iniciar el bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()