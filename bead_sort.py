#  this algorithm just work for int and posetive number
#  [4 , 7 , 9 , 2 , 3 , 6 , 7]
#  [7 , 9 , 2 , 3 , 6 , 7]
#  در واقع متد زیپ یک شی تکرار شونده را پیمایش می کند و یک به یک کنار هم قرار می دهد

def bead_sort(arr) :
    if any ( item < 0  or not isinstance (item , int ) for item in arr) :
        raise TypeError ('your input is not vali for my program.')  
    
    for _ in range(len(arr)) :
        for i , (upper , lower ) in enumerate(zip(arr , arr[1:])) :
            if upper > lower :
                arr[i] -= upper - lower
                arr[i+1] += upper - lower
    return arr

print(bead_sort([4 , 7 , 9 , 2 , 3 , 6 , 7]))