tuple1=(5, 2.5, 8, 4, 'Hi', -5, True, 6)
def IsTrue(tuple1):
    boo=False
    for x in range(0, len(tuple1)):
        while type(tuple1[x]) is list:
            boo=True
            return boo
    return boo
print(IsTrue(tuple1))
