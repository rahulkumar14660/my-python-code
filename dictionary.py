d = {'a':10,'b':20,'c':30,'d':'upflairs','e':[34,56.7],'f':(43,5,76),'g':{45,65,67.8,46,76.86,65}}
print(type(d))
print(d,'\n') #\n is the new line character

d1 = {'a':67,'b':76,'c':43,'d':67,'e':78}
print(d1['a'])
print(d1.keys())
print(d1.values())
d1['a'] = 34
print(d1['a'])
print(d1.keys())
print(d1.values())
d1.pop('b')
print(d1)
#print(d1*2) or print(d1+2) -> not allowed in dictionary

d2 = {'a':7,'b':4,'c':3,'d':87,'e':56}
e = {'f':786,'g':'Rahul'}
d2.update(e)
print(d2)
#print(d2['ab'])
print(d2.get('ab','Not Found!'))
print(d2)