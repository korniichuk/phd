# -*- coding: utf-8 -*-
# Name: accessory
# Version: 0.1a2
# Owner: Ruslan Korniichuk
# E-mail: ruslan.korniichuk(at)gmail.com

import re


def word_counter(text):

    total_words = 0

    word_pattern = re.compile("(?:[a-zA-Z]+[-–’'`ʼ]?)*[a-zA-Z]+[’'`ʼ]?")
    words = word_pattern.findall(text)
    total_words = len(words)
    return total_words
