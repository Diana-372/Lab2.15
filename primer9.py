#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Приведенный выше код переименует файл file2.txt в file3.txt в текущей рабочей папке.

if __name__ == "__main__":
    import os

    # rename file2.txt to file3.txt
    os.rename("file2.txt", "file3.txt")
