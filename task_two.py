def is_ordered(list):
    temp = list[0]
    for item in list:
        if(item<temp):
            return False
        temp = item
    return True


list1 = (1, 2, 4, 5, 12, 21)

print(is_ordered(list1))        