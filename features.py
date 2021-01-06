# -*- coding: utf-8 -*-
# Name: features
# Version: 0.1a3
# Owner: Ruslan Korniichuk
# E-mail: ruslan.korniichuk(at)gmail.com

import os

from nltk.stem import PorterStemmer
import requests

from promovolt.readability import word_counter, sentence_counter
from promovolt.syllables import syllable_counter


def acs(text):
    """ACS -- Average number of Characters per Sentence."""

    acs = None

    characters_num = len(text)
    sentences_num, sentences = sentence_counter(text, 'en')
    if sentences_num != 0:
        acs = characters_num / sentences_num
    return acs


def acw(text):
    """ACW -- Average number of Characters per Word"""

    acw = None

    words_num, words = word_counter(text, 'en')
    characters_num = 0
    for word in words:
        characters_num += len(word)

    if words_num != 0:
        acw = characters_num / words_num
    return acw


def ass(text):
    """ASS -- Average number of Syllables per Sentence."""

    ass = None

    words_num, words = word_counter(text, 'en')
    syllables_num = 0
    for word in words:
        syllables_num += syllable_counter(word)

    sentences_num, sentences = sentence_counter(text, 'en')
    if sentences_num != 0:
        ass = syllables_num / sentences_num
    return ass


def asw(text):
    """ASW -- Average number of Syllables per Word."""

    asw = None

    words_num, words = word_counter(text, 'en')
    syllables_num = 0
    for word in words:
        syllables_num += syllable_counter(word)

    if words_num != 0:
        asw = syllables_num / words_num
    return asw


def aws(text):
    """AWS -- Average number of Words per Sentence."""

    aws = None
    words_num, words = word_counter(text, 'en')
    sentences_num, sentences = sentence_counter(text, 'en')
    if sentences_num != 0:
        aws = words_num / sentences_num
    return aws


def pdw(text):
    """PDW -- Percentage of Difficult Words.

    According to New Dale-Chall readability index.
    """

    pdw = None
    difficult_words_num = 0

    path = '/tmp/new_dale-chall_simple_words_en_stemmed.txt'
    if not os.path.exists(path):
        url = 'https://raw.githubusercontent.com/korniichuk/phd/master/resources/new_dale-chall_simple_words_en_stemmed.txt'  # noqa: E501
        r = requests.get(url)
        with open(path, 'w') as f:
            f.write(r.text)
    with open(path, 'r') as f:
        new_dale_chall_simple_words = f.read().splitlines()

    words_num, words = word_counter(text, 'en')
    stemmer = PorterStemmer()
    for word in words:
        word_lower = word.lower().strip()
        word_stemmed = stemmer.stem(word_lower)
        if word_stemmed not in new_dale_chall_simple_words:
            difficult_words_num += 1

    if words_num != 0:
        pdw = difficult_words_num / words_num
    return pdw


def pew(text):
    """PEW -- Percentage of Echomimetic (onomatopoeic) Words."""

    pew = None
    onomatopoeic_words_num = 0

    path = '/tmp/onomatopoeic_words_en-1.0.txt'
    if not os.path.exists(path):
        url = 'https://raw.githubusercontent.com/korniichuk/phd/master/resources/onomatopoeic_words_en-1.0.txt'  # noqa: E501
        r = requests.get(url)
        with open(path, 'w') as f:
            f.write(r.text)
    with open(path, 'r') as f:
        onomatopoeic_words = f.read().splitlines()

    words_num, words = word_counter(text, 'en')
    for word in words:
        word_lower = word.lower().strip()
        if word_lower in onomatopoeic_words:
            onomatopoeic_words_num += 1

    if words_num != 0:
        pew = onomatopoeic_words_num / words_num
    return pew


def pmw(text):
    """PMW -- Percentage of Multi-character Words."""

    pmw = None
    multi_character_words_num = 0

    words_num, words = word_counter(text, 'en')
    for word in words:
        if len(word) > 6:
            multi_character_words_num += 1
    if words_num != 0:
        pmw = multi_character_words_num / words_num
    return pmw


def ppw(text):
    """PPW -- Percentage of Polysyllabic Words."""

    ppw = None
    polysyllabic_words_num = 0

    words_num, words = word_counter(text, 'en')
    for word in words:
        if syllable_counter(word) >= 3:
            polysyllabic_words_num += 1
    if words_num != 0:
        ppw = polysyllabic_words_num / words_num
    return ppw


def psw(text):
    """PSW -- Percentage of Selling Words."""

    psw = None
    selling_words_num = 0

    path = '/tmp/selling_words_en_stemmed.txt'
    if not os.path.exists(path):
        url = 'https://raw.githubusercontent.com/korniichuk/phd/master/resources/selling_words_en_stemmed.txt'  # noqa: E501
        r = requests.get(url)
        with open(path, 'w') as f:
            f.write(r.text)
    with open(path, 'r') as f:
        selling_words = f.read().splitlines()

    words_num, words = word_counter(text, 'en')
    stemmer = PorterStemmer()
    for word in words:
        word_lower = word.lower().strip()
        word_stemmed = stemmer.stem(word_lower)
        if word_stemmed in selling_words:
            selling_words_num += 1

    if words_num != 0:
        psw = selling_words_num / words_num
    return psw


def puw(text):
    """PUW -- Percentage of Unique Words."""

    puw = None

    words_num, words = word_counter(text, 'en')
    stemmer = PorterStemmer()
    stemmed_words = []
    for word in words:
        word_lower = word.lower().strip()
        stemmed_words.append(stemmer.stem(word_lower))
    unique_words_num = len(set(stemmed_words))

    if words_num != 0:
        puw = unique_words_num / words_num
    return puw
