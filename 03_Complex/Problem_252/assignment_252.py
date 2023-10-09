def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
    
        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1
    return -1


if __name__=="__main__":
    arr = [2, 4, 7, 10, 15, 18, 21, 23]
    target = 15
    result = binary_search(arr, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")
