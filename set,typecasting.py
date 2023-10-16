#Set{} in Python 
set1 = {20,'Single',3.5,'c'}
print(set1) #Unordered
print(type(set1))
#print(set1[0]) #Error because it is unoredered so accessing cannot be done
#set1[2] = 65 #Error because it is unchangeable

print(set1) 

set2 = {43,'Bharat',65.37,'b',True,(4,3,64,4,8)}
#set2 = {43,'Bharat',65.37,'b',True,(4,3,64,4,8),{5,3,7,9,10}} #Error because set is not allowed inside a set
print(set2)

set3 = {4,4,4,44,4,4,4,5,5,55,5,66,6,7,8,7,7,77,6}
print(set3)

#Typecasting
a = 25
# int(),float(),strt()
print(int(a))
print(float(a))
print(str(a))
print(type(str(a)))

lst = [2,5,4,8,6,4,8,1,2,4,2,5,3,2]
print(lst)
print(set(lst))

set4 = {3,5,4,6,8,65,45}
print(set4)
set4.add(677)
print(set4)
set4.remove(8)
#set4.discard(877) will shpw the error because the element is not present in this set
print(set4)
set4.discard(4)
#set4.discard(56) will not show error even when the element is not present
print(set4)

set5 = {4,5,6,7,'d','r'}
set6 = {3,5,3,6}
set5.update(set6)
print(set5)