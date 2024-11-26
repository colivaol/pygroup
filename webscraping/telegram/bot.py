from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
import os
import sys

# Ruta al archivo actual
current_dir = os.path.dirname(__file__)
# Dos niveles arriba
grandparent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
parent_dir = os.path.dirname(current_dir)


# Agrega el directorio del abuelo al sys.path
sys.path.append(grandparent_dir)

from config.encrypted_decrypted import encrypt_telegram_key
from webscraping.car.coches_net import run_coches_net

TOKEN = encrypt_telegram_key()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # car = run_coches_net()
    await update.message.reply_text("Hola!!!! Envíame una URL :)")

# Función que maneja la URL proporcionada por el usuario
async def handle_url(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Captura la URL que envía el usuario
    url = update.message.text
    # Aquí puedes llamar a la función para procesar la URL
    car_data = run_coches_net(url)
    print(f"Soy el car_data{car_data}")
    await update.message.reply_text(f"Datos del coche: {car_data}")

    # Termina la conversación
    return ConversationHandler.END

# Configuración del bot
def main():

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_url)) # Aquí manejamos el mensaje de texto

    application.run_polling()


if __name__ == '__main__':
    main()