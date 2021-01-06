# Reverse Words in a Sentence

def reverseString(s):
    arr=[]
    w=""
    t=' '
    s=s+" "
    for i in s:
        if i==' ':
            arr.append(w)
            w=""
        else:
            w=w+i
    arr.reverse()
    t= t.join(arr)
    return t

print(reverseString("Hello World!"))