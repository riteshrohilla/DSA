def binarySearch(arr, element):
    start = 0
    end = len(arr)-1
    
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid] == element):
            return mid
        elif(arr[mid] < element):
            start = mid + 1
        else:
            end = mid - 1
    return -1
    
arr = [1,3,8,9,11,13,70,89,98]
index = binarySearch(arr, 21)
print(index)
