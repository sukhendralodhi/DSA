# import array as arr
from array import *

# val = array('i', [1, 2, 3, 4, 5,6])
# val_char = array('u', ['a', 'b', 'c', 'd', 'e', 'f'])

# for i in range(0,6):
#     print(val[i], end=" ")

# for i in range(0,len(val)):
#     print(val[i], end=" ")

# print("\n")

# for x in val:
#     print(x, end=" ")

# print(val.typecode)
# print(val_char.typecode)

# reverse array 

# val.reverse()

# for i in range(0, len(val)):
#     print(val[i])


# val.insert(1, 90) # insert any perticular index
# val.append(100) # add in last
# val[2] = 200 # override value

# for i in range(0, len(val)):
#     print(val[i], end=" ")

# copy array 


# copy_array = array(val.typecode, (x*3 for x in val))
# print(copy_array)

# for i in range(0, len(copy_array)):
#     print(i)


# for i in range(0, len(copy_array)):
#     print(copy_array[i])

# for x in copy_array:
#     print(x)

# pop() # if u know index | or want to remove last element of array
# remove() # if u dont know index only know element

# slicing 
val = array('i', [1, 2, 3, 4, 5,6,7,8,9])
# abc = val[2:5]

# for i in range(0, len(abc)):
#     print(abc[i])

# reverse array using slicing 

# abc = val[::-1]

# for i in range(0, len(abc)):
#     print(abc[i])


arr = array('i', [])

n = int(input("Enter the size of array: "))

for i in range(0,n):
    number = int(input("Enter the next number: "))
    arr.append(number)

for x in arr:
    print(x)