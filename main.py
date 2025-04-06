import telebot
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Fala, Marcos! Bot do JetX tá online. Envia /ajuda pra ver os comandos.")

@bot.message_handler(commands=["ajuda"])
def ajuda(message):
    texto = """
Comandos disponíveis:
/start - Inicia o bot
/ajuda - Mostra essa mensagem
"""
    bot.reply_to(message, texto)

bot.infinity_polling()
