# region COMMON
# print('''asd 'asdasd' asd''')
# print('''This is first string
# This is second string''')   # можно писать внутри тройных кавычек кавычки
# print('asjdh' 'asdasda')    # объединение строковых констант
#
#
# # # method 'format'
# age = 26
# name = 'Swaroop'
#
# print('age {} -- {} old.' .format(name, age))
# print('Why is {} having fun with this Python?' .format(name))
# # # плюсы: 1. читаемость кода 2. авт. преобразование в строку
# # # 3. изменение сообщения не затрагивая сообщения и наоборот
# n = 20
# m = 25
# prod = n * m
# print(f'product of {n} by {m} equal {prod}')
#
# # # десятичное число (.) с точностью до 3 знака для плавающих?:
# print('{0:.3}' .format(1/3))
#
# # # заполнить подчеркиваниями (_) с центровкой текста (^) по ширине 11:
# print('{0:_^11}' .format('hello'))
#
# # # по ключевым словам:
# print('{name} write {book}' .format(name='Swaroop', book='A Byte Of Python'))
#
# print(2 << 2)     # сдвиг по битам 10 => 1000 (10 = 2, 1000 = 8)
# # анологично >>
#
# # побитовык операции: &(побитовое и), |(побитовое или),
# # ^(побитовое исключительно или), ~(побитовое не).
# endregion

# region CYCLES
# for i in range(1, 5):
# 	print(i)
# else:
# 	print('for series is over')

# while True:
# 	s = input("Enter something: ")
# 	if s == 'close':
# 		break
# 	if len(s) < 3:
# 		print("too little")
# 		continue
# 	print("output string of sufficient lenght")
# endregion

# region LOCAL VARIABLE
# __we are copying x
# x = 50
# # x = [1, 2, 3]
#
#
# def func(x):
# 	print('x is equal to', x)
# 	x = 2
# 	# x[0] = 2
# 	print('replacing local x to', x)
#
#
# func(x)
# print("x stil", x)
# endregion

# region GLOBAL VARIABLE
# __we are not copying x
# x = 50
#
#
# def func():
# 	global x
#
# 	print('x is equal to', x)
# 	x = 2
# 	print('replacing local x with', x)
#
#
# func()
# print("x already", x)

# if __name__ == "__main__":    # point enter
	# x = 50
	# func(x)
# read functional prog
# endregion

# region NONLOCAL VARIABLE
# def func_outer():
# 	x = 2
# 	print('x is equal to', x)
#
# 	def func_inner():
# 		nonlocal x
# 		# global x
# 		x = 5
#
# 	func_inner()
# 	print('local x has changed to', x)
#
#
# func_outer()
# print(x)
# endregion

# region DEFAULT VALUE OF ARGUMENTS
# def say(message, times=1):
# 	print(message * times)
#
#
# say('hello')
# say('hi', 5)
# endregion

# region KEY PARAMETERS
# def func(a, b=5, c=10):
# 	print("a =", a, "b =", b, "c =", c)
#
#
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)
# endregion

# region VARIABLE NUMBER OF PARAMETERS
# def total(initial=5, *numbers, **keywords):
# 	count = initial
# 	for number in numbers:
# 		print(count)
# 		count += number
# 		print(count)
# 	for key in keywords:
# 		print(count)
# 		count += keywords[key]
# 		print(count)
# 	return count
#
#
# print(total(10, 1, 2, 3, vegetables=50, fruits=100))


# def total(initial=5, *numbers, extra_number):
# 	count = initial
# 	for number in numbers:
# 		count += number
# 	count += extra_number
# 	print(count)
#
#
# total(10, 1, 2, 3, extra_number=50)
# total(10, 1, 2, 3)  # will cause an error
# endregion

# region OPERATOR RETURN
# def maximum(x, y):
# 	if x > y:
# 		return x
# 	elif x == y:
# 		return 'numbers is equal'
# 	else:
# 		return y
#
#
# print(maximum(2, 3))
# # return без возвращающего значения ~ return None
#
#
# def some_function():
# 	pass
#
#
# print(some_function())
# # каждая функция содержит в неявной форме return None в конце
# endregion

# region DOCUMENTATION STRINGS
# def print_max(x, y):
# 	"""Print maximum of 2 numbers.\n\nBoth values must be integers."""
# 	x = int(x)
# 	y = int(y)
#
# 	if x > y:
# 		print(x, "is max")
# 	elif x == y:
# 		print('x equal y')
# 	else:
# 		print(y, "is max")
#
#
# print_max(3, 5)
# print(print_max.__doc__)
# endregion

# region MODULES

# import sys
#
# print('command string arguments:')
# for i in sys.argv:
# 	print(i)
#
# print('\n\nPYTHONPATH variable contains', sys.path, '\n')

