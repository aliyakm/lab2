exercise_3=[10, 3, 4, 5, 9]
n=int(input())
for i in range (0, len(exercise_3)):
    if i>=n:
        exercise_3[i]=(exercise_3[i])**2
print(exercise_3)