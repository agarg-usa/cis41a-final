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
		self.burgerDict = {}
		for burger in burgers:
			self._add_to_dict(burger)

	def add_burger(self, burger):
		self.burgers.append(burger)

	def _add_to_dict(self, burger):
		self.burgerDict[burger.name] = burger

	def show_menu(self):
		for burger in self.burgers:
			burger.print_description()

	def get_burger_by_name(self, name):
		return self.burgerDict[name]

	def get_burgers(self):
		return self.burgers

class DeAnzaBurger(Burger):
	def __init__(self, name, price, description):
		super().__init__(name, price, description)

	def print_description(self):
		print(f"{self.price}: {self.name} + {self.description}")

