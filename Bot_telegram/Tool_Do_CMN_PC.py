import random
import shutil
from PIL import Image
import requests
import urllib.request
from pynput.keyboard import Key, Controller


def random_name():
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    name = str(random.randint(12,124))+random.choice(string)+str(random.randint(12,122324))+random.choice(string)+str(random.randint(12,122324))+random.choice(string)+str(random.randint(12,122324))+random.choice(string)+str(random.randint(12,122324))+random.choice(string)+str(random.randint(12,122324))+random.choice(string)+str(random.randint(12,122324))+random.choice(string)
    return name
def download():
    url="https://image.thanhnien.vn/800/uploaded/congnguyen/2019_09_09/huanhoahong-1_ugww.jpg"
    full_name= "C:/Users/tuanpa48/Desktop/hehe.jpg"
    urllib.request.urlretrieve(url,full_name)

def copy_image():
        src= "C:/Users/tuanpa48/Desktop/hehe.jpg"
        dst = "C:/Users/tuanpa48/Desktop/" + random_name() + ".jpg"
        shutil.copyfile(src,dst)
        open_image=Image.open(dst)
        open_image.show()
download()
for i in range(1,10):
    copy_image()

def sceenshot():
    keyboard = Controller()
    with keyboard.pressed(Key.cmd_l):
        keyboard.press(Key.print_screen)
        keyboard.release('a')