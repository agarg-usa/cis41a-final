class Burger:
	def __init__(self, name, price, description):
		self.name = name
		self.price = price
		self.description = description

	def print_description(self):
		print(f"{self.price}: {self.name} - {self.description}")

	def get_name(self):
		return self.name

	def get_price(self):
		return self.price

	def get_description(self):
		return self.description

	def set_name(self, name):
		self.name = name

	def set_price(self, price):
		self.price = price

	def set_description(self, description):
		self.description = description

class BurgerCollection:

	@staticmethod
	def get_burger_collection():
		return BurgerCollection([DeAnzaBurger(), BaconCheese(), MushroomSwiss(), WesternBurger(), DonCaliVeggieBurger()])

	def __init__(self, burgers):
		self.burgers = burgers
		self.burgerDict = {}
		for burger in burgers:
			self._add_to_dict(burger)

	def show_menu(self):
		for burger in self.burgers:
			burger.print_description()

	# getters
	def get_burger_by_name(self, name):
		return self.burgerDict[name]

	def get_burgers(self):
		return self.burgers

	# setters
	def add_burger(self, burger):
		self.burgers.append(burger)
		self._add_to_dict(burger)

	def _add_to_dict(self, burger):
		self.burgerDict[burger.name] = burger

	# remove

	def remove_burger(self, burger):
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

	def print_description(self):
		print(f"{self.price}: {self.name} (VEGGIE OPTION FOR VEGETARIANS!) - {self.description}")