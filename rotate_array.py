arr = [1, 2, 3, 4, 5, 6, 7]

# ROTATE ARRAY — DYNAMIC ARRAY
def left_rotate(arr, n):
    return arr[n:] + arr[:n]
    
# ROTATE ARRAY — STATIC ARRAY   
def left_rotate_static(arr, rotations, arr_size):
    for i in range(rotations):
        temp = arr[0]
        for i in range(arr_size-1):
            arr[i] = arr[i+1]
        arr[arr_size-1] = temp
    return arr
    
print(left_rotate(arr, 2))
print(left_rotate_static(arr, 2, 7))