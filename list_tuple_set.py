#a list
l1= [1,'2',[1,2,3],{"name":"luis"},0.58, 1]

#add element
l1.append({"name":"luis"})

#a tuple, i can not change the values
t1=(1,2,3)

#a SET does not allow duplicates, it is useful to eliminate duplicated items in a list
#dictionaries dont work
s1= set([1,4,2,3,2])

l2=[3,3,3,5,6,9]
s2= set(l2)

l3=[3,3,3,5,6,"ok"]
s3= set(l3)

#bad
#l4=[{"name":"luis"},{"name":"pedro"},{"name":"pedro"}]
#s4= set(l4)

#bad
#l5= [[1,2],[1,2]]
#s5= set(l5)

print (l1)
print (t1)
print (s1)
print (s2)
print (s3)
#print (s4)
#print (s5)