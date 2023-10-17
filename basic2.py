print(100)
print("Hello")
print('Hey there!')
print(23+100)
# This is a comment
x=3
print(x)
y = 3.3
print(y)
z = "Hello"
print(z)
print(type(x))
print(type(y))
print(type(z))
sum = x + y
print(sum)
print(id(z))
st1 = "Hello World"
st2 = "Hello"
print(len(st1))
print("Hello" in st1)
print(st1.lower())

# SLICING
print(st1[3])   # 3rd index (l)
print(st1[0:3]) # range (last index is not printed)
print(st1[:3])  # automatically starts from 0
print(st1[0:])  # automatically ends at the last index
print(st2 in st1) # true
print(st2[-1])  # (o)
print(st2[-2:]) # (lo)
# print(st2[5:2]) wrong output

# TUPLE
t1= (2,5.5,6,'a',"Hello")
print(t1) # (2, 5.5, 6, 'a', 'Hello')
print(len(t1)) # 5
print(t1[0]) # 2
print(t1[4][4])
t2 = (3,5,4,"Jecrc")
t3 = t1 + t2
print(t3)
# t1.append(20) Error because tuple is immutable

# LIST
c1 = [1,2,3.3,"Hello",7.8]
c2 = [0,"Hey",7.8]
type(c1) #list
type(c2) #list
c2.append(29) # List is mutable
print(c2) 
c2.insert(1,666) # add 666 at 1st index
print(c2)
c2.append(t2) # append a tuple to a list
print(c2)
t4 = (c1[3],t2[3])
print(t4)
print(str(c1[3]) + " " +str(t2[3])+ " " +str(c2[3]))