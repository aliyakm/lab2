a=[11,2,44,23]
n=int(input())
def Funct(a, n):
    for x in a:
        if x<=n:
            a.remove(x)
    return a
print(Funct(a, n))