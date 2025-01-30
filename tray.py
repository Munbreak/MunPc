import PIL.ImageGrab
import pystray
import sys
import os
import json
import customtkinter as CTk
from PIL import Image, ImageGrab, ImageDraw

root = os.getcwd()
tokens = {}

with open("tokens.json", 'r', encoding='utf-8') as file:
    tokens = json.load(file)

def exit():
    os.system('TASKKILL /F /IM main.exe')
    tray.stop()



def bottoken():
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


        def __init__(self):
            super().__init__()
            self.iconbitmap('logo.ico')
            self.geometry('600x180')
            self.title("MunPc 1.0")
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



            self.button_ok1 = CTk.CTkButton(master=self.first_frame, text='Ok', width=100, command=self.get_token)

            self.entertoken = CTk.CTkLabel(master=self.first_frame, text="Введи токен бота: ", font = self.font)
            self.enter_token.grid(row=10, column=0, padx=(0, 0))
            self.button_ok1.grid(row=10, column=300, padx=(0, 0))
            self.entertoken.grid(row=0, column=0, padx=(0, 112))


    if __name__ == '__main__':
        app = App()
        app.mainloop()
    f = open('first.pt', 'tw', encoding='utf-8')
    f.close


def you_id():
    class App(CTk.CTk):


        def get_id(self):
            newid = self.enter_id.get()

            tokens['You'] = newid
            print('Новый Id: ' + tokens['You'])

            with open('tokens.json', 'w') as file:
                json.dump(tokens, file)
            app.destroy()

        def __init__(self):
            super().__init__()
            self.iconbitmap('logo.ico')
            self.geometry('600x180')
            self.title("MunPc 1.0")
            self.resizable(False, False)
            self.logo = CTk.CTkImage(dark_image=Image.open('logo.png'), size=(600, 100))
            self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)

            self.logo_label.grid(row=0, column=0)
            self.font = CTk.CTkFont(family= 'Franklin Gothic Heavy', size = 20)
            self.first_frame = CTk.CTkFrame(master=self, fg_color='transparent')
            self.first_frame.grid(row=1, column=0, pady=(0, 0), sticky='nsew')

            self.enter_id = CTk.CTkEntry(master=self.first_frame, width=300)
            self.enter_id.grid(row=10, column=0, padx=(0, 0))



            self.button_ok = CTk.CTkButton(master=self.first_frame, text='Ok', width=100, command=self.get_id)
            self.button_ok.grid(row=10, column=300, padx=(0, 0))



            self.enterid = CTk.CTkLabel(master=self.first_frame, text="Введи id пользователя: ", font= self.font)
            self.enterid.grid(row=0, column=0, padx=(0, 70))




    if __name__ == '__main__':
        app = App()
        app.mainloop()
    f = open('first.pt', 'tw', encoding='utf-8')
    f.close

image = PIL.Image.open('icon.png')
tray = pystray.Icon(name = 'MunPc', icon = image,title = 'MunPc', menu=pystray.Menu
                        (pystray.MenuItem('Изменить Id пользователя', you_id),
                         pystray.MenuItem('Поменять токен бота', bottoken),
                         pystray.MenuItem('Выход', exit)



    ))


tray.run()

