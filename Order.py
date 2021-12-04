import Burger
import time
import datetime


class Order:
	def __init__(self):
		self.burgerCollection = Burger.BurgerCollection.get_burger_collection()
		self.quantities = dict()
		self.is_discount = False
		self._init_quantity()

	"""
	This method initializes quantities dictionary to 0
	"""
	def _init_quantity(self):
		for burger in self.burgerCollection.get_burgers():
			self.quantities[burger.get_name()] = 0

	"""
	This method gets the input from the user, by repeatedly asking the user what it wants to order
	then asking for the quantity of what the user will order
	"""
	def get_inputs(self):
		while True:
			self.is_discount = input("Are you a student or a staff member? Please enter yes or no: ")
			if self.is_discount == "yes":
				self.is_discount = True
			elif self.is_discount == "no":
				self.is_discount = False
			else:
				print("That was an invalid input, please enter yes or no: ")
				continue
			break

		while True:
			self.burgerCollection.show_menu()
			item = input("Please choose your option (Press q to exit): ").strip()
			if item == "q":
				break
			if not self.burgerCollection.does_burger_name_exist(item):
				print("Burger does not exist.")
				continue
			while True:
				quantity = input("How many do you want to buy? ")
				try:
					quantity = int(quantity)
					if quantity < 0:
						raise ValueError("Negative number")
					self.quantities[item] += quantity
					break
				except ValueError:
					print("That was an invalid input. Please enter a number greater than or equal to 0")

	"""
	This method displays the contents of the bill, including the total taxed value depending on discount status.
	"""
	def print_bill(self):
		price_before_tax, price_after_tax, tax = self.compute_bill()
		output_string = "Bill: \n"
		for burger_name in self.quantities:
			this_burger = self.burgerCollection.get_burger_by_name(burger_name)
			this_name = this_burger.get_name()
			this_price = this_burger.get_price()
			this_quantity = self.quantities[burger_name]
			if(this_quantity == 0):
				continue
			output_string += f"{this_quantity}x {this_name} - {this_price} - {round(this_quantity * this_price, 2)}\n"

		output_string += "Subtotal - $" + str(round(price_before_tax, 2)) + "\n"
		output_string += "Tax - $" + str(round(tax, 2)) + "\n"
		output_string += "Total - $" + str(round(price_after_tax, 2)) + "\n"
		print(output_string)
		return output_string

	"""
	This method is a helper method that computes the bill for the print function to call.
	"""
	def compute_bill(self):
		total_cost = 0
		for burger_name in self.quantities:
			total_cost += self.quantities[burger_name] * self.burgerCollection.get_burger_by_name(
				burger_name).get_price()
		if self.is_discount:
			tax = 0
			total_cost_after_tax = total_cost
		else:
			tax = total_cost * 0.09
			total_cost_after_tax = total_cost * 1.09

		return total_cost, total_cost_after_tax, tax

	"""
	This method saves the outputs of print_bill to a file
	"""
	def save_to_file(self, output):
		time_stamp = time.time()
		order_time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H-%M-%S')
		order_time_stamp += '.txt'
		with open(order_time_stamp, 'w') as file:
			file.write(output)