# from math import *
# n = int(input('enter range: '))
# p = [2, 3]
# count = 2
# a = 5
# while count < n:
# 	b = 0
# 	for i in range(2, a):
# 		if i <= sqrt(a):
# 			if a % i == 0:
# 				print('a neprost', a)
# 				b = 1
# 			else:
# 				pass
#
# 	if b != 1:
# 		print('a prost', a)
# 		p = p + [a]
# 	count = count + 1
# 	a = a + 2
# print(p)

# if __name__ == '__main__':
# 	print('this programm is running on its own')
# else:
# 	print('I was imported into another module')

# import sys
#
# print(dir(sys))
# print(dir())
# a = 4
# print(dir())
# del a
# print(dir())
# print(dir(print()))
# print(dir(str))
# # using the dir() function, we get a list of identifiers that the object defines

# # package
# | - <some directory from sys.path>/
# | |---- world/
# |       |---- __init__.py
# |       |---- asia/
# |       |    |---- __init__.py
# |       |    |---- india/
# |       |         |---- __init__.py
# |       |         |---- foo.py
# |       |---- africa/
# |            |---- __init__.py
# |            |---- madagaskar/
# |                   |---- __init__.py
# |                   |---- bar.py
# endregion

# region DATA STRUCTURES (LIST)
# shop_list = ['apple', 'mango', 'carrot', 'bananas']
#
# print('i have to make', len(shop_list), 'purchases')
#
# print('purchases:', end=' ')
# for item in shop_list:
# 	print(item, end=', ')
#
# print('\nAlso need to buy rice.')
# shop_list.append('rice')
# print('my shopping list is now', shop_list)
#
# print('I will sort my list')
# shop_list.sort()
# print('sorted shopping list looks like this:', shop_list)
#
# print('the first thing i need to buy is', shop_list[0])
# olditem = shop_list[0]
# del shop_list[0]
# print('i bought', olditem)
# print('now my shopping list:',shop_list)

# endregion

# region SEQUENCE
# shop_list = ['apple', 'mango', 'carrot', 'bananas']
# name = 'swaroop'
# print(shop_list)
#
# # indexing operation
# print('Element 0 -', shop_list[0])
# print('Element 1 -', shop_list[1])
# print('Element 2 -', shop_list[2])
# print('Element 3 -', shop_list[3])
# print('Element -1 -', shop_list[-1])
# print('Element -2 -', shop_list[-2])
# print('Symbol 0 -', name[0])
# # attribution of an index
#
# # list clipping
# print('Elements with 1 to 3:', shop_list[1:3])
# print('Elements with 2 to the end:', shop_list[2:])
# print('Elements with 1 to -1:', shop_list[1:-1])
# print('Elements from the beggining to the end:', shop_list[:])
#
# print(name)
#
# # string clipping
# print('Symbols with 1 to 3:', name[1:3])
# print('Symbols with 2 to the end:', name[2:])
# print('Symbols with 1 to -1:', name[1:-1])
# print('Symbols from the beggining to the end:', name[:])
# endregion

# region SET
# bri = {'Brazil', 'Russia', 'India'}
# print('India' in bri)
# # True
# print('USA' in bri)
# # False
# bric = bri.copy()
# bric.add('China')
# bric.issuperset(bri)
# # True
# bri.remove('Russia')
#
# # & intersection of set
# print(bri & bric)      # OR bri.intersection(bric)
# # ('Brazil', 'India')
# endregion

# region LINKS
# print('simple assignment')
# shop_list = ['apples', 'mango', 'carrot', 'bananas']
# my_list = shop_list     # my_list is only another name pointing to the same object
#
# del shop_list[0]    # i made the first purchase so I am deleted it from the list
#
# print('shoplist:', shop_list)
# print('mylist:', my_list)
# # note that both a shoplist and a mylist display the same list
# # without the item 'apple', thereby confirming that they point to the same object
#
# print('full cut copying')
# my_list = shop_list[:]      # create a copy by full clipping
# del my_list[0]      # delete first element
#
# print('shoplist:', shop_list)
# print('mylist', my_list)
# # note that now the lists are different
# endregion

# region MORE ABOUT THE STRINGS
# name = 'Swaroop'    # this is a string object
#
# if name.startswith('Swa'):
# 	print('yes, the string starts with "Swa"')
#
# if 'a' in name:
# 	print('Yes, it contains the string "a"')
#
# if name.find('war') != -1:
# 	print(name.find('war'))
# 	print('Yes, it contains the string "war"')
#
# delimiter = '_*_'
# my_list = ['Brazil', 'Russia', 'India', 'China']
# print(delimiter.join(my_list))
# endregion

# region OBJECT ORIENTED PROGRAMMING

