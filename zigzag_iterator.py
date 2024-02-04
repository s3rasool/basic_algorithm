class zigzag :
    def __init__(self , L1 , L2 ) :
        self.queue = [L1 , L2 ]

    
    def Function (self) :
        first = self.queue.pop[0]
        First_object = first.pop[0]
# شرط پایین به این معنی است که تا زمانی که لیست مورد نظر مقدار داشته باشد این عملیات انجام شود
        if first :
            self.queue.append(first)
        return First_object
    def has_next (self) :
        if self.queue :
            return True
        return False

output = zigzag([1 , 3 , 5 ] , [2 , 4 , 6 ])

