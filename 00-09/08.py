def cipher(s):
    return ''.join((map(lambda c: chr(219-ord(c)) if 97 <= ord(c) <= 122 else c, s)))

print(cipher('Anyone who has never made a mistake has never tried anything new.'))
