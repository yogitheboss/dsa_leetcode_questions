from collections import defaultdict

def maxPoints(points) -> int:

        # default value(if single point given)
        result=1

        for i in range(len(points)):
            # default dict to store count of points with same slopes

            d=defaultdict(int)
            for j in range(i+1,len(points)):
                # if slope is infinity 
                if(points[i][0]-points[j][0]==0):
                    d["inf"]+=1

                # increase count of slope
                else:
                    d[(points[j][1]-points[i][1])/(points[j][0]-points[i][0])]+=1

            if(d.values()):
                # max count +1 stored as number of points
                result=max(result,max(d.values())+1)
            print(d)
        return result

points=[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

print(maxPoints(points))
