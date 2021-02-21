def split_string(string):
    list1 = ""
    list2 = ""
    list3 = ""
    for word in string.split(' '):
        if len(word)>=7: 
            list1+=f'{word} '
        elif len(word)>=4: 
            list2+=f'{word} '
        else: 
            list3+=f'{word} '
    return f'{list1}{list2}{list3}'
print(split_string("tetttttt tetwsfsdf tsdfsdgdfhg qweqweqweqw trtrtr rwwww wwwww wwewqe dasd ss sss"))