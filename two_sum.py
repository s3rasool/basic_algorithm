#  [2 , 7 , 11 , 15 ] , 9 == [ 1 , 2  ] جمع اولین عدد و دومین عدد از لیست برابر با مقدار خواسته شده است
# two sum algorithm

def two_sum (input_list , target_number ) :
    p1 = 0
    p2 = len(input_list) - 1 

    while p1 < p2 :
        summ =  input_list[p1] + input_list[p2]
        if summ == target_number :
            return [ p1 + 1 , p2 + 1]
        elif summ > target_number :
            p2 = p2 - 1
        else :
            p1 = p1 + 2 

print(two_sum([2 , 7 , 11 , 15 ] , 9))