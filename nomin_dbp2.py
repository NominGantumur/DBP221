#1
list= ['python','php','java']
for i in list:
    print(i)
    
#2
list = [3,9,1,2,4,5,7,6,10,8]
total=sum(list)
print("listiin buh toog nemeh: ", total)

#3
def product_list(list_of_numbers):
    aaa = 1
    for a in list_of_numbers:
        aaa = aaa*a
    return aaa

print(product_list([9,3,8,6,2]))

#4
def f(x):
    y= x[3] * x[-1]
    return y

x= [9,3,8,6,2]
f(x)

#5
def Maxmin(x):
    x.sort()
    a = x[0]
    b = x[-1]
    return(a,b)

x = [10,9,1,2,3]
Maxmin(x)

#6
def scount(a):
    b = 0
    for i in a:
        if len(i) > 1:
            if i[0] ==i[-1]:
                b = b+1
    print(b)
    
x = ['abdba', 'abcd', '121']
scount(x)

#7
x = ['abdba', 'abcd', '121', '121', 'abcd']
y = set(x)
x = (y)
print(x)

#8
def empty(a):
    if len(a) == 0:
        print('hooson unen baina')
    else:
        print('hooson hudal baina')
a=[0]
empty(a)

#9
n=[1,3,5,7,9,2,4,6,8,10]
n.pop(7)
n.pop(2)
n.pop(6)
print(n)

#10
n=(2,4,6,8,10)
print(n)

#11
x = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')
y = list(x)
y.append('mango')
x = tuple(y)
print(x)

#12
x = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')
y = list(x)
print(x[2])
print(x[-2])

#13
x = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')
n = input()
y=0
for i in x:
    if n == i:
        y = y + 1
if y == 0:
    print('utga baihgui')
else:
    print('Utga baina')
    
    
x = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')
n = input()
y = 0
for i in x:
    if n == i:
        y = y+1
if y == 0:
    print('none')
else:
    print('baina')
    
#14
x = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')
y = list(x)
for i in y:
    print(i)
    
#15
set_1 = {'red', 'green', 'yellow'}
set_2 = {'black', 'white', 'blue'}
Newset = set_1.union(set_2)
print(Newset)

#16
set_1 = {'red', 'blue', 'yellow','gray'}
set_2 = {'black', 'white', 'blue', 'gray'}
Newset = set_1.intersection(set_2)
print(Newset)

#17
x = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')
print(len(x))

#18
x = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')
n = input()
x.remove(n)
print(x)

#19
x = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')
x.clear()
print(x)

#20
x = {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'}
del x 
print()

#21
orders = {'milk':20, 'bread':10 , 'water':23, 'cookie':6 , 'tea':30 }
sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    print(i[0], i[1])
    
#22
dict1 = { 'restaurant': 'kfc' , 'building': '5a', 'toot':65 }
if 'building' in dict1:
    print('baina')
else:
    print('baihgu')
    
#23
dict1 = { 'restaurant': 'kfc' , 'building': '5a', 'toot':65 }

 if  in dict1.values():
     print('bainа' )
 else:
     print('baihgui')
     
#24
dict1 = { 'restaurant': 'kfc' , 'building': '5a', 'toot':65 }
for x,y in dict1.items():
    print(x,y)
    
#25
dict1 = { 'restaurant': 'kfc' , 'building': '5a', 'toot':65 }
dict2 = {
    'restaurant2': 'pizzahut',
    'building': '6a',
    'toot': 67}
dict1.update(dict2)
print(dict1)

#26
dict1 ={
        'baraa': tahia,
        'building': 5a,
        'toot': 65 }
y=0
for i in dict1:
    y= y+ dict1[i]
print(y)



    






















