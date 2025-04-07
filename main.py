import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import asyncio

# Inicializa variáveis de acertos e erros
acertos = 0
erros = 0

# Mensagens personalizadas
def gerar_sinal():
    resultado = random.choice(["acima de 2.0", "entre 1.5 e 2.0", "acima de 1.8", "acima de 3.0"])
    mensagem = f"""
🚀 *SINAL IDENTIFICADO*

🎯 _Padrão de voo detectado!_
💡 Aposte com saída: *{resultado}*

⚠️ Siga a gestão de banca e mantenha o foco.
"""
    return mensagem

# Comandos do bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot do JetX ativado e pronto para enviar sinais automaticamente! 💥")

async def taxas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total = acertos + erros
    if total == 0:
        await update.message.reply_text("📊 Nenhum sinal enviado ainda.")
    else:
        taxa_acerto = (acertos / total) * 100
        taxa_erro = (erros / total) * 100
        await update.message.reply_text(
            f"📈 *Taxa de Acertos:* {taxa_acerto:.2f}%\n"
            f"📉 *Taxa de Erros:* {taxa_erro:.2f}%\n"
            f"✅ Acertos: {acertos}\n"
            f"❌ Erros: {erros}",
            parse_mode="Markdown"
        )

async def resetar_taxas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global acertos, erros
    acertos = 0
    erros = 0
    await update.message.reply_text("♻️ Taxas de acertos e erros foram resetadas com sucesso!")

# Envio de sinal automático (simulado a cada 30 segundos)
async def enviar_sinal(context: ContextTypes.DEFAULT_TYPE):
    global acertos, erros
    chat_id = context.job.chat_id
    mensagem = gerar_sinal()
    await context.bot.send_message(chat_id=chat_id, text=mensagem, parse_mode="Markdown")
    if random.random() > 0.2:  # Simula 80% de acertos
        acertos += 1
    else:
        erros += 1

async def ativar_sinais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 Sinais ativados! Você receberá atualizações a cada rodada.")
    context.job_queue.run_repeating(enviar_sinal, interval=30, first=5, chat_id=update.message.chat_id)

# Inicialização do bot
logging.basicConfig(level=logging.INFO)
token = os.getenv("TELEGRAM_BOT_TOKEN")
app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("taxas", taxas))
app.add_handler(CommandHandler("resetartaxas", resetar_taxas))
app.add_handler(CommandHandler("sinais", ativar_sinais))

print("Bot iniciado...")
app.run_polling()  # ← Sem asyncio.run()
