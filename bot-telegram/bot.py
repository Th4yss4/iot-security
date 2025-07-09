from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 'INSIRA-TOKEN-BOT'  # Substitua pelo token do seu bot

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"Olá! Seu chat_id é: {chat_id}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot rodando... Envie /start no Telegram.")
app.run_polling()
