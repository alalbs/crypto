from pycoingecko import CoinGeckoAPI
import telebot


cg = CoinGeckoAPI()

price = cg.get_price(ids=['bitcoin', 'ethereum', 'prosper', 'frontier-token', 'pancakeswap-token', 'bdollar', 'bdollar-share'], vs_currencies='usd')

bot = telebot.TeleBot("1577238504:AAHKc7bM48I--iPgU7igFM1rH_T2Ge9vhH0", parse_mode=None)

@bot.message_handler(commands=['check'])
def send_welcome(message):
	bot.reply_to(message, f"btc - {price['bitcoin']['usd']}\neth - {price['ethereum']['usd']}\nfront - {price['frontier-token']['usd']}\n\
cake - {price['pancakeswap-token']['usd']}\nbdo - {price['bdollar']['usd']}\nsbdo - {price['bdollar-share']['usd']}\nprosper - {price['prosper']['usd']}")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	try:
		bot.reply_to(message, cg.get_price(ids=str(message.text).lower(), vs_currencies='usd')[str(message.text).lower()]['usd'])
	except:
		bot.reply_to(message, "Key error")




bot.polling()