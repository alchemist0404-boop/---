import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Логи — ОБЯЗАТЕЛЬНЫ для Railway
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("Переменная окружения BOT_TOKEN не задана")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Бот запущен и работает.\n"
        "Это базовая версия. Дальше добавим читалку."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # Long polling — подходит для Railway
    app.run_polling()

if __name__ == "__main__":
    main()
