def hide_card(number):
    if len(number) != 16:
         raise ValueError('Некорректный формат!')
    out =  number[:4] + '*'*(8) + number[-4:]
    return out

print(hide_card("5123567891231212"))