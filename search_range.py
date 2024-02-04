#  در این الگوریتم یک عدد ورودی و یک لیست مرتب شده به ما داده می شود
#  رنج عدد ورودی را در لیست پیدا کرده و خروجی می دهیم
#  برای مثال می گوییم که این عدد در این لیست از کجای رشته تا کجای رشته قرار دارد

# عملیات چرخش در رشته به این صورت هست که از کم ترین میزان ایندکس عدد مورد نظر را پیدا می کند 
#  for loop range ( start , stop , step )


def search_range(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            break

    for i in range(mid, -1, -1):
        if arr[i] == target:
            start_index = i
        else:
            break

    for i in range(mid, len(arr)):
        if arr[i] == target:
            end_index = i
        else:
            break

    try:
        return [start_index, end_index]
    except NameError:
        return [None, None]

print(search_range([ 5 , 7 , 7 , 8 , 8 , 8 , 10 ] , 7))


