

# create list of alpha chars
def create_alphabet():
    alpha_chars = []
    n = 97
    for i in range(26):
        alpha_chars.append(chr(n))
        n += 1
    return alpha_chars


# convert list of alpha chars to unicode ints
def convert_alpha_to_unicode(alpha_chars):
    unicode_ints = []
    for c in alpha_chars:
        unicode_ints.append(ord(c))
    return unicode_ints
