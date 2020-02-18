a={1, 2, 3, 2, 4}
def NewSet(a):
    n=1
    for x in a:
        if x in a:
            x=x**n
            n+=1
    return a
print(NewSet(a))