# region Common_class (1)
# class Person:
# 	def __init__(self, name):
# 		self.name = name
#
# 	def say_hi(self):
# 		print(f'Hello, my name is {self.name}')
#
# 	def say_bye(self):
# 		print(f'Bye bye {self.name}')
#
#
# p = Person('Swaroop')
# p.say_hi()
# # we can combine the instructions for creating an instance of class and call the method
# Person('Swaroop').say_hi()
# endregion


# region EX:robot (2)

# class Robot:
# 	"""Represents a robot, with a name\n"""
#
# 	# A class variable, counting the number of robots
# 	population = 0
#
# 	def __init__(self, name):  # __init__ - class constructor
# 		"""initializes the data\n"""
# 		self.name = name
# 		print(f"(initializing {self.name})")
#
# 		# when this person is created, the robot
# 		# adds to the population
# 		Robot.population += 1
#
# 	def __del__(self):
# 		"""i die\n"""
# 		print(f'{self.name} is being destroyed!')
#
# 		Robot.population -= 1
#
# 		if Robot.population == 0:
# 			print(f'{self.name} was the last one.')
# 		else:
# 			print(f'there are still {Robot.population} robots working.')
#
# 	def say_hi(self):
# 		"""greetings by the robot.\nYeah. they can do that\n"""
# 		print(f'greetings, my masters call me {self.name}.')
#
# 	# def how_many():
# 	# 	"""prints the current population"""
# 	# 	print(f' we have {Robot.population} robots.')
# 	#
# 	# how_many = staticmethod(how_many)
#
# 	@staticmethod
# 	def how_many():
# 		"""prints the current population\n"""
# 		print(f'we have {Robot.population} robots.')
#
# 	# @classmethod
# 	# def how_many(cls):
# 	# 	"""prints the current population"""
# 	# 	print(f'we have {Robot.population} robots.')
# 	# 	return 'class method called', cls
#
#
# print(Robot.__doc__)
# print(Robot.__init__.__doc__)
# print(Robot.__del__.__doc__)
# print(Robot.say_hi.__doc__)
# print(Robot.how_many.__doc__)
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# Robot.how_many()
#
#
# # --- another way to call a class instance method
# # Robot.say_hi(droid1)
# # Robot.say_hi(droid2)
#
# # -*-*- static method can be called through a class object
# # droid1.how_many()
# # droid2.how_many()
#
# # -*-*- class method can be called through a class object
# # print(droid1.how_many())
# # print(droid2.how_many())
#
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# Robot.how_many()
#
# print("\nRobots have finished their work. So let's destroy them.\n")
#
# del droid1
# del droid2
#
# Robot.how_many()
# # -*-*- static method CAN'T be called through a class object, if it DEAD

# endregion


# region inheritance_precis (3)
# region Simple inheritance of parent class methods     1-1-1-1
# class Table:
# 	def __init__(self, l, w, h):
# 		self.lenght = l
# 		self.width = w
# 		self.height = h
#
#
# class KitchenTable(Table):
# 	def set_places(self, p):
# 		self.places = p
#
#
# class DeskTable(Table):
# 	def square(self):
# 		return self.width * self.lenght
#
#
# # t1 = KitchenTable()   # __init__() missing 3 required positional arguments: 'l', 'w' and 'h'
# t1 = KitchenTable(2, 2, 0.7)
# t2 = DeskTable(1.5, 0.8, 0.75)
# t3 = KitchenTable(1, 1.2, 0.8)
#
# t4 = Table(1, 1, 0.5)
# print(t2.square())
# # t4.square()     # Error due to the fact that 'Table' object has no attribute 'square'
# # t3.square()     # Error due to the fact that 'KitchenTable' object has no attribute 'square'
# # - All mammals have a four-chambered heart, but only rhinos have a horn
# endregion                                             1-1-1-1


# region Overriding the overclass method completely     2-2-2-2
# class ComputerTable(DeskTable):
# 	def square(self, e):
# 		return self.width * self.lenght - e
# endregion                                             2-2-2-2


# region Addition, it is an extension of the method     3-3-3-3
# class ComputerTable(DeskTable):
# 	def __init__(self, l, w, h, e):
# 		Table.__init__(self, l, w, h)
# 		self.e = e
#
# 	def square(self):
# 		return DeskTable.square(self) - self.e
#
#
# ct = ComputerTable(2, 1, 1, 1)
# print(ct.square())
#
#
# # This is not the best way if almost the entire constructor of the superclass is duplicated (1)
# # class KitchenTable(Table):
# # 	def __init__(self, l, w, h, p):
# # 		self.lenght = l
# # 		self.width = w
# # 		self.height = h
# # 		self.places = p
#
# # It is easier to call the parent constructor, and then complete it with your code (2)
# class KitchenTable(Table):
# 	def __init__(self, l, w, h, p):
# 		Table.__init__(self, l, w, h)   # Call parent constructor
# 		self.places = p
# # (1) and (2) classes are equivalent
#
#
# tk = KitchenTable(2, 1.5, 0.7, 10)
# print(tk.places)
# print(tk.width)
# endregion                                             3-3-3-3
# endregion


