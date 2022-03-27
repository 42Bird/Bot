import telebot
from telebot import *


bot = telebot.TeleBot('5216771262:AAGwuaeGG8k6D5xho3zPN97Xl6fcGhCYp5k')
messageDeposit = ["Вклад",
                  "Раздел \"ВКЛАД\"\n\n Ваш ID: 4829342\n\nВаш вклад: 0.00 руб\nБаланс: 0.00 руб\nПартнеры: 0 чел\n\nПроцент прибыли: 3,2% за 24 часа\n\n Проценты начисляются на основной баланс"]
messagePartnership = ["Партнерство",
                      "Раздел \"ПАРТНЕРСТВО\"\n\nПриглашайте других пользователей на платформу и зарабатывайте с депозита вашего партнера\nПроцент с депозита:10%\nПартнеры:0 чел.\nЗаработок с партерства:0 руб.\n\nВаша партнерская ссылка"]
messageInformation = ["Информация"]
messageCalculation = ["Расчёт",
                      "Введите сумму, которую хотите рассчитать:",
                      "Введите целое число",
                      "В данном разделе вы можете рассчитать вашу прибыль, от суммы вклада:\n",
                      "Ваш вклад: ",
                      "\nПрибыль за сутки: ",
                      "\nПрибыль за месяц: ",
                      "\nПрибыль за год: ",
                      False]
out_money_information = ["Введите сумму вывода:"]
add_money_information = ["Реквизиты для пополнения:"]
reinvest_information = ["У вас на балансе: __\nУкажите суммму перевода на вклад"]

messageMainMenu = "ГЛАВНОЕ МЕНЮ"
startCommand = "start"
percent = 0.32

@bot.message_handler(commands=[startCommand])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    partershipButton = types.KeyboardButton(messagePartnership[0])
    depositButton = types.KeyboardButton(messageDeposit[0])
    calculationButton = types.KeyboardButton(messageCalculation[0])
    inforamationButton = types.KeyboardButton(messageInformation[0])
    markup.add(partershipButton)
    markup.add(depositButton)
    markup.add(calculationButton)
    markup.add(inforamationButton)
    bot.send_message(m.chat.id, messageMainMenu, reply_markup=markup)

@bot.message_handler(content_types=["text"])

def handle_text(message):
    if message.text.strip() == messageDeposit[0]:
      #  bot.send_message(message.chat.id, messageDeposit[1])
        
        keyboard = types.InlineKeyboardMarkup()
        key_add_money = types.InlineKeyboardButton(text='Пополнить', callback_data='add')
        keyboard.add(key_add_money)
        key_out_money = types.InlineKeyboardButton(text='Вывести', callback_data='out')
        keyboard.add(key_out_money)
        key_reinvest =  types.InlineKeyboardButton(text='Реинвестировать', callback_data='reinvest')
        keyboard.add(key_reinvest)
        bot.send_message(message.chat.id, text = messageDeposit[1], reply_markup=keyboard)
        
    elif message.text.strip() == messagePartnership[0]:
        bot.send_message(message.chat.id, messagePartnership[1])
    elif message.text.strip() == messageCalculation[0]:
        bot.send_message(message.chat.id, messageCalculation[1])
        messageCalculation[-1] = True
             
    elif messageCalculation[-1] == True:
        try:
            deposit = int(message.text)
            messageCalculationOutput = messageCalculation[3]+messageCalculation[4]+str(deposit)+messageCalculation[5]+str(deposit*percent)+messageCalculation[6]+str(deposit*percent*30)+messageCalculation[7]+str(deposit*percent*360)
            bot.send_message(message.chat.id, messageCalculationOutput)
        except ValueError:
            bot.send_message(message.chat.id,messageCalculation[2])

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "out":
        bot.send_message(call.message.chat.id, out_money_information[0])
    elif call.data == "add":
        bot.send_message(call.message.chat.id, add_money_information[0])
    elif call.data == "reinvest":
        bot.send_message(call.message.chat.id, reinvest_information[0])
'''
def is_subscribed(chat_id, user_id):
    try:
        bot.get_chat_member(chat_id, user_id)
        return True
    except ApiTelegramException as e:
        if e.result_json['description'] == 'Bad Request: user not found':
            return False
'''

bot.polling(none_stop=True, interval=0)
