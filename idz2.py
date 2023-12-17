#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Ученикам, желающим запомнить правила написания слов в английском языке, часто напоминают следующее рифмованное
#одностишие: «I before E except after C» (I перед E, если не после C). Это правило позволяет запомнить, в какой
#последовательности писать буквы I и E, идущие в слове одна за другой, а именно: буква I должна предшествовать букве E,
#если непосредственно перед ними не стоит буква C. Если стоит – порядок гласных будет обратным. Примеры слов, на которые
#действует это правило: believe, chief, fierce, friend, ceiling и receipt. Но есть и исключения из этого правила, и
#одним из них является слово weird (странный). Напишите программу, которая будет построчно обрабатывать текстовый файл.
#В каждой строке может присутствовать много слов, а может и не быть ни одного. Слова, в которых буквы E и I не
#соседствуют друг с другом, обработке подвергать не следует. Если же такое соседство присутствует, необходимо проверить,
#соответствует ли написание анализируемого слова указанному выше правилу. Создайте и выведите на экран два списка. В
#первом должны располагаться слова, следующие правилу, а во втором – нарушающие его. При этом списки не должны содержать
#повторяющиеся слова. Также отобразите на экране длину каждого списка, чтобы пользователю было понятно, сколько слов в
#файле не отвечает правилу.

if __name__ == "__main__":
    # Создаем два пустых списка для слов, следующих правилу, и нарушающих его
    words0 = []
    words1 = []

    # Открываем файл для чтения
    with open('idz2.txt', 'r') as file:
        # Читаем файл построчно
        for line in file:
            # Разбиваем строку на слова
            words = line.split()

            # Перебираем каждое слово
            for word in words:
                # Проверяем, содержит ли слово буквы E и I, и они идут друг за другом
                if 'ei' in word.lower() or 'ie' in word.lower():
                    # Проверяем, соответствует ли слово правилу
                    if 'cie' not in word.lower() and 'cei' not in word.lower():
                        words1.append(word)
                    else:
                        words0.append(word)

    # Убираем повторяющиеся слова из списков
    words0 = list(set(words0))
    words1 = list(set(words1))

    # Выводим списки и их длину на экран
    print("Слова, следующие правилу:")
    print(words0)
    print("Длина списка:", len(words0))

    print("\nСлова, нарушающие правило:")
    print(words1)
    print("Длина списка:", len(words1))
