import enum


class Text(enum.Enum):
	first_input = 'Enter the first number: '
	operation = '["+", "-", "*", "/"]\nEnter a number from 1 to 4: '
	second_input = 'Enter the second number: '
	y2_interval = 'Enter a number from 1 to 4: '
	string = 'Don not enter strings'


class CheckArguments:
	def __init__(self):
		self.x = input(Text.first_input.value)
		self.y = input(Text.operation.value)
		self.z = input(Text.second_input.value)
		self.clean_arg = []

	def checker(self):
		while True:
			try:
				x2 = int(self.x)
				y2 = int(self.y)
				z2 = int(self.z)
				if y2 < 1 or y2 > 4:
					print(Text.y2_interval.value)
					create_element1()
			except ZeroDivisionError:
				print(Text.string.value)
				create_element1()
			else:
				self.clean_arg = [x2, y2, z2]
				break


class Answer(CheckArguments):
	def calculation(self):
		if self.clean_arg[1] == 1:
			addition = self.clean_arg[0] + self.clean_arg[2]
			print(addition)

		if self.clean_arg[1] == 2:
			subtraction = self.clean_arg[0] - self.clean_arg[2]
			print(subtraction)

		if self.clean_arg[1] == 4 and self.clean_arg[2] != 0:
			privare = self.clean_arg[0] / self.clean_arg[2]
			print(privare)

		if self.clean_arg[1] == 3:
			product = self.clean_arg[0] * self.clean_arg[2]
			print(product)


def create_element1():
	roll = Answer()
	roll.checker()
	roll.calculation()


create_element1()

# read about switch case
# modification processing on zero
# read about decorators
# CHANGE REGION COLOR

# shift + windows + s
# lite shot
# windows + l
# help(any type of data)
