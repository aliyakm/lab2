exercise_7=[5, 3, 2]
def swapPositions(list, pos1, pos2, pos3):     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    list[pos1], list[pos3] = list[pos3], list[pos1] 
    return list
pos1, pos2, pos3  = 1, 2, 3 
print(swapPositions(exercise_7, pos1-1, pos2-1, pos3-1)) 