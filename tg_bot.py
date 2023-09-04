from random import shuffle

import psycopg2
import telebot

from config import settings
from config.settings import API_TOKEN

# Активируем бота
bot = telebot.TeleBot(API_TOKEN)

# Создаем пустой словарь для ответов пользователя
user_dict = {}


def get_data(theme, problem_complexity,
             conn=psycopg2.connect(dbname=settings.DATABASES['default']['NAME'],
                                   user=settings.DATABASES['default']['USER'],
                                   password=settings.DATABASES['default']['PASSWORD'])):
    """Функция, которая получает из базы данных задачи по критериям пользователя, перемешивает их и возвращает 10 штук"""
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT * FROM problems_problem WHERE theme like '%{theme}%' AND problem_complexity = '{problem_complexity}'")
            rows = cur.fetchall()
            data = []
            for row in rows:
                data.append(str(row))
            shuffle(data)
    return data[:11]


def get_problem(number_of_problem,
                conn=psycopg2.connect(dbname=settings.DATABASES['default']['NAME'],
                                      user=settings.DATABASES['default']['USER'],
                                      password=settings.DATABASES['default']['PASSWORD'])):
    """Функция, которая получает из базы данных задачи по критериям пользователя, перемешивает их и возвращает 10 штук"""
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT * FROM problems_problem WHERE number_of_problem = '{number_of_problem}'")
            rows = cur.fetchall()
            data = []
            for row in rows:
                data.append(row)
    return data


@bot.message_handler(commands=['start'])
def send_welcome(message):
    '''Функция приветствия бота'''
    chat_id = message.chat.id
    user_dict['chat_id'] = chat_id
    msg = bot.reply_to(message, """\
Привет!
Если хочешь найти определенную задачу, то пришли ее номер, если хочешь получить подборку задач, то напиши слово пропустить
""")
    bot.register_next_step_handler(msg, find_problem)


def find_problem(message):
    '''Функция поиска конкретной задачи'''
    try:
        user_answer = message.text.lower()
        if user_answer == "пропустить":
            msg = bot.reply_to(message, """\
        Напиши сложность задач
        """)
            bot.register_next_step_handler(msg, problem_complexity)
        else:
            try:
                bot.send_message(user_dict['chat_id'], str(get_problem(user_answer)[0]))
            except Exception as e:
                bot.reply_to(message, 'oooops')
    except Exception as e:
        bot.reply_to(message, 'oooops')


def problem_complexity(message):
    '''Функция получения сложности задачи'''
    try:
        problem_complexity = message.text
        user_dict['problem_complexity'] = problem_complexity
        if not problem_complexity.isdigit():
            msg = bot.reply_to(message, 'Сложность задачи болжна содержать цифры. Уточни сложность задачи?')
            bot.register_next_step_handler(msg, theme)
            return
        msg = bot.reply_to(message, 'Напиши тему на английском языке')
        bot.register_next_step_handler(msg, theme)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def theme(message):
    '''Функция получения темы задачи и отправки сообщения с задачами'''
    try:
        theme = message.text.lower()
        user_dict['theme'] = theme
        bot.send_message(user_dict['chat_id'], 'Вот твои задачи:')
        bot.send_message(user_dict['chat_id'], '\n'.join(get_data(user_dict['theme'], user_dict['problem_complexity'])))
    except Exception as e:
        bot.reply_to(message, 'oooops')


# Метод для обхода падения бота путем перезапуска его
bot.infinity_polling()
