list1=[char for char in "hello"]
list2=[num for num in range(0,100)]
list3=[num*2 for num in range(0,100)]
list4=[num/2 for num in range(0,100)]
list5=[num for num in range(0,100) if num%2!=0]

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

my_list=['a','a','b','c','n','n','m','z']
dublicates=[x for x in my_list if my_list.count(x)>1]
print(list(set(dublicates)))