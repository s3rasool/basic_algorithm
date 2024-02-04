my_list = [1 , 2 , 1 , 3 , 3 , 3 , 3]
dicionary = {}
output = []


for item in my_list :
    if item in dicionary : 
        dicionary[item] = dicionary[item] + 1
    else :
        dicionary[item] = 1

max_of_repeat = max(dicionary.values())


for i in dicionary.keys() :
    if dicionary[i] == max_of_repeat :
        output.append(i)
    else :
        continue

print(output)

