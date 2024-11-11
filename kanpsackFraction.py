def fractionalKnapsack(values ,weights,capacity):
    ratios = [(values[i] / weights[i] , i) for i in range(len(values))]
    ratios.sort(key=lambda x:x[0],reverse =True)

    totalValue =0 
    for ratio , indx in ratios:
        if capacity >= weights[indx]:
            totalValue += values[indx]
            capacity -= weights[indx]
        
        else:
            totalValue += values[indx] * (capacity / weights[indx])

    return totalValue







values =[60,100,120]
weights =[10,20,30]
capacity = 50

maxValue = fractionalKnapsack(values ,weights , capacity)

print(maxValue)