# Program compares List and Tuple

import sys
import timeit

mylist=[23,56,34,89,53,11]
mytuple=(54,77,12,65,86,64)

print("length of list:%d"%len(mylist))
print("length of tuple:%d"%len(mytuple))



print(dir(mylist))
print(20*"-")
print(dir(mytuple))


print(20*"-")
print("List size ",sys.getsizeof(mylist))
print("Tuple size ",sys.getsizeof(mytuple))

# we can add,remove,change data in list
# data cant be changed in tuples
# tuples are fast and consume less memory

biglist=timeit.timeit(stmt="[1,2,3,4,5]",number=1000000)
bigtuple=timeit.timeit(stmt="(1,2,3,4,5)",number=1000000)

print("List time ",biglist)
print("Tuple time ",bigtuple)


#content of sohamglobal.com