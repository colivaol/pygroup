from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import sys

# Ruta al archivo actual
current_dir = os.path.dirname(__file__)
# Un nivel arriba
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
# Dos niveles arriba
grandparent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
# Carpeta config
config_dir = os.path.abspath(os.path.join(current_dir, "..", "config"))

print("config_dir:", config_dir)
# print("parent_dir:", parent_dir)
# print("grandparent_dir:", grandparent_dir)
#
# Agrega el directorio del abuelo al sys.path
sys.path.append(grandparent_dir)

# Añadir la raíz del proyecto al PYTHONPATH
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from config.encrypted_decrypted import encrypt_telegram_key

# BotFather token // refactor
# TOKEN = '7317962628:AAEcORnIsf6fuvTnzQktx1XWc6GuhAVD55s'
TOKEN = encrypt_telegram_key()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello word")


# Configuración del bot
def main():
    print(TOKEN)
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


if __name__ == '__main__':
    main()