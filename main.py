import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from jetx_signals import gerar_sinal_jetx
from stats import registrar_resultado, obter_taxas

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot de sinais JetX ativado com sucesso!")

async def sinal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sinal = gerar_sinal_jetx()
    registrar_resultado(sinal["resultado_real"])
    mensagem = f"""🚀 *SINAL GERADO* 🚀

🎯 Previsão de voo: até *{sinal['previsao']:.2f}x*
📊 Confiança: *{sinal['confianca']}%*
✅ Acertos: {sinal['acertos']} | ❌ Erros: {sinal['erros']}
📈 Taxa de acerto: *{sinal['taxa_acerto']}%*

Aposte com cautela e gestão. 🎯"""

    await context.bot.send_message(chat_id=CHAT_ID, text=mensagem, parse_mode="Markdown")

async def taxa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    acertos, erros, taxa = obter_taxas()
    msg = f"""📊 *Taxas de Acerto*

✅ Acertos: *{acertos}*
❌ Erros: *{erros}*
📈 Taxa de acerto: *{taxa}%*"""

    await update.message.reply_text(msg, parse_mode="Markdown")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sinal", sinal))
    app.add_handler(CommandHandler("taxa", taxa))

    print("🤖 Bot iniciado...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
