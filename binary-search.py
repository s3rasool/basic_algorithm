def binary_search (arr , element ) :
    low = 0
    high = len(arr) - 1


    while low <= high :
        mid = (low + high ) // 2 
        valu = arr[mid]

        if valu == element :
            return mid
        elif valu < element :
            low = mid + 1 
        else :
            high = mid - 1 
    
    return -1 
print(binary_search( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 2 ))
