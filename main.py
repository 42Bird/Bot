# tg bot API 5549838211:AAFOBdRyPbbM0OV_-xiSEvFdEyMlugmJJrU

###################################################### Libraries
import telebot
import time
import os
import sqlite3
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests
import lxml
import re
from urllib.parse import urljoin, urlparse
from urllib.request import urlretrieve
import shutil
from transliterate import translit
from telebot import types
import telebot
from urllib.request import urlopen
#from goto import with_goto
import hashlib
import webbrowser
import emojis
###################################################### Libraries




PAGE_NUMBERS = []
# Создаем экземпляр бота
bot = telebot.TeleBot('6243379302:AAE0bZN3v32-V58wrge8c5ziALrVdX_Ue1c')

MAX_RETIES = 20
PASSWORD = '123'

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message: str, res=False) -> str:
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            #btn1 = types.KeyboardButton("ВОЕННЫЕ ПРЕСТУПНИКИ")
            #btn2 = types.KeyboardButton("БАТАЛЬОН РЕВАНШ")
            #btn3 = types.KeyboardButton("72 ЦИПСО")
            #btn4 = types.KeyboardButton("16 ЦИПСО")
            #btn5 = types.KeyboardButton("УЧАСТНИКИ АТО")
            #btn6 = types.KeyboardButton("СБУ")
            #btn7 = types.KeyboardButton("ГУР")
            #btn8 = types.KeyboardButton("СВР УКРАИНЫ")
            #btn9 = types.KeyboardButton("ПОЛК АЗОВ")
            #btn10 = types.KeyboardButton("БАТАЛЬОН ДОНБАСС")
            #btn11 = types.KeyboardButton("БАТАЛЬОН ТОРНАДО")
            #btn12 = types.KeyboardButton("БАТАЛЬОНЫ АЙДАР, АСКЕР, ДНЕПР-1")
            #btn13 = types.KeyboardButton("НАЦ. КОРПУС")
            #btn14 = types.KeyboardButton("ПРАВЫЙ СЕКТОР")
            #btn15 = types.KeyboardButton("УЛЬТРАС ФК")
            #btn16 = types.KeyboardButton("ПАТРИОТЫ УКРАИНЫ, ПРАВОРАДИКАЛЫ")
            #btn17 = types.KeyboardButton("ИНОСТРАННЫЕ НАЕМНИКИ")
            #btn18 = types.KeyboardButton("IT ARMY OF UA")
            #btn19 = types.KeyboardButton("SAVE UA")
            #btn20 = types.KeyboardButton("КИБЕРВОЙСКА УКРАИНЫ")
            btn1 = types.KeyboardButton("Поиск по фото 🔍 (В разработке)")
            btn2 = types.KeyboardButton("Голосовой поиск 💬(В разработке)")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text="Информационно-поисковая система 'Марс'", reply_markup=markup)            
            #bot.send_message(message.chat.id, text="Схема расположения региональных отделений националистических организаций на территории Украины", reply_markup=markup)

            #bot.send_photo(message.chat.id, photo=open('map.jpg', 'rb'))
            bot.send_photo(message.chat.id, photo=open('plakat14.jpg', 'rb')) 
            #bot.send_message(message.chat.id, text="Участие укронационалистов в антиправительственных митингах", reply_markup=markup)
            #bot.send_photo(message.chat.id, photo=open('naz2.jpg', 'rb'))
            #bot.send_photo(message.chat.id, photo=open('naz1.jpg', 'rb'))
            bot.send_message(message.chat.id, text="Введите ИМЯ, ФАМИЛИЯ ИМЯ, ФАМИЛИЯ ИМЯ ОТЧЕСТВО, а также возможен ввод рода деятельности, номера телефона, адреса проживания, должности, социальных сетей и даты рождения военнослужащего Украины для поиска", reply_markup=markup)
            bot.send_message(message.chat.id, text="Введите пароль!", reply_markup=markup)


users_auth = ['200']





