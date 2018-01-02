import linecache
from random import randint

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_word(fname):
    h = linecache.getline(fname, (randint(1, file_len(fname))))
    return h

a = get_word("First.txt").rstrip()
b = get_word("Second.txt").rstrip()
print (a, b)
