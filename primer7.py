#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Написать программу, которая считывает текст из файла и выводит на экран только предложения, содержащие запятые.
# Каждое предложение в файле записано на отдельной строке.

if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as f:
        sentences = f.readlines()

    # Вывод предложений с запятыми.
    for sentence in sentences:
        if "," in sentence:
            print(sentence)
