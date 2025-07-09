import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from twilio.rest import Client

# ========== CONFIGURAÇÕES ==========
TELEGRAM_TOKEN = 'INSIRA-TOKEM'  # SUBSTITUA AQUI


ACCOUNT_SID = 'INSIRA-SID'          # SUBSTITUA AQUI
AUTH_TOKEN = 'INSIRA-AUTH-TOKEN'            # SUBSTITUA AQUI
TWILIO_WHATSAPP_NUMBER = 'INSIRA-NUMERO'  # Sandbox do Twilio
NUMERO_DESTINO = 'INSIRA-NUMERO-DESTINO'     # Ex: whatsapp:+559998887766

ARQUIVO_LOCALIZACOES = "localizacoes.txt"


# ========== COMANDOS DO BOT ==========

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot ativo!\n\n"
        "Envie uma imagem (foto ou documento), ou use:\n"
        "🗺️ /ccn → mapa do CCN\n"
        "🗺️ /cchl → mapa do CCHL\n"
        "📍 Envie sua localização\n"
        "🚨 /alerta → enviar alerta via WhatsApp"
    )


async def enviar_mapa_ccn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await enviar_imagem_por_nome(update, "mapa_ccn.jpg", "CCN")


async def enviar_mapa_cchl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await enviar_imagem_por_nome(update, "mapa_cchl.jpg", "CCHL")


# ========== TRATAMENTO DE MÍDIA ==========

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    filename = f"{update.message.from_user.id}_{photo.file_unique_id}.jpg"
    await file.download_to_drive(filename)
    await update.message.reply_text(f"📸 Imagem salva como {filename}")
    print(f"[📥 FOTO] {filename}")


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    if doc and doc.mime_type.startswith("image/"):
        file = await doc.get_file()
        filename = f"{update.message.from_user.id}_{doc.file_unique_id}_{doc.file_name}"
        await file.download_to_drive(filename)
        await update.message.reply_text(f"🗂️ Documento salvo como {filename}")
        print(f"[📥 DOCUMENTO] {filename}")
    else:
        await update.message.reply_text("❌ Isso não é uma imagem.")
        print("[⚠️ DOCUMENTO] Não é imagem.")


async def enviar_imagem_por_nome(update: Update, nome_arquivo: str, nome_legenda: str):
    if not os.path.isfile(nome_arquivo):
        await update.message.reply_text(f"⚠️ O arquivo {nome_arquivo} não foi encontrado.")
        print(f"[❌ ERRO] Arquivo não encontrado: {nome_arquivo}")
        return

    with open(nome_arquivo, 'rb') as img:
        await update.message.reply_photo(photo=img, caption=f"🗺️ Mapa do {nome_legenda}")
        print(f"[📤 ENVIO] {nome_arquivo}")


# ========== LOCALIZAÇÃO ==========

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    location = update.message.location

    if not location:
        await update.message.reply_text("❌ Localização inválida.")
        return

    latitude = location.latitude
    longitude = location.longitude
    nome_usuario = user.full_name

    with open(ARQUIVO_LOCALIZACOES, "a") as f:
        f.write(f"{nome_usuario} ({user.id}) - {latitude}, {longitude}\n")

    await update.message.reply_text(f"📍 Localização recebida! Enviado para equipe de segurança.\nLat: {latitude}\nLon: {longitude}")
    print(f"[📍 LOCALIZAÇÃO] {nome_usuario}: {latitude}, {longitude}")


# ========== ALERTA VIA WHATSAPP ==========

def enviar_whatsapp(mensagem: str, numero_destino: str):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=mensagem,
        to=numero_destino
    )
    print(f"✅ WhatsApp enviado! SID: {message.sid}")


async def alerta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        enviar_whatsapp("🚨 ALERTA: Um usuário acionou o botão no bot Telegram!", NUMERO_DESTINO)
        await update.message.reply_text("📲 Mensagem enviada via WhatsApp!")
    except Exception as e:
        await update.message.reply_text("❌ Falha ao enviar via WhatsApp.")
        print(f"[ERRO WHATSAPP] {e}")


# ========== INICIAR BOT ==========

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ccn", enviar_mapa_ccn))
    app.add_handler(CommandHandler("cchl", enviar_mapa_cchl))
    app.add_handler(CommandHandler("alerta", alerta))

    # Mensagens (imagem, localização)
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.Document.IMAGE, handle_document))
    app.add_handler(MessageHandler(filters.LOCATION, handle_location))

    print("🤖 Bot rodando... comandos: /start /ccn /cchl /alerta")
    app.run_polling()
