from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
# from config.encrypted_decrypted import decrypt_telegram_token #TO-DO

# BotFather token // refactor
TOKEN = 'token'


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