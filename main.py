# This is a sample Python script.
import random
import tkinter

import telebot
import pystray
from telebot import types
import os
import json
import PIL.ImageGrab
from PIL import Image, ImageGrab, ImageDraw
import ctypes
from telebot.types import ReactionTypeEmoji
import customtkinter as CTk
import GPUtil
import uptime
import datetime
from sound import Sound







MessageBox = ctypes.windll.user32.MessageBoxW



a = 0
b = 0

root = os.getcwd() #Узнаем текущую директорию

#os.startfile(f'{root}' + '\\tray.exe') #Запуск скрипта для трея

tokens = {'Bot' : '', 'You' : ''} #Токен бота и пользователя
passwords = {} #Пароли хранятся в Passwords.json
pass2 = ''

if os.path.exists("first.mun"):

    pass
else:
    class App(CTk.CTk):

        def close(self):
            app.destroy()

        def get_token(self):
            newtoken = self.enter_token.get()
            tokens['Bot'] = newtoken
            print('Новый токен бота: ' + tokens['Bot'])
            with open('tokens.json', 'w') as file:
                json.dump(tokens, file)
            app.destroy()

        def get_id(self):
            newid = self.enter_id.get()

            tokens['You'] = newid
            print('Новый Id: ' + tokens['You'])

            with open('tokens.json', 'w') as file:
                json.dump(tokens, file)
            self.enterid.grid_remove()
            self.enter_id.delete(0, 1000)
            self.entertoken.grid(row=0, column=0, padx=(0, 112))
            self.enter_id.grid_remove()
            self.button_ok.grid_remove()
            self.enter_token.grid(row=10, column=0, padx=(0, 0))
            self.button_ok1.grid(row=10, column=300, padx=(0, 0))

        def __init__(self):
            super().__init__()
            self.iconbitmap('logo.ico')
            self.geometry('600x180')
            self.title("MunPc 1.2")
            self.resizable(False, False)
            self.logo = CTk.CTkImage(dark_image=Image.open('logo.png'), size=(600, 100))
            self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)

            self.logo_label.grid(row=0, column=0)
            self.font = CTk.CTkFont(family= 'Franklin Gothic Heavy', size = 20)
            self.first_frame = CTk.CTkFrame(master=self, fg_color='transparent')
            self.first_frame.grid(row=1, column=0, pady=(0, 0), sticky='nsew')

            self.enter_id = CTk.CTkEntry(master=self.first_frame, width=300)
            self.enter_id.grid(row=10, column=0, padx=(0, 0))

            self.enter_token = CTk.CTkEntry(master=self.first_frame, width=300)

            self.button_ok = CTk.CTkButton(master=self.first_frame, text='Ok', width=100, command=self.get_id)
            self.button_ok.grid(row=10, column=300, padx=(0, 0))

            self.button_ok1 = CTk.CTkButton(master=self.first_frame, text='Ok', width=100, command=self.get_token)

            self.enterid = CTk.CTkLabel(master=self.first_frame, text="Введи id пользователя: ", font= self.font)
            self.enterid.grid(row=0, column=0, padx=(0, 70))

            self.entertoken = CTk.CTkLabel(master=self.first_frame, text="Введи токен бота: ", font = self.font)


    if __name__ == '__main__':
        app = App()
        app.mainloop()
    f = open('first.mun', 'tw', encoding='utf-8')
    f.close



with open("Passwords.json", 'r', encoding='utf-8') as file:
    passwords = json.load(file)

with open("tokens.json", 'r', encoding='utf-8') as file:
    tokens = json.load(file)

me = tokens['You'] #IdПользователя
token = tokens['Bot'] #Токен бота из botFather
bot = telebot.TeleBot(token)

if os.path.exists("two.mun"):
    pass
else:
    tglink = telebot.types.InlineKeyboardMarkup()
    tglink.add(telebot.types.InlineKeyboardButton(text='Мой тг канал', url="https://t.me/Munbreak1"))
    bot.send_message(me, 'Спасибо за установку!', reply_markup = tglink)
    f = open('two.mun', 'tw', encoding='utf-8')
    f.close


#Кнопки

btnoff = types.KeyboardButton('🔴Выключить пк')
btnwinl = types.KeyboardButton('🔐Заблокировать')
btntimeoff = types.KeyboardButton('⏳Выключить через...')
btnscreen = types.KeyboardButton('📷Скрин')
btnreset = types.KeyboardButton('♻️Перезагрузить')
btnpass = types.KeyboardButton('💻Менеджер паролей')
btninfo = types.KeyboardButton('🌡 О пк')
btnvol = types.KeyboardButton('🔇 Звук')
btnother1 = types.KeyboardButton('🧰 Другое')
btnrand = types.KeyboardButton('🎰 Рандомное число')
btnupd = types.KeyboardButton('🌐Обновление')
btnother = types.KeyboardButton('💡Предложить идею')
btnid = types.KeyboardButton('🆔 Узнать id')
btnhours = types.KeyboardButton('Выключить через час')
btnoff_cancel = types.KeyboardButton('Отменить выключение')
btndice = types.KeyboardButton('🎲 Кинуть кубик')
updlink = telebot.types.InlineKeyboardMarkup()

btnback = types.KeyboardButton('⏪Назад')
other_btn = types.InlineKeyboardMarkup()


updlink.add(telebot.types.InlineKeyboardButton(text='Проверить обновление', url="https://t.me/MunPc"))
other_btn.add(telebot.types.InlineKeyboardButton(text='Предложить идею', url="https://t.me/MunPcFeedBack_bot"))

#Клавиатуры

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard= False)
other_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard= False)
id_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard= False)
off_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard= False)
off_timer_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard= False)

btnid1 = types.KeyboardButton('👤 Отправить пользователя', request_users=types.KeyboardButtonRequestUser(request_id=1))

main_keyboard.row(btnwinl, btnoff)
main_keyboard.row(btnscreen, btnreset)
main_keyboard.row(btntimeoff, btnpass)
main_keyboard.row(btninfo, btnvol)
main_keyboard.row(btnother1)
main_keyboard.row(btnupd, btnother)

other_keyboard.row(btnrand, btndice)
other_keyboard.row(btnid )
other_keyboard.row(btnback)
id_keyboard.row(btnid1)
id_keyboard.row(btnback)
off_keyboard.row(btnhours)
off_keyboard.row(btntimeoff)
off_keyboard.row(btnoff_cancel)
off_keyboard.row(btnback)

off_timer_keyboard.row(btnback)



#Кнопки Звук
vol_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
volmax = types.KeyboardButton("Звук на 100")

btnmin = types.KeyboardButton("Звук на 0")
btnset = types.KeyboardButton("Установить громкость на ...")
btnhalf = types.KeyboardButton("Звук на 50")

#Отображение кнопок в меню звука


vol_keyboard.row(volmax, btnset)
vol_keyboard.row(btnmin,btnhalf)
vol_keyboard.row(btnback)




if os.path.exists("two.mun"):
    bot.send_message(me, 'Компьютер включился!', reply_markup=main_keyboard)

else:
    pass





@bot.message_handler(content_types=["text", "users_shared"])

def start(sms):

    if sms.from_user.id == int(me):

        if sms.text == '🔴Выключить пк':
            os.system('shutdown -s /t 0 /f')
        elif sms.text == '🔐Заблокировать':
            ctypes.windll.user32.LockWorkStation()
        elif sms.text == "📷Скрин":

            bot.set_message_reaction(me, sms.message_id, [ReactionTypeEmoji("🥱")], is_big=True)
            screen = PIL.ImageGrab.grab()
            screen.save("screen.png", "png")
            screen = Image.open("screen.png")
            bot.send_chat_action(me, "upload_photo")
            bot.send_photo(me, open("screen.png", "rb"))
            bot.set_message_reaction(me, sms.message_id, [ReactionTypeEmoji("👍")], is_big=False)



        elif sms.text == '♻️Перезагрузить':
            os.system('shutdown -r -t 00')
        elif sms.text == '⏳Выключить через...':
            bot.send_message(me, "⏳Выключить через...", reply_markup=off_keyboard)
            bot.register_next_step_handler(sms, timeoff)
        elif sms.text == '💻Менеджер паролей':
            for key, value in passwords.items():
                global pass2
                pass2 += key + ":  " + value + ' | '
            bot.send_message(me, 'Твои пароли:\n' + str(pass2))
            pass2 = ''
        elif sms.text == '🌐Обновление':
            bot.send_message(me, 'Текущая версия: 1.2 | Проверить обновление можно ниже', reply_markup= updlink)
        elif sms.text == '💡Предложить идею':
            bot.send_message(me, 'Предлагай идеи для обновления по кнопке ниже!', reply_markup=other_btn)
        elif sms.text == '🌡 О пк':

            gpu = GPUtil.getGPUs()
            for gpu in gpu:
                gput = f"Температура GPU: {gpu.temperature} °C"

            time = uptime.uptime()
            time1 = convert_seconds(time)
            time3 = str(time1[:7])


            bot.send_message(me,gput + ' | ' + 'Время работы пк: ' + time3)
        elif sms.text == '🔇 Звук':
            bot.send_message(me, "Управление звуком 🔇", reply_markup=vol_keyboard)
            bot.register_next_step_handler(sms, sound1)

        elif sms.text == '🧰 Другое':
            bot.send_message(me, "🧰 Другое", reply_markup=other_keyboard)
            bot.register_next_step_handler(sms, other)


def other(sms):
    if sms.from_user.id == int(me):

        if sms.text == '🎰 Рандомное число':
            bot.send_message(me, 'Введи минимальное число: ')


            bot.register_next_step_handler(sms, min_rand)

        elif sms.text == "⏪Назад":
            back(sms)



        elif sms.text == '🎲 Кинуть кубик':
            bot.send_dice(me, '🎲')
            bot.register_next_step_handler(sms, other)

        elif sms.text == '🆔 Узнать id':
            bot.send_message(me, '✉️ Отправь пользователя/бота, Id которого ты хочешь узнать', reply_markup=id_keyboard)
            bot.register_next_step_handler(sms, get_id)
def back_other(sms):
    bot.send_message(me, '🧰 Другое', reply_markup=other_keyboard)
    bot.register_next_step_handler(sms, other)
def get_id(sms):

    try:
        id_get = sms.users_shared.user_ids[0]
        id_send = id_get.user_id
        bot.send_message(me, f'🆔 Пользователя: {id_send}', reply_markup=other_keyboard)
        bot.register_next_step_handler(sms, other)
    except:
        bot.send_message(me, '🧰 Другое', reply_markup=other_keyboard)
        bot.register_next_step_handler(sms, other)


def min_rand(sms):
    global a
    a = sms.text
    bot.send_message(me, 'Введи максимальное число: ')
    bot.register_next_step_handler(sms, random1)


def random1(sms):
    b = sms.text

    try:
        rand = random.randint(int(a), int(b))
        bot.send_message(me, rand, reply_markup=other_keyboard )
        bot.register_next_step_handler(sms, other)
    except:
        bot.send_message(me, 'Что-то пошло не так', reply_markup=other_keyboard)
        bot.register_next_step_handler(sms, other)

def timeoff(sms):


    if sms.text == '⏪Назад':
        back(sms)

    elif sms.text == 'Выключить через час':
        time2 = 3600
        os.system(f'shutdown -s -t {time2}')
        bot.send_message(me, "Пк будет выключен через час")
        bot.register_next_step_handler(sms, timeoff)
        on_or_no =+ 1

    elif sms.text == 'Отменить выключение':
        os.system('shutdown /a')
        on_or_no = 0

        bot.send_message(me, "Выключение отменено")
        bot.register_next_step_handler(sms, timeoff)

    elif sms.text == '⏳Выключить через...':
        bot.send_message(me, "Введи время до выключения в секундах:", reply_markup=off_timer_keyboard)
        bot.register_next_step_handler(sms, off_timer)


def off_timer(sms):
    if sms.text == '⏪Назад':
        bot.send_message(me, "⏳Выключить через...", reply_markup=off_keyboard)
        bot.register_next_step_handler(sms, timeoff)
    else:
        time1 = sms.text
        print(time1)
        os.system(f'shutdown -s -t {time1}')
        bot.send_message(me, "Пк будет выключен через: " + time1 + ' с', reply_markup=off_keyboard)
        bot.register_next_step_handler(sms, timeoff)
def sound1(sms):
	if sms.from_user.id == int(me):
		if sms.text == "Звук на 100":
			bot.send_chat_action(me, 'typing')
			try:
				Sound.volume_max()
				bot.send_message(me, "Установил громкость на 100")
				bot.register_next_step_handler(sms, sound1)
			except:
				bot.send_message(me,"Компьютер недоступен :( ")
				bot.register_next_step_handler(sms, sound1)
		elif sms.text == "Звук на 0":
			bot.send_chat_action(me, 'typing')
			try:
				Sound.volume_min()
				bot.send_message(me, "Установил громкость на 0")
				bot.register_next_step_handler(sms, sound1)
			except:
				bot.send_message(me,"Компьютер недоступен :( ")
				bot.register_next_step_handler(sms, sound1)
		elif sms.text == "Звук на 50":
			bot.send_chat_action(me, 'typing')
			try:
				Sound.volume_set(50)
				bot.send_message(me, "Установил громкость на 50")
				bot.register_next_step_handler(sms, sound1)
			except:
				bot.send_message(me,"Компьютер недоступен :( ")
				bot.register_next_step_handler(sms, sound1)

		elif sms.text == "Установить громкость на ...":
			bot.send_chat_action(me, 'typing')
			bot.send_message(me, "Введи новую громкость:")
			bot.register_next_step_handler(sms, soundset)

		elif sms.text == "⏪Назад":
			back(sms)

def soundset(sms):
	user_vol = sms.text
	try:
		bot.send_message(me, "Готово :)")
		Sound.volume_set(int(user_vol))
		bot.register_next_step_handler(sms, sound1)
	except:
		bot.send_message(me, "Компьютер недоступен :(")
		bot.register_next_step_handler(sms, sound1)

def back(sms):
	bot.register_next_step_handler(sms, start)
	bot.send_message(me, "Ты в главном меню", reply_markup = main_keyboard)


def convert_seconds(seconds):
    return str(datetime.timedelta(seconds=seconds))






bot.infinity_polling(timeout=10, long_polling_timeout = 5)

