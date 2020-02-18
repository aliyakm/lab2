exercise_5=[10, 3, 4, 5, 9]
n=int(input())
a=len(exercise_5)
def DeleteIt(exercise_5, n):
    for i in range(0, a):
        if i>=n:
            exercise_5.pop()
    return exercise_5
print(DeleteIt(exercise_5, n))