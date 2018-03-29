import re

def flip(x):
    out = ""
    x = x.lower()
    x = x[::-1]
    words = x.split()
    for word in words:
        word = re.sub("[^a-zA-Z]+", "", word)
        for c in word:
            out = out + flip_char(c)
        out = out + " "
    return out

def flip_char(c):
    if c == 'a':
        return 'ɐ'
    if c == 'b':
        return 'q'
    if c == 'c':
        return 'ɔ'
    if c == 'd':
        return 'p'
    if c == 'e':
        return 'ǝ'
    if c == 'f':
        return 'ɟ'
    if c == 'g':
        return 'b'
    if c == 'h':
        return 'ɥ'
    if c == 'i':
        return 'ı'
    if c == 'j':
        return 'ɾ'
    if c == 'k':
        return 'ʞ'
    if c == 'l':
        return 'ן'
    if c == 'm':
        return 'ɯ'
    if c == 'n':
        return 'u'
    if c == 'o':
        return 'o'
    if c == 'p':
        return 'd'
    if c == 'q':
        return 'b'
    if c == 'r':
        return 'ɹ'
    if c == 's':
        return 's'
    if c == 't':
        return 'ʇ'
    if c == 'u':
        return 'n'
    if c == 'v':
        return 'ʌ'
    if c == 'w':
        return 'ʍ'
    if c == 'x':
        return 'x'
    if c == 'y':
        return 'ʎ'
    if c == 'z':
        return 'z'
    else:
        return ' '
    
        
