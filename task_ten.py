import math


def get_unique_chars(string): #from task six
    chars = dict()
    for c in string:
        if c not in chars:
            chars[c] = 0
        chars[c]=chars[c]+1
    unique_chars = list(filter(lambda item: item[1]==1, chars.items()))
    return unique_chars


def check_password(password):
    weights = (0.5, 0.15, 0.15, 0.2)
    min_length = 20
    length = len(password)
    unique_chars = get_unique_chars(password)
    numbers = sum(c.isdigit() for c in password)
    upper = sum(c.isupper() for c in password)
    lower = sum(c.islower() for c in password)
    symbols  = length - numbers - upper - lower
    random_values = (upper, lower, numbers)

    med = 0
    for v in random_values:
        med+=v/len(random_values)
    
    lengthiness = min(length/min_length, 1)

    randomness = 0
    for v in random_values:
        randomness = abs(med/(v+1))/len(random_values)
    uniqueness = len(unique_chars)/length
    symbolness = math.pow(symbols/length, 1)

    weighted_values = (lengthiness, randomness, uniqueness, symbolness)

    weight = 0
    for w in weights:
        weight+=w
    safety = 0
    for i, value in enumerate(weighted_values):
        safety+=(value*weights[i])

    return safety


print(check_password("password"))

print(check_password("password1234"))
print(check_password("PassWOrd???ie213!"))

print(check_password("testpasswordonetewo12323"))
