with open('input.txt') as f:
        lst = []
        for line in f:
                lst.append(line.split())
        i = 0
        sum = 0
        for item in lst:
                min = 0
                max = 0
                temp = 0
                
                firstIteration = 1
                for number in item:
                        temp = 0
                        if firstIteration == 1:
                                min = int(number)
                                max = int(number)
                                firstIteration = 0
                        else:
                                #just get the min for now
                                if int(number) < min:
                                        min = int(number)
                                if int(number) > max:
                                        max = int(number)
                print("max: ", max, "min: ", min)
                print("temp is now equal to ", max-min)
                temp = max - min
                sum = sum + temp
                
        print(sum)
