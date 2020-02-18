exercise_6=[10, 3, 4, 5, 9]
a=int(input())
b=int(input())
def Function(exercise_6, a, b):
    for i in range(0, len(exercise_6)):
        if i==a:
            exercise_6.insert(i, 1)
            exercise_6.insert(i+1, 2)
            exercise_6.insert(i+2, 3)
        for i in range(0, len(exercise_6)):
            if i>=b:
                exercise_6.pop()
    return exercise_6
print(Function(exercise_6, a, b))