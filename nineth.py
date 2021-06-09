# How many ways can you make change with coins and a total amount


def coin(n,arr):
    if n==0 or n==1: 
        return 1
    if n==2
        return 2
    sum=0
    for(i in arr):
        if(n-i)>=0:
            sum+=coin(n-i,arr)
    return sum
    


print(coin(5))