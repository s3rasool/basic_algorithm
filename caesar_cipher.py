from string import ascii_letters

def encrypt (string, key ) :
    result = ''
    alpha = ascii_letters 

    for ch in string : 
        if ch not in alpha :
            result = result + ch
        else :
            new_key =(alpha.index(ch)  + key ) %  len(alpha)
            result += alpha[new_key]        
    return result

print(encrypt('rasool' , 4))


# برای رمز گشایی از این الگوریتم فقط کافی است که مقدار شیفت را منفی در نظر بگیریم