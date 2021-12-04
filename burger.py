class Burger:
	def __init__(self, name, price, description):
		self.name = name
		self.price = price
		self.description = description
	def print_description(self):
		raise NotImplementedError("Subclass must implement abstract method")

class BurgerCollection:
	def __init__(self, burgers):
		self.burgers = burgers

	def show_menu():
		print("Welcome to De Anza Grill!")
		print("1 - De Anza Burger - $5.25")
		print("2 - Bacon Cheese - $5.75")
		print("3 - Mushroom Swiss - $5.95")
		print("4 - Western Burger - $5.95")
		print("5 - Don Cali Burger - $5.95")
		print("6 - Exit")