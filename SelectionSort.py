
def selectionSort(arr):
    length = len(arr)
    # put the correct element at ith position
    for i in range(length-1):
        minIndex = i
        #calculating the index of minimum element for this iteration
        for j in range(i+1, length):
            if(arr[j] < arr[minIndex]):
                minIndex = j
                
        arr[i],arr[minIndex] = arr[minIndex], arr[i]
    
arr = [1,3,2,4,0,6,8]
selectionSort(arr)
print(arr)
