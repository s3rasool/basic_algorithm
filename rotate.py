def rotate( string , rotate_number ) :
    new_string = string + string
    if rotate_number <= len(string) :
        return new_string[rotate_number : rotate_number + len(string)]
    else :
        return new_string[rotate_number - len(string) : rotate_number]

print(rotate( 'hello' , 2 ))


# در فرآیند اسلایس کردن رشته ها باید توجه داشت که عدد دوم محاسبه نمی شود بلکه یک عدد کم تر از آن حساب می شود