# -*- coding: utf-8 -*-
# Name: comprehend
# Version: 0.1a1
# Owner: Ruslan Korniichuk
# E-mail: ruslan.korniichuk(at)gmail.com

import boto3


def get_dominant_language(text, aws_region='eu-west-1'):
    """

    A UTF-8 text string. Each string should contain at least 20 characters and
    must contain fewer than 5,000 bytes of UTF-8 encoded characters.
    """

    def prepare_text(text):

        while len(bytes(text, 'utf-8')) > 4999:
            text = text[:-1]
        return text

    dominant_language = None
    score_max = 0

    if len(text) < 20:
        return None, None

    comprehend = boto3.client('comprehend', region_name=aws_region)
    text = prepare_text(text)

    try:
        res = comprehend.detect_dominant_language(Text=text)
    except BaseException:
        return 1
    else:
        if isinstance(res, dict):
            meta_data = res.get('ResponseMetadata')
            if meta_data:
                status_code = meta_data.get('HTTPStatusCode')
                if status_code != 200:
                    return 1

        languages = res.get('Languages')
        if languages and isinstance(languages, list):
            for language in languages:
                language_code = language.get('LanguageCode')
                score = language.get('Score')
                if language_code and score:
                    if score > score_max:
                        score_max = score
                        dominant_language = language_code

    return dominant_language, score_max