@bot.message_handler(content_types=["text"])
def handle_text(message: str) -> str:
        
            
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        
        user_id = message.from_user.id
        
        PASSWORD_MD5 = '7c6a180b36896a0a8c02787eeafb0e4c'
        
                  

        if not(user_id in users_auth):
            message.text = bytes(message.text, encoding = 'utf8')
            
            password_test = hashlib.md5()
            password_test.update(b"%s" % message.text)
            password_test = password_test.hexdigest()
            
           
            if (password_test != PASSWORD_MD5):
    
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    bot.send_message(message.chat.id, text="ДОСТУП ЗАПРЕЩЕН!", reply_markup=markup)
                
            if (password_test == PASSWORD_MD5):
                
                    users_auth.append(user_id)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    bot.send_message(message.chat.id, text="Добро пожаловать!", reply_markup=markup)
              

                                        
        def nemezida(man:str, *args, **kwargs) -> str:        
            if user_id in users_auth:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
                name = message.text
                           
                ### nemezida
                        
                url = f"https://nemez1da.ru/page/1/?s={man}"
                
                        
                response = requests.get(url, allow_redirects = True,headers={
                        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                        })


               
                soup = BeautifulSoup(response.text, 'lxml')
                
                
                for page in soup.find_all('a', class_='page-numbers'):                    
                        PAGE_NUMBERS.append(page.text)
                        
                
                      
                
                for i in range (1,  40):           
                    url = f"https://nemez1da.ru/page/{i}/?s={man}"
                    print(url)
                            
                    response = requests.get(url, allow_redirects = True,headers={
                            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                            })



                    soup = BeautifulSoup(response.text, 'lxml')
                            
                    links = []

                    for link in soup.find_all('a', class_='simple-grid-grid-post-thumbnail-link'):
                                            links.append(link.get('href'))
                   # if not links:
                                            #bot.send_message(message.chat.id, text="Не найдено! Базы дополняются и обновляются", reply_markup=markup)    

                    

                                    
                    for link in links:
                                            response = requests.get(link, allow_redirects = True, headers={
                                    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                                    })

                                            soup = BeautifulSoup(response.text, 'lxml')
                                            
                                            name_tag = soup.find('h1')
                                            name = name_tag.text
                                            

                                            category_tag = soup.find(rel = 'category tag')
                                         
                                            
                                            info_tag = soup.find('div', class_ = 'entry-content simple-grid-clearfix')

                                            
                                            ### html


                                            f = open(f'{name} {category_tag.text}.html', 'w',  encoding="utf-8")
                                            html_template_new = f"""
                                                                    <html>
                                                                   
     
                                                                            <head>
                                                                                    
                                                                                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                                                                                    <meta name="viewport" content="width=device-width, initial-scale=1">
                                                                                    <title>{man}</title>
                                                                                    <base target="_blank">
                                                                            </head>

                                                                            

                                                                            <body>
                                                                                    <center>

                                                                                            <div class="information">
                                                                                            
                                                                                                   
                                                                                                    <div class="source"><p>ИНФОРМАЦИЯ О ЗАПРОСЕ</p></div>
                                                                                                    <div class="row">
                                                                                                            <div class="row-title">НАЙДЕНО: </div><div class="row-result">{name} {category_tag.text}</div></div>
                                                                                                            <div class="row-title"><p>Google Dorks (ChatGPT): </p></div><div class="row-result">https://www.google.com/search?q='{name}%20intext:'ВСУ'</div></div>
                                                                                                    <div class="row">
                                                                                                            
                                                                                            </div>

                                                                                    
                                                                                            <div class="information">
                                                                                                    <div class="source"><p>Информация:</p></div>
                                                                                                    {info_tag.text}
                                                                                            </div></div>
                                                                                    </center>
                                                                            </body>
                                                                    </html>
                                                                    """
                                            f.write(html_template_new)
                                            f.close()
                                            bot.send_document(message.chat.id, document = open(f'{name} {category_tag.text}.html','rb'))


                                            ### html
                                            
                                            # Загружаем картинки
                                            pictures = []

                                            try:
                                                    img = soup.find("div", {"class": "photos_single_place"}).find("img")
                                                    print(img["data-src"])
                                                    pictures.append(img["data-src"])
                                            except:
                                                    pass
                                            
                                            try:
                                                    p = requests.get(pictures[0], allow_redirects = True,headers={
                                                    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                                                    })
                                                    out = open("img.jpg", "wb")
                                                    out.write(p.content)
                                                    bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'))
                                                   
                                                            
                                                    out.close()
                                            except:
                                                    pass

                                            try:
                                                    p = requests.get(pictures[1], allow_redirects = True,headers={
                                                    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                                                    })
                                                    out = open("img.jpg", "wb")
                                                    out.write(p.content)
                                                    bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'))
                                                            
                                                    out.close()
                                            except:
                                                    pass
        def volunteer(man:str, *args, **kwargs) -> str:   
                       

            name_volunteer = message.text        
            url = f"https://volunteer.su/search?text={name_volunteer}"
                
                        
            response = requests.get(url, allow_redirects = True,headers={
                        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                        })

            soup = BeautifulSoup(response.text, 'lxml')
            print(url)
                            
            response = requests.get(url, allow_redirects = True,headers={
                            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                            })
                            
            links = []

            for link in soup.find_all('a', rel = 'tag'):
                                      
                                            links.append("https://volunteer.su" + link.get('href'))
            del links[-5:]
            print(links)

            for link in links:
                                            
                                            response = requests.get(link, allow_redirects = True, headers={
                                    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                                    })

                                            soup = BeautifulSoup(response.text, 'lxml')
                                            
                                            name_tag = soup.find('h2')
                                            name = name_tag.text
                                            print(name)
                                            

                                            #category_tag = soup.find(rel = 'category tag')
                                         
                                            
                                            info_tag = soup.find('div', class_ = 'content')

                                            
                                            ### html

                                            f = open(f'{name}.html', 'w',  encoding="utf-8")
                                            html_template_new = f"""
                                                                    <html>
                                                                   
     
                                                                            <head>
                                                                                    
                                                                                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                                                                                    <meta name="viewport" content="width=device-width, initial-scale=1">
                                                                                    <title>{message.text}</title>
                                                                                    <base target="_blank">
                                                                            </head>

                                                                            

                                                                            <body>
                                                                                    <center>

                                                                                            <div class="information">
                                                                                            
                                                                                                   
                                                                                                    <div class="source"><p>ИНФОРМАЦИЯ О ЗАПРОСЕ</p></div>
                                                                                                    <div class="row">
                                                                                                            <div class="row-title">НАЙДЕНО: </div><div class="row-result">{name}</div></div>
                                                                                                            <div class="row-title"><p>Google Dorks (ChatGPT): </p></div><div class="row-result">https://www.google.com/search?q='{name}%20intext:'ВСУ'</div></div>
                                                                                                    <div class="row">
                                                                                                            
                                                                                            </div>

                                                                                    
                                                                                            <div class="information">
                                                                                                    <div class="source"><p>Информация:</p></div>
                                                                                                    {info_tag.text}
                                                                                            </div></div>
                                                                                    </center>
                                                                            </body>
                                                                    </html>
                                                                    """
                                            f.write(html_template_new)
                                            f.close()
                                            bot.send_document(message.chat.id, document = open(f'{name}.html','rb'))


                                            # Картинки
                                            
                                            pictures = []

                                            try:
                                                        img = soup.find("div", {"class": "node-image"}).find("href")
                                                        print(img["data-src"])
                                                        pictures.append(img["data-src"])
                                            except:
                                                        pass
                                                
                                            try:
                                                        p = requests.get(pictures[0], allow_redirects = True,headers={
                                                        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                                                        })
                                                        out = open("img.jpg", "wb")
                                                        out.write(p.content)
                                                        bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'))
                                                       
                                                                
                                                        out.close()
                                            except:
                                                        pass

                                            try:
                                                        p = requests.get(pictures[1], allow_redirects = True,headers={
                                                        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                                                        })
                                                        out = open("img.jpg", "wb")
                                                        out.write(p.content)
                                                        bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'))
                                                                
                                                        out.close()
                                            except:
                                                        pass
        
        #volunteer(message.text)
        nemezida(message.text)
        


            ### Солнцепек
        '''
            HTMLFILE = open("messages.html", "r", encoding = 'utf8')
            index = HTMLFILE.read()
            SP = BeautifulSoup(index, 'lxml')
            SP_MAS = SP.find_all("div", class_="message default clearfix")
            for i in SP_MAS:
                    if (f"{name}" in i.text):
                        
                        
                        
                        f = open(f'{name}_SP.html', 'w',  encoding="cp1251")
                        html_template = f"""
                                                    <html>
                                                    <head>
                                                    <title>{name}</title>
                                                    </head>
                                                    <body>
                                                    <h2>{i.text[55:]}</h2>
                                                    
                          



                                                    </body>
                                                    </html>


                                """
                        f.write(html_template)
                        f.close()
                        bot.send_document(message.chat.id, document = open(f'{name}_SP.html','rb'))


'''

        

         

                                        
                                                     
            
        
            
            
                
# Запускаем бота
bot.polling(none_stop=True, interval=0)
