def capitilize(string):
    output_string = ""
    for word in string.split():
        output_string+=f"{word.upper() if word[0].isupper() else word} "
    return output_string


text = input()
print(capitilize(text))