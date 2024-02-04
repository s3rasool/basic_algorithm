# input array must be sorted
#  [1 , 3 , 5 , 6 ]
#  آرایه را نصف می کنیم و به سمت راست یا چپ حرکت خواهیم کرد و در نهایت لو را باز می گردانیم

def serch_insert(arry , val ) :
    low = 0 
    high = len(arry) - 1 
    mid = high // 2

    while low <= high :
        if val >= arry[mid] :
            mid += 1
            low = mid
        else :
            mid = mid - 1
            high = mid
    return low

print(serch_insert([1 , 3 , 5 , 6 ] , 4))