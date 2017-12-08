with open('input.txt') as f:
        temp = 0
        add = 0
        first = 1
        for line in f:
                for number in line:
                        if first == 1:
                                temp = int(number)
                                first = 0;
                        else:
                                if temp == int(number):
                                        add = add + int(number)
                                temp = int(number)
        print (add)