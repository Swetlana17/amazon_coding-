# String segmentation
# You are given a dictionary of words and a large input string. 
# You have to find out whether the input string can be completely segmented into the words of a given dictionary.


def stringSegmentation(st,arr):
    dic={}
    w=""
    for i in arr:
        dic[i]=0

    # print(dic)
    for i in st:
        w=w+i
        if w in dic.keys():
            # print(w)
            w=""

    if w=="" :
        return True
    else:
        return False

print(stringSegmentation("applepie",["apple","pie","pear"]))