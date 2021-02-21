import random
from datetime import datetime, date, time

startDate = date(date.today.year, 9, 14)

def get_teams(teams, n_of_lists = 4):
    n = len(teams)-1
   
    return_teams = [[],[],[],[]]
    for i in range(n+1):
        m = random.randint(0,n-i)
        return_teams[i%n_of_lists].append(teams[m])
        del teams[m]
    return return_teams

te = ["A", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
print(get_teams(te))

