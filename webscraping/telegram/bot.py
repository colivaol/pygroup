from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
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


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     car = run_coches_net()
#     await update.message.reply_text(car)


# Configuración del bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Envíame url de www.coches.net")


# Función para manejar el comando con argumentos
async def buscar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Recoge los argumentos después del comando
    argumentos = ' '.join(context.args)  # Une todos los argumentos en un string
    if not argumentos:
        await update.message.reply_text("Por favor, proporciona una url de www.coches.net")
        return

    # Llama a la función personalizada con los datos del usuario
    resultado = realizar_busqueda(argumentos)

    # Devuelve el resultado al usuario
    await update.message.reply_text(resultado)

# Función personalizada para usar los datos que envía el usuario
def realizar_busqueda(texto):
    # Aquí usarías `texto` en tu lógica personalizada, como scraping o búsqueda
    print(f'TEXTO:{texto}')
    coche = run_coches_net(texto)
    print(coche)
    return coche


# Función para manejar mensajes de texto sin comandos
async def manejar_texto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto_usuario = update.message.text  # Captura el texto enviado por el usuario

    # Llama a la función personalizada con el texto
    resultado = realizar_busqueda(texto_usuario)

    # Responde al usuario
    await update.message.reply_text(f"Resultado para tu url de www.coches.net: {resultado}")


# Configuración del bot
def main():

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("buscar", buscar))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_texto))
    application.run_polling()


if __name__ == '__main__':
    main()