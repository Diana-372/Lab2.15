#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Приведенный код для операционной системы Windows сменит текущий каталог на C:\Windows и выведет новое имя текущего
# каталога.

if __name__ == "__main__":
    import os
    . . .
    # Changing current directory with the new directiory
    os.chdir("C:\\Windows")
    #It will display the current working directory
    print(os.getcwd())
