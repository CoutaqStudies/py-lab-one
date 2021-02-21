def get_unique_chars(string):
    chars = dict()
    for c in string:
        if c not in chars:
            chars[c] = 0
        chars[c]=chars[c]+1
    unique_chars = list(filter(lambda item: item[1]==1, chars.items()))
    return unique_chars


print(get_unique_chars("lsdjfhksdjgfksb.  ddddasdasd w,,, asdasd ,"))
