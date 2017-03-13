#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ChineseLocalizer:
    def __init__(self):
        self.dictionary = dict(dog = "狗", cat = "猫")

    def localize(self, word):
        try:
            return self.dictionary[word]
        except KeyError:
            return str(word)

class EnglishLocalizer:
    def localize(self, word):
        return str(word)

def get_localizer(lang = "english"):
    languages = dict(chinese = ChineseLocalizer, english = EnglishLocalizer)
    return languages[lang]()

c, e = get_localizer("chinese"), get_localizer()
for word in "dodo dog and mimi cat".split():
    print(e.localize(word), c.localize(word))