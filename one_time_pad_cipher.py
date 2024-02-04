# به هر حرف یک عدد منحصر به فرد اختصاص می دهیم
# بر روی هر عدد اختصاص داده شده به همراه یک کلید منحصر به فرد برای هر حرف یک عملیات ریاضی انجام می دهیم
#  توجه داشته باشید که کلید ها منحصر به فرد هستند
import random
class OneTime() :
    def encrypt( self , input_text ) :
       unicod_for_charachter =  [ord(ch) for ch in str(input_text)]
       key = []
       cipher = [] 

       for item in unicod_for_charachter :
           random_number = random.randint( 0 , 1000 )
           build_number = random_number + item
        #    عملیات ریاضی دلخواه در این نقطه می تواند برای رمز گذاری انجام شود
           cipher.append(build_number)
           key.append(random_number)

       return cipher , key

c , k  = OneTime().encrypt('amir')
print ( c  , '\n' , k)
       


