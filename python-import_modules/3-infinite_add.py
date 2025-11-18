#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    total = 0
    for arg in argv[1:]:  # пропускаем argv[0], имя скрипта
        total += int(arg)
    print(total)
