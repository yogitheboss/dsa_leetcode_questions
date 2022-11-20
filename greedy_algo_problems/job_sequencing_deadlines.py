#Job sequencing based on deadline
profits=[20,15,10,5,1]
deadlines=[2,2,1,3,3]
total_slots=max(deadlines)

#making slots for assigning jobs
allot_array=[0]*total_slots
max_profit=0
i=0
#checking if all slots occupied or no more jobs ready to sequence
while(total_slots>0 and i<len(profits)):
    for j in reversed(range(deadlines[i])):
        #if slot empty then add the job to it and update the profit
        if(allot_array[j]==0):
            allot_array[j]=1
            max_profit+=profits[i]
            total_slots-=1
            break
    i+=1
print(max_profit)



