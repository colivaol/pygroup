from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
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
    car = run_coches_net()
    await update.message.reply_text(car)


# Configuración del bot
def main():

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


if __name__ == '__main__':
    main()