with open('input.txt') as f:
        lst = []
        for line in f:
                lst.append(line.split())
        i = 0
        sum = 0
        temp = 0
        divisiblenum1 = 0
        divisiblenum2 = 0
        for item in lst:
                i = 0
                for number in item:
                        i = 0
                        while i < len(item):
                                if (int(number) != int(item[i])) and (int(number) % int(item[i]) == 0):
                                        divisiblenum1 = int(number)
                                        divisiblenum2 = int(item[i])
                                i += 1
                temp = divisiblenum1/divisiblenum2
                print(divisiblenum1, " and ", divisiblenum2, " ", temp)
                
                sum = sum + temp
                divisiblenum1 = 0
                divisiblenum2 = 0
        print(sum)
