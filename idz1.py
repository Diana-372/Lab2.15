#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Написать программу, которая считывает текст из файла и выводит на экран только строки, не содержащие двузначных чисел.

if __name__ == "__main__":
    with open('idz1.txt', 'r') as file:
        # Читаем файл построчно
        for line in file:
            # Проверяем, содержит ли строка двузначные числа
            if not any(x.isdigit() and len(x) == 2 for x in line.split()):
                # Если строка не содержит двузначных чисел, выводим её
                print(line, end='')
