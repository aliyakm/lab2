exercise_10={1, 5, 9}
def NewSet(set1):
    for x in set1:
        set1.add(x>>=1)
        set1.add(x<<=1)
    return set1
print(NewSet(exercise_10))
