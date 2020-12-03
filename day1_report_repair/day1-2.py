import math

def sum_of_three(filename, sum_number):

    firstdiff = dict()

    with open(filename, 'r') as file:
        listfile = file.read().splitlines()

    for index, i in enumerate(listfile):
        for j in listfile[index+1:-1]:
            i_int = int(i)
            j_int = int(j)
            difference = sum_number - (i_int + j_int)
            if difference <= 0:
                continue
            firstdiff[difference] = [i_int, j_int]
    
    for k in listfile:
        kint = int(k)
        if kint in firstdiff.keys():
            firstdiff[kint].append(kint)
            return math.prod(firstdiff[kint])

    

print(sum_of_three('data.txt', 2020))

