#Array is a container that can hold a fix number of items
#Element ~ Each item stored in an array is called an element
#Index ~ each elements in the array has a numerical index number which can
#be used for identifying element.

#Basic Operation
# Traverse, Search, Insert, Update, Delete.

from array import *


#arryName=array(typecode,[value,value])
#basic type code -i-signed integer 2bytes,c-charcter 1 byte,f-floating point 4bytes,d-floating points of 8 bytes


num_array=array('i',[10,12,14,16,18,20,22,24])

#traverse

# for x in num_array:
# 	print(x)

#accessing values by index number
#print(num_array[0])

#insertion
#num_array.insert(6,60)
#for x in num_array:
#    print(x)

#delete
#num_array.remove(24)

#search
#print(num_array.index(24))

#update
num_array[6]=28
for x in num_array:
    print(x)

