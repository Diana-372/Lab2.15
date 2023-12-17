#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Данный код удалит ранее созданный каталог new при условии, что он не пуст и находится в текущей рабочей папке.

if __name__ == "__main__":
    import os

    # removing the new directory
    os.rmdir("new")
