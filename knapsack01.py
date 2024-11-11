def fractional(values,weights,capaciy):
    n = len(values)
    ratio = [(values[i] /weights[i] , i ) for i in range(n)]
    ratio.sort(key=lambda x:x[0] , reverse= True)


    sortedValues = [values[ratio[i][1]] for i in range(n)]
    sortedWeights = [weights[ratio[i][1]]for i in range(n)]

    bestValue = 0
    currentValue = 0
    currentWeight = 0

    stack = []
    stack.append((0 , currentValue , currentWeight ))

    while stack:
        indx , value , weight = stack.pop()

        if indx >= n or weight > capacity:
            continue

        bestValue = max(bestValue , value)

        if weight + sortedWeights[indx] <= capacity:
            stack.append((indx+1 , value + sortedValues[indx] , weight + sortedWeights[indx]))

        stack.append((indx+1 , value , weight ))

    return bestValue
values =[60,100,120]
weights = [10,20,30]
capacity = 50


maxValue = fractional(values,weights,capacity)

print(maxValue)