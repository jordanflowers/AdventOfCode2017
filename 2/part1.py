with open('input.txt') as f:
        min = 0
        max = 0
        firstIteration = 1
        for line in f:
                firstIteration = 1
                for number in line:
                        print(number)
                        #if firstIteration == 1:
                        #        min = int(number)
                        #        max = int(number)
                        #        firstIteration = 0
                        #else:
                        #        if min > int(number):
                        #                min = int(number)
                        #        elif max < int(number):
                        #                max = int(number)
                #print ("max: %d min: %d") % (max, min)