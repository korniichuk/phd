# -*- coding: utf-8 -*-
# Name: accessory
# Version: 0.1a6
# Owner: Ruslan Korniichuk
# E-mail: ruslan.korniichuk(at)gmail.com

import re

from bs4 import BeautifulSoup


def clean_text_data(data):

    result = []

    for text in data:
        text = text.strip()
        while '  ' in text:
            text = text.replace('  ', ' ')
        if text[-1] not in ['.', '…', '?', '!']:
            text += '.'
        result.append(text)
    return result


def filter_text_data(data):

    result = []

    for text in data:
        if text == '':
            continue
        total_words = word_counter(text)
        if total_words < 2:
            continue
        soup = BeautifulSoup(text, 'lxml')
        text = soup.get_text(separator=' ')
        result.append(text)
    return result


def get_text_data(node, result=None):

    if result is None:
        result = []

    if type(node) is dict:
        for key, item in node.items():
            if key == 'Ghosts':
                continue
            elif (key == 'type') and (item == 'Text'):
                if '_value' in node:
                    result.append(node['_value'])
            elif (key == 'type') and (item == 'Input/Button'):
                if '_value' in node:
                    result.append(node['_value'])
            elif key == 'type':
                if 'placeholder' in node:
                    result.append(node['placeholder'])
            else:
                get_text_data(item, result=result)
    if type(node) is list:
        for element in node:
            get_text_data(element, result=result)
    return result


def word_counter(text):

    total_words = 0

    word_pattern = re.compile("(?:[a-zA-Z]+[-–’'`ʼ]?)*[a-zA-Z]+[’'`ʼ]?")
    words = word_pattern.findall(text)
    total_words = len(words)
    return total_words
