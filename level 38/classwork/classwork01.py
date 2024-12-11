def check_exam(arr1,arr2):
    point = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            point += 4
        elif arr2[i] == "":
            continue
        else:
            point -= 1
    if point < 0:
        return 0
    return point
