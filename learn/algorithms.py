# region CLASS

# class OneDimension:
# 	def __init__(self, x):
# 		self._x = x
#
# 	def setx(self, x):
# 		self._x = x
#
# 	def getx(self):
# 		return self._x
#
# 	def useless(self):
# 		print('useless method')
#
#
# class TwoDimension(OneDimension):
# 	def __init__(self, x, y):
# 		super(TwoDimension, self).__init__(x)
# 		self._y = y
#
# 	def sety(self, y):
# 		self._y = y
#
# 	def gety(self):
# 		return self._y
#
#
# first = OneDimension(10)
# first.setx(15)
# print(first.getx())
# second = TwoDimension(2, 5)
# second.setx(3)
# second.sety(6)
# print(second.getx(), second.gety())
# first.useless()
# second.useless()

# endregion

# # region
# def find_smallest(list):
# 	smallest = list[0]
# 	smallest_index = 0
# 	for i in range(1, len(list)):
# 		if list[i] < smallest:
# 			smallest = list[i]
# 			smallest_index = i
# 	return smallest_index

#
#
# def selectionSort(list):
# 	newList = []
# 	for i in range(len(list)):
# 		smallest = indSmallest(list)
# 		newList.append(list.pop(smallest))
# 	return (selectionSort([1, 5, 6, 6, 0]))

# x = "Hello world"
# print(x)
# print(type(x))
# x = 1 + 2 + 3 * 2

# обмен значений переменых
# a = 2
# b = 5
# tmp = a
# a = b
# b = tmp

# обмен через временный кортеж (в данном случае создаются 2 ссылки)
# a = 2
# b = 5
# tmp1 = b    tmp1, tmp2 = b, a
# tmp2 = a                        a, b = b, a
# a = tmp1    a, b = tmp1, tmp2
# b = tmp2

# y = -16 // 5
# x = -16 % 5
# print(y, x)

# x = int(input())
# while x > 0:
# 	y = x
# 	while y > 0:
# 		y -= 1
# 		print(y)
# 	x -= 1
# print("stop")
# # endregion

# region нахождение хотя бы одного числа делящегося на 10
# flag = False
# N = int(input())
# for i in range(N):
# 	x = int(input())
# 	flag = (x % 10 == 0) or flag
# print(flag)
# endregion

# region проверка на дилимость ВСЕЙ последовательности на 10
# flag = True
# N = int(input())
# for i in range(N):
# 	x = int(input())
# 	flag = (x % 10 == 0 and flag)
# print(flag)
# endregion

# x = int(input())
# if x < 0:
# 	print('a')
# elif x < 5:    # x > 0
# 	print('b')
# elif x < 10:
# 	print('c')    # x >= 5
# else:    # x >= 10
# 	print('d')

# region BINARY SEARCH


# def binary_search(list, item):
# 	low = 0
# 	high = len(list) - 1
#
# 	while low <= high:
# 		mid = (low + high)
# 		guess = list[mid]
# 		print(mid)
# 		if guess == item:
# 			return mid
# 		if guess > item:
# 			high = mid - 1
# 		else:
# 			low = mid + 1
# 	return None
#
#
# my_list = [1, 3, 5, 7, 9]
#
# # print(len(my_list))
#
# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))
#
#
#
# def binary_search(list, element):
# 	start = 0
# 	stop = len(list) - 1
# 	mid = (stop + start) // 2
# 	while start <= stop:
# 		if mid == element:
# 			return mid
# 		elif mid > element:
# 			return


# def b_s(li, num, start, stop):
# 	if start > stop:
# 		return False
# 	else:
# 		mid = (start + stop) // 2
# 		if num == li[mid]:
# 			return mid
# 		elif num > li[mid]:
# 			return b_s(li, num, mid + 1, stop)
# 		else:
# 			return b_s(li, num, start, mid - 1)
#
#
# li1 = [i for i in range(1, 101, 2)]
# print(b_s(li1, 99, 0, len(li1) - 1))


# x = []
#
# for i in range(1, 101):
# 	x.append(i)

# x = [i for i in range(1, 101)]

# print(x)

















# endregion
