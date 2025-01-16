from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ApplicationBuilder

# Telegram Bot API Anahtarı
TOKEN = "8147471558:AAFOtCbuziPjvmWwVWmErOTnhXl1DSL8rB8"

# Telegram Bot Uygulaması
application = ApplicationBuilder().token(TOKEN).build()

# /start komutu
async def start(update, context):
    # Kullanıcıya gösterilecek mesaj
    message = "Welcome to Vaada Game! Click the button below to start your journey:"

    # Flask URL'si (Doğru port: 5000)
    flask_url = "http://127.0.0.1:5000/game"

    # Buton
    keyboard = [
        [InlineKeyboardButton("Visit Vaada Game", url=flask_url)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Mesajı gönder
    await update.message.reply_text(
        text=message,
        reply_markup=reply_markup
    )

# Komutları ekle
application.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    application.run_polling()
