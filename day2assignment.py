#LIST AND ITS DEFAULT FUNCTIONS
lst = [11.2,"priyanka","shirsat",1452,[1,2,3,4]]
lst.append("akola")
print("updated list is : ",lst)
b = lst.index(1452)
print("index of:",b)
c = lst[-1]
print("reverse : ",c)
lst.extend([5,7])
print("extend list is : ",lst)
lst.pop(5)
print("after pop list is : ",lst)
print("***********************************************************************************************")
#DICTIONARY AND ITS DEFAULT FUNCTIONS
dit = {"name":"priyanka shirsat","age":"24","email":"shirsat121996@gmail.com","mobile no":"8208143991"}
print(dit)
j = dit.get("name")
print("get function is : ",j)
k = dit.items()
print("items are : ",k)
l = dit.setdefault("colour","white")
print("setdefault fun is : ",l)
dit.pop("mobile no")
print(dit)
dit.clear()
print(dit)

print("******************************************************************************************************")
#SETS AND ITS DEFAULT FUNCTIONS

st = set(("piu","instagram","telegram","facebook","whatsapp"))
print(st)
st.add("twitter")
print("set after adding twitter : ", st)
st1 = {"google","microsoft","apple","piu"}
y = st.union(st1)
print("union of sets is : ",y)
z = st.intersection(st1)
print("intersection is : ",z)
q = {"a","b","c"}
r = {"f","g","h","c","b","a"}
t = q.issubset(r)
print("issubset : ",t)
s = st1.pop()
print("after pop set is : ",s)


print("**************************************************************************************************")

#TUPLE AND EXPLORE DEFAULT METHODS
tup = ("apple","cherry","banana","cherry","pinapple","orange")
print("tuple is : ",tup)
a = tup.count("cherry")
print("count of tuple is :  ",a)
b = tup.index("pinapple")
print("index of pinapple is : ",b)
tuple = ("fruits", [8, 4, 6], (1, 2, 3))
print("nested tuple indexing is : ")
print(tuple[0][2])
print(tuple[1][1])
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print("negative indexing of tuples are : ")
print(my_tuple[-1])
print(my_tuple[-6])
my_tuple = my_tuple + (20,)
print("append tuple is : ",my_tuple)

print("**************************************************************************************************")
#STRINGS AND EXPLORE DEFAULT METHODS
str = 'letsupgrade is on instagram,letsupgrade is in pune,letsupgrade is doing very good job'
print("string is : ",str)
a = str.count("letsupgrade")
print("count of string is : ",a)
b = str.index("on")
print("index of string on  is : ",b)
c = str.capitalize()
print("capitalization of string is : ", c)
d =  "My name is {}, I'am {}".format("vedika",30)
print("format of string is : ",d)
e = str.find("x")
print("after find function of string is : ",e)

print("**************************************************************************************************")



""""
########## OUTPUT ############
updated list is :  [11.2, 'priyanka', 'shirsat', 1452, [1, 2, 3, 4], 'akola']
index of: 3
reverse :  akola
extend list is :  [11.2, 'priyanka', 'shirsat', 1452, [1, 2, 3, 4], 'akola', 5, 7]
after pop list is :  [11.2, 'priyanka', 'shirsat', 1452, [1, 2, 3, 4], 5, 7]
***********************************************************************************************
{'name': 'priyanka shirsat', 'age': '24', 'email': 'shirsat121996@gmail.com', 'mobile no': '8208143991'}
get function is :  priyanka shirsat
items are :  dict_items([('name', 'priyanka shirsat'), ('age', '24'), ('email', 'shirsat121996@gmail.com'), ('mobile no', '8208143991')])
setdefault fun is :  white
{'name': 'priyanka shirsat', 'age': '24', 'email': 'shirsat121996@gmail.com', 'colour': 'white'}
{}
******************************************************************************************************
{'whatsapp', 'instagram', 'piu', 'telegram', 'facebook'}
set after adding twitter :  {'whatsapp', 'instagram', 'piu', 'telegram', 'facebook', 'twitter'}
union of sets is :  {'whatsapp', 'instagram', 'microsoft', 'piu', 'telegram', 'facebook', 'twitter', 'apple', 'google'}
intersection is :  {'piu'}
issubset :  True
after pop set is :  apple
**************************************************************************************************
tuple is :  ('apple', 'cherry', 'banana', 'cherry', 'pinapple', 'orange')
count of tuple is :   2
index of pinapple is :  4
nested tuple indexing is : 
u
4
negative indexing of tuples are : 
t
p
append tuple is :  ('p', 'e', 'r', 'm', 'i', 't', 20)
**************************************************************************************************
string is :  letsupgrade is on instagram,letsupgrade is in pune,letsupgrade is doing very good job
count of string is :  3
index of string on  is :  15
capitalization of string is :  Letsupgrade is on instagram,letsupgrade is in pune,letsupgrade is doing very good job
format of string is :  My name is vedika, I'am 30
after find function of string is : -1

"""



