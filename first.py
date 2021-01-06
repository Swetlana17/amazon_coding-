# Find the missing number in the array

def find_missing(arr):
 arr.sort()
 ctr=1
 for i in arr:
     if(i!=ctr):
        return ctr
     ctr+=1
 return -1

print(find_missing([6,3,4,2,5]))