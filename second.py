# Determine if the sum of two integers is equal to the given value

# 1  7 |  1+6 === 7
# 2  6 |  5+2 === 7
# 3  5 |


def sum_of_two(arr,val):
    dic={}
    for i in arr:
        if i not in dic.keys():
            dic[i]=0
        dic[i]+=1;

    for i in arr:
        if (val-i) in dic.keys():
            if ((i) == (val-i) and dic[val-i] <= 1):
                continue
            else:
                return True

    return False

print(sum_of_two([1,2,7,6,5,3,6,6],10))