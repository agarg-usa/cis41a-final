class Burger:
	"""
	Superclass for all burgers
	"""
	def __init__(self, name, price, description):
		"""
		constructor for burger
		"""
		self.name = name
		self.price = price
		self.description = description

	def print_burger(self):
		"""
		prints information about the burger (used in the menu)
		"""
		print(f"{self.price}: {self.name} - {self.description}")

	def get_name(self) -> str:
		"""
		returns the name of the burger
		"""
		return self.name

	def get_price(self) -> int:
		"""
		return the price of the burger
		"""
		return self.price

	def get_description(self) -> str:
		"""
		get description of the burger
		"""
		return self.description

	def set_name(self, name : str):
		"""
		set the name of the burger
		"""
		self.name = name

	def set_price(self, price : int):
		"""
		set the price of the burger
		"""
		self.price = price

	def set_description(self, description : str):
		"""
		set the description of the burger
		"""
		self.description = description

class BurgerCollection:
	"""
	Datastructure to store the burgers
	"""

	@staticmethod
	def get_burger_collection():
		"""
		get the burger collection
		"""
		return BurgerCollection([DeAnzaBurger(), BaconCheese(), MushroomSwiss(), WesternBurger(), DonCaliVeggieBurger()])

	def __init__(self, burgers : list):
		"""
		constructor for burger collection
		"""
		self.burgers = burgers
		self.burgerDict = {}
		for burger in burgers:
			self._add_to_dict(burger)

	def show_menu(self):
		"""
		prints menu of burgers
		"""
		for burger in self.burgers:
			burger.print_burger()

	def does_burger_name_exist(self, name : str):
		"""
		checks if the burger name exists in dict
		"""
		return name in self.burgerDict

	# getters
	def get_burger_by_name(self, name : str):
		"""
		get burger by name
		"""
		return self.burgerDict[name]

	def get_burgers(self) -> list:
		"""
		returns list of burgers
		"""
		return self.burgers

	# setters
	def add_burger(self, burger : Burger):
		"""
		adds burger to collection
		"""
		self.burgers.append(burger)
		self._add_to_dict(burger)

	def _add_to_dict(self, burger : Burger):
		self.burgerDict[burger.name] = burger

	# remove

	def remove_burger(self, burger : Burger):
		"""
		removes burger from collection
		"""
		self.burgers.remove(burger)
		del self.burgerDict[burger.name]


class DeAnzaBurger(Burger):
	def __init__(self):
		super().__init__("De Anza Burger", 5.25, "Charboiled Beef patty, Green Leaf, Tomato, Red Onion, White Cheddar, on a Toasted Bun")

class BaconCheese(Burger):
	def __init__(self):
		super().__init__("Bacon Cheese", 5.75, "Charboiled Beef Patty, Sliced Bacon, Caramelized Onion, American Cheese, on a Toasted Bun")

class MushroomSwiss(Burger):
	def __init__(self):
		super().__init__("Mushroom Swiss", 5.75, "Beef Patty, Mushrooms, Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, Tomato, on a Toasted Bun")

class WesternBurger(Burger):
	def __init__(self):
		super().__init__("Western Burger", 5.75, "Charboiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce, American Cheese, on a Toasted Bun")

class DonCaliVeggieBurger(Burger):
	def __init__(self):
		super().__init__("Don Cali Burger", 5.75, "Spring Mix Lettuce, Tomato, Red Onion, Avocado, Smoked Gouda, on a Toasted Bun")

	def print_burger(self):
		print(f"{self.price}: {self.name} (VEGGIE OPTION FOR VEGETARIANS!) - {self.description}")