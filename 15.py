a=[22,23,24,33,34,35]
def Funct(a):
    cnt=0
    for i in range(0, len(a)):
        if i%2!=0:
            if a[i]%2!=0:
                cnt+=1
    return cnt
print(Funct(a))