tpl = (34,) #For single element also comma is necessary to be in tuple type else it will be int type.
print(tpl)
print(type(tpl))

name = 'Rahul','Single'
print(name)
print(type(tuple))

tpl2 = (2,4,5,4,64,(4,5),[6,8],'upflairs',756.4,True)
print(tpl2)
print(tpl2[-1::-1])
print(tpl2 * 2)

tpl3 = (2,5,4,7,8,9,[2,5,4,7,8,9,10])
#tpl3[-1][-1] = 'Upflairs'
print(tpl3[-1][-1])

tpl4 = (2,54,233,65,54,9,[2,32,6,486,3,5,9,10])
tpl4[-1][-1] = 'Upflairs'
print(tpl4[-1][-1][-1])
# print(min(tpl4))
# print(max(tpl4))
# print(sum(tpl4))
tpl5 = ('upflairs','jaipur','rajasthan')
a,b,c = tpl5
print(tpl5)
print(a)
print(b)
print(c)
print(tpl5.count('upflairs'))
print(tpl5.index('rajasthan'))