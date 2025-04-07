import os
import time
import random
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ativa log básico
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Obtem token do ambiente
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Histórico fictício de voos para simulação
historico_voos = [1.25, 1.7, 2.0, 1.1, 5.0, 1.3, 1.5, 3.2, 1.0, 2.8]

# Função de previsão baseada em padrão simples
def prever_voo():
    media = sum(historico_voos[-5:]) / 5
    variacao = random.uniform(-0.3, 0.3)
    previsao = round(media + variacao, 2)
    return previsao if previsao > 1.0 else 1.01

# Comando para iniciar o bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot JetX ativado! Enviarei sinais a cada rodada automaticamente.")

# Função que simula nova rodada e envia sinal
async def enviar_sinal(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    previsao = prever_voo()
    historico_voos.append(previsao)
    await context.bot.send_message(chat_id=chat_id, text=f"Próximo voo estimado: {previsao}x")

# Comando para começar a enviar sinais automaticamente
async def sinais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Envio de sinais iniciado.")
    context.job_queue.run_repeating(enviar_sinal, interval=60, first=5, chat_id=update.effective_chat.id)

# Inicializa bot
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sinais", sinais))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

