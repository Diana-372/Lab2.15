#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#необходимо открыть файл в режиме и добавить содержимое в существующий файл file2.txt.

if __name__ == "__main__":
    # open the file2.txt in write mode.
    with open("file2.txt", "a") as fileptr:
        # overwriting the content of the file
        fileptr.write(" Python has an easy syntax and user-friendly interaction.")