# region inheritance (4)
# class SchoolMember:
# 	"""Represents any school member"""
# 	# membership = True
#
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		print(f'Initialized SchoolMember: {self.name}')
#
# 	def tell(self):
# 		"""Tell my details"""
# 		print(f'Name: {self.name} Age: {self.age}', end=" ")
#
#
# class Teacher(SchoolMember):
# 	"""Represents a teacher"""
# 	def __init__(self, name, age, salary):
# 		SchoolMember.__init__(self, name, age)
# 		self.salary = salary
# 		print(f'(Initialized Teacher: {self.name})')
#
# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print(f'Salary: {self.salary}')
#
#
# class Student(SchoolMember):
# 	"""Represents a student"""
# 	def __init__(self, name, age, marks):
# 		SchoolMember.__init__(self, name, age)
# 		self.marks = marks
# 		print(f'(Initialized Student: {self.name})')
#
# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print(f'Marks: {self.marks}')
#
#
# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
#
# # prints a blank line
# print()
#
# members = (t, s)
# for member in members:
# 	# Works for both Teachers and Students
# 	member.tell()


# # Ilya's programm
# # def print_info(school_member):
# # 	print("Name = %s Age = %s" % (school_member.name, school_member.age))
# #
# # school1 = SchoolMember('Artem', 25)
# # SchoolMember.info = print_info
# # school1.info()
# endregion


# region Metaclass (5)
# !/usr/bin/env python
# Filename: inherit_abc.py

# from abc import *
#
#
# class SchoolMember(metaclass=ABCMeta):
# 	"""Represents any school member."""
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		print(f'(Initialized SchoolMember: {self.name})')
#
# 	@abstractmethod
# 	def tell(self):
# 		"""Print info."""
# 		print(f'Name:"{self.name}" Age:"{self.age}"', end=" ")
#
#
# class Teacher(SchoolMember):
# 	"""Represents a teacher."""
# 	def __init__(self, name, age, salary):
# 		SchoolMember.__init__(self, name, age)
# 		self.salary = salary
# 		print(f'(Initialized Teacher: {self.name})')
#
# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print(f'Salary: {self.salary}')
#
#
# class Student(SchoolMember):
# 	"""Represents a student."""
# 	def __init__(self, name, age, marks):
# 		SchoolMember.__init__(self, name, age)
# 		self.marks = marks
# 		print(f'Initialized Student: {self.name}')
#
# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print(f'Marks: {self.marks}')
#
#
# t = Teacher('Mrs.Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
#
# # m = SchoolMember('abc', 10)
# # This will result in an Error: "TypeError: Can't instantiate abstract class
# # SchoolMember with abstact methods tell"
#
# print()
#
# members = [t, s]
# for member in members:
# 	member.tell()
# endregion

# endregion

# region INPUT/OUTPUT

# # region User Input (1)
# def reverse(text):
# 	return text[::-1]
#
#
# def is_palindrome(text):
# 	return text == reverse(text)
#
#
# something = input('Input text: ')
#
# if is_palindrome(something):
# 	print("Yes, it is palindrome")
# else:
# 	print("No, it is not palindrome")


# def reverse(text):
# 	return text[::-1]
#
#
# def is_palindrome(text):
# 	return text == reverse(text)
#
#
# def cleaner(text):
# 	global something
# 	something = something.lower()
# 	forbidden = ('.', '?', '!', ':', ';', '-', '—', ' ', ',', '/')
# 	for i in forbidden:
# 		something = something.replace(i, "")
# 	return is_palindrome(something)
#
#
# something = (input('Input text: '))
#
# # (check this operation) something = "".join(symbol for symbol in forbidden if symbol not in forbidden)
#
# if cleaner(something):
# 	print("Yes, it is palindrome")
# else:
# 	print("No, it is not palindrome")


import re


# def reverse(text):
# 	return text[::-1]
#
#
# def is_polindrome(text):
# 	return text == reverse(text)
#
#
# def cleaner(text):
# 	text = text.lower()
# 	forbidden = ('.', '?', '!', ':', ';', '-', '—', ' ', ',', '/')
# 	for i in forbidden:
# 		text = text.replace(i, "")
# 	return is_polindrome(text)
#
#
# word = input('Input text: ')
#
# if cleaner(word):
# 	print('Yes', word)
# else:
# 	print("no")

# endregion