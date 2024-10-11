#Problem 1: 
clothing= ['socks', 'pants', 'shirt', 'polo']
print(clothing)
clothing.insert(-1, 'skirt')

#Problem 2: 
clothing.insert(2,['suit jacket', 'suit pants', 'tie', 'button down'])
print(clothing)

#Problem 3: 
nums= [2, 150, 14, 36, 78, 81, 14, 1000, 54, 14, 14]
print(nums.count(14))

# Problem 4:
print(sum(nums))

#Problem 5:


#Problem 6: 
one_to_five= [1, 2, 3, 4, 5]
print(one_to_five[-2:])

#Problem 7: 
animals= ["koala", "cat", "fox", "panda", "chipmunk", "sloth"]
for x in animals:
    print(x)

#Problem 8: 
random_things= ['hello', ['breakfast', 'you', 'pencil', 2], 22, ['burrito', 'taco'], [22, 'win', 33, [5], 'laptop']]

#Problem 9: 
names= ['Dre', 'Seuss', 'Who', 'McCoy']
Doctors = []
for name in names:
  Doctors.append("Dr."+name)
print(Doctors)

#Problem 10: 
num2= [10, 99, 85, 76, 43, 2, 77, 100, 13, 12, 42, 99, -1, -100]


#Problem 11:
list1= ["McDonald's", "Wendy's", "", "Burger King", "", "Taco Bell"]
new_list = []
for i in list1:
  if i:
    new_list.append(i)
print(new_list)


my_list = [1, 2, 3]
another_list = [4, 5, 6]
my_list.append(another_list)
print(my_list)  # Output: [1, 2, 3, [4, 5, 6]]

my_list = [1, 2, 3]
another_list = [4, 5, 6]
my_list.extend(another_list)
  # Output: [1, 2, 3, 4, 5, 6]
another_list.append(7)
print(my_list,another_list)