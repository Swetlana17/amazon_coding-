def find_missing(input):
 input.sort()
 ctr=1
 for i in input:
     if(i!=ctr):
        return ctr
     ctr+=1
 return -1

print(find_missing([6,3,4,2,5]));