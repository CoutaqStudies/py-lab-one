def extra_enumerate(enumeratable):
    length = len(enumeratable)
    output = []
    sum = 0
    for item in enumeratable:
        sum+=item
    cum = 0
    for i in range(length):
        cum+=enumeratable[i]
        new_list = [i, enumeratable[i], cum, cum/sum]
        output.append(new_list)
    return output

x = [1,3,4,2]
for i,elem,cum,frac in extra_enumerate(x):
    print(f"({elem}, {cum}, {frac})")