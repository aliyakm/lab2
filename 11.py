a={1, 2, 3, 4}
b={3, 5, 7}
def Diff(set1, set2):
    c=a.difference(b)
    return c
print(Diff(a, b))