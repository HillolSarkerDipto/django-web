#list, tuples , set , dictonary
#index 0 - (n-1)

l=[ 1 , 2, 2 , 3 , 4.5 , 5.5 , 6.5 , "seven", "Eight","Nine"]

print(l[0])

print(type(l))
print(l)
l.append("Ten")
print(l)
l.insert(9, 12)
print((l))

print(l.index("Ten"))

print(l.count(2))
print(l.pop(9))
r = l.pop(9)
print(r)
print (l)

l= [5,3,8,5,9,7,1]
print("Before shorting",l)
l.sort()
print("After shorting",l)
l.reverse()
print(l)
l.remove(3)
print(l)
#  for i in l:
 #   print(type(i))
  #  print(i)
  #  print(l[0])


#Nested list

l=([1,2,[3.1,3.2,3.3]],[4.1,4.2,4.3],[5.1,5.2])

print(l[0][2])
print(l[0][2][2])


print ("*"*70)
#mutable , Imutable

t=(1,2,3,4,5,6,7,8,9,[10.2,10.2,10.3])
print(t)
print(t[6])
print(t.index(9))

print("*"*90)

#imutable , no indexing

s={1,2,2,2,2,7,7,7,7,9,3,4,4,4,4,4,8,5}
print(s)
s2={9,6,3,4,5}
print(s2.issubset(s))
print(s2.intersection(s))

