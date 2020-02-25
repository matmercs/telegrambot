# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import telebot
import random

NUM = 0
LENGTH = 0


def getpass():
    def isok(word):
        nums = False
        small = False
        big = False
        symbols = False
        for j in word:
            if j.isnumeric():
                nums = True
            elif j.isalpha():
                if j.isupper():
                    big = True
                else:
                    small = True
            else:
                symbols = True
        return nums and small and big and symbols

    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    passwords = []
    while len(passwords) < NUM:
        password = ''
        for i in range(LENGTH):
            password += random.choice(chars)
        if isok(password):
            passwords.append(password)
    s = ''
    for i in passwords:
        s += i + '\n'
    return s


bot = telebot.TeleBot('1083493676:AAHHlgUnzBhDfohgLmuulYIrN5b7gLyExsg')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который умеет генерировать надежные пароли. '
                                      'Чтобы начать, введи, пароли какой длины ты хочешь получить.')


@bot.message_handler(content_types=['text'])
def send_text(message):
    global NUM
    NUM = 5
    global LENGTH
    LENGTH = int(message.text)
    bot.send_message(message.chat.id, 'Готово! Вот твои пароли:\n' + getpass())


bot.polling()
