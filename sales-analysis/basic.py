#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    character = input()
    position = int(input())
    ls = []

    for index, char in enumerate(s):
        if index == position:
            ls.append(character)
            ls.append(char)
        else:
            ls.append(char)

    result = "".join(ls)
    print(result)
