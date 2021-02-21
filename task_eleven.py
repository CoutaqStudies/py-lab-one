def frange(start, end, step):
    i = start
    output = list()
    while i<end:
        output.append(round(i, 14)) #maybe use decimal?
        i+=step
    return output


for x in frange(1, 5, 0.1):
    print(x)
