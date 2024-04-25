def find_biggest(arr):
    biggest = arr[0]
    biggest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
    return biggest_index

print(find_biggest([9,13,3,83,12,32]))
