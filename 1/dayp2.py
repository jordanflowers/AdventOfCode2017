from itertools import cycle

with open('input.txt') as f:
        temp = 0
        max = 0
        index = 0
        sum = 0
        lst = []
        for line in f:
                max = len(line) - 1
                i = 0
                for number in line:
                        lst.insert(i, int(number))
                        i = i + 1
        howManySteps = (max + 1)/2   #represents how many digits to get the one to compare
        while temp <= max:
                if lst[temp] == lst[(temp+howManySteps)%2042]:
                        sum = sum + lst[temp]
                temp += 1
        print (sum)
        #for item in lst:
