import random

bills = [5000, 2000, 1000, 500, 200, 100, 50, 10]
bank = { i : random.randint(3, 10) for i in bills }
print(f"current bank account: {bank}")

def withdraw(amount):
    output =  dict.fromkeys(bills , 0)
    for value, n in bank.items():
        if n>0 and value<=amount:
            n_of_bills = min(int((amount/value)), n)
            output[value]=n_of_bills
            amount-=value*n_of_bills
            n-=n_of_bills
            bank[value]-=n_of_bills
    if amount is not 0: 
        print("Операция не может быть выполнена!")
        for value, n in output.items():
            bank[value]+=n
    else:
        output = dict(filter(lambda elem: elem[1] > 0, output.items()))
        print(f"withdrawing: {' + '.join(['%s*%s' % (key, value) for (key, value) in output.items()])}")



withdraw(5370)
print(f"current bank account: {bank}")