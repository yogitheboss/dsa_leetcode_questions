# here we have to maximize profit
weight=[2,3,4,5,2]
profit=[10,23,34,12,34]

#we would use profit per kg to add object to knapsack
ratio=[(profit[i]/weight[i],i) for i in range(len(weight))]
print(ratio)
ratio.sort(reverse=True)

max_profit=0
allowed_weight=10
i=0
while(allowed_weight>0):
    #if the item can full put inside the knapsack
    if(allowed_weight-weight[ratio[i][1]]>=0):
        max_profit+=profit[ratio[i][1]]
        allowed_weight-=weight[ratio[i][1]]
    #if only fraction of item can be added to knapsack
    else:
        max_profit+=ratio[i][0]*allowed_weight
        allowed_weight=0
    i+=1
print(max_profit)





