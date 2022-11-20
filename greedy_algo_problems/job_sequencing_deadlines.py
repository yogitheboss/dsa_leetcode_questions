#Job sequencing based on deadline
profits=[35,30,25,20,15,12,5]
deadlines=[3,4,4,2,3,1,2]
total_slots=max(deadlines)

#making slots for assigning jobs
allot_array=[0]*total_slots

max_profit=0
for i in range(total_slots):
    for j in reversed(range(deadlines[i])):
        #if slot empty then add the job to it and update the profit
        if(allot_array[j]==0):
            allot_array[j]=1
            max_profit+=profits[i]
            break
print(max_profit)



