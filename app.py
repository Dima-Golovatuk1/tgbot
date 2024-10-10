import telebot

bot = telebot.TeleBot('7210915615:AAEKImwdxe9MWYDsLyEorjrc9k4P5EGeWJc')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привіт {message.from_user.first_name} введи яка в тебе зараз температура температуру градуси Цельсія')

@bot.message_handler()
def info(message):
    try:
        text = message.text.replace('°C', '').strip()
        if float(text) <= 0:
            bot.send_message(message.chat.id,
                         f'A cold, isn’t it?.')
        elif 10 > float(text) > 0:
            bot.send_message(message.chat.id,
                         f'Cool.')
        elif 100 > float(text) > 40:
            bot.send_message(message.chat.id,
                            f'Wear something black')
        elif float(text) == 5499:
            bot.send_message(message.chat.id,
                         f'https://www.google.com/search?q=%D1%82%D0%B5%D0%BC%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D1%83%D1%80%D0%B0+%D1%81%D0%BE%D0%BD%D1%86%D1%8F+%D0%B2+%D0%B3%D1%80%D0%B0%D0%B4%D1%83%D1%81%D0%B0%D1%85+%D1%86%D0%B5%D0%BB%D1%8C%D1%81%D1%96%D1%8F&sca_esv=12e82f26f75a1e30&sxsrf=ADLYWIKkpdtvtvkQJbIERIzYpf_9pllRew%3A1728582946136&ei=IhUIZ4P1B4mExc8Py5TnwAE&oq=%D1%82%D0%B5%D0%BC%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D1%83%D1%80%D0%B0+%D1%81%D0%BE%D0%BD%D1%86%D1%8F+%D0%B2+%D0%B3%D1%80%D0%B0%D0%B4%D1%83%D1%81%D0%B0%D1%85+%D1%86&gs_lp=Egxnd3Mtd2l6LXNlcnAiONGC0LXQvNC_0LXRgNCw0YLRg9GA0LAg0YHQvtC90YbRjyDQsiDQs9GA0LDQtNGD0YHQsNGFINGGKgIIADIFECEYoAEyBRAhGKABMgUQIRifBTIFECEYnwUyBRAhGJ8FSKkKUHlYhwJwAHgCkAEAmAHyAaAB8gKqAQUwLjEuMbgBAcgBAPgBAZgCA6AChwPCAgQQABhHwgIGEAAYFhgewgIIEAAYgAQYogSYAwCIBgGQBgiSBwUxLjEuMaAH0Qo&sclient=gws-wiz-serp')
        else:
            bot.send_message(message.chat.id,
                         f'Nice weather we’re having.')
    except ValueError:
        bot.send_message(message.chat.id, 'Будьласка ведіть число або тепмпературу в °C')
bot.polling(non_stop=True)