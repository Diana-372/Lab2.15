#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == "__main__":
    def list_txt_files():
        current_directory = os.getcwd()
        txt_files = [file for file in os.listdir(current_directory) if file.endswith(".txt")]

        if txt_files:
            print("Список файлов с расширением .txt:")
            for file in txt_files:
                print(file)
            print(f"Общее количество файлов: {len(txt_files)}")
        else:
            print("В текущей директории нет файлов с расширением .txt")


    # Вызов функции
    list_txt_files()
