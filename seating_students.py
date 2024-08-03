def SeatingStudents(arr):
    K = arr[0]
    occupied = set(arr[1:])
    rows = K // 2
    seating = 0

    for i in range(rows):
        if (2 * i + 1) not in occupied and (2 * i + 2) not in occupied:
            seating += 1

    for i in range(rows - 1):
        if (2 * i + 1) not in occupied and (2 * (i + 1) + 1) not in occupied:
            seating += 1
        if (2 * i + 2) not in occupied and (2 * (i + 1) + 2) not in occupied:
            seating += 1

    return seating

print(SeatingStudents(input()))