#premitive , Non premitive
#premitive integer => float , boolean , char
#Non premitive => string, array
#python
#integer , float , string, boolean
import numpy

integer =10
float = 10.45

string = "this is django course"
boolean = True
boolean_ = False
char = 'a'
arr = numpy.array([1,2,3,4,5])
print  ( integer, string, float , boolean , char)
print (type(integer), type(string), type(float), type(boolean_),type(boolean),type(char))
print(arr)

#loop => for , while
print(100/2)

for i in range(10):
    print(i+1)

for i in range(1 ,10):
    print(100/i)

for i in range(1,10,2):
    print(i)

i=0
n=10

while i<n:
    print(i)
    i+=2
