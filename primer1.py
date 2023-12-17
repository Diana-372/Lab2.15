#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#файл file2.txt не существует, необходимо создать программу которая будет создавать новый файл и записывать его
#содержимое с помощью функции write() .

if __name__ == "__main__":
    # open the file2.txt in append mode. Create a new file if no such file exists.
    fileptr = open("file2.txt", "a")

    # appending the content to the file
    fileptr.write(
        "Python is the modern day language. It makes things so simple.\n"
        "It is the fastest-growing programing language"
)

    # closing the opened the file
    fileptr.close()
