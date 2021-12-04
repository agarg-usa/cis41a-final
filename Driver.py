"""
Built by Aryan Garg and Rahul Sengupta
This program uses OOP concepts to help create a ordering system for a burger shop.
"""
from Order import Order

if __name__ == "__main__":
    order = Order()
    order.get_inputs()
    order.save_to_file(order.print_bill())

"""
Are you a student or a staff member? Please enter yes or no: yes
5.25: De Anza Burger - Charboiled Beef patty, Green Leaf, Tomato, Red Onion, White Cheddar, on a Toasted Bun
5.75: Bacon Cheese - Charboiled Beef Patty, Sliced Bacon, Caramelized Onion, American Cheese, on a Toasted Bun
5.75: Mushroom Swiss - Beef Patty, Mushrooms, Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, Tomato, on a Toasted Bun
5.75: Western Burger - Charboiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce, American Cheese, on a Toasted Bun
5.75: Don Cali Burger (VEGGIE OPTION FOR VEGETARIANS!) - Spring Mix Lettuce, Tomato, Red Onion, Avocado, Smoked Gouda, on a Toasted Bun
Please choose your option (Press q to exit): De Anza Burger
How many do you want to buy? 2
5.25: De Anza Burger - Charboiled Beef patty, Green Leaf, Tomato, Red Onion, White Cheddar, on a Toasted Bun
5.75: Bacon Cheese - Charboiled Beef Patty, Sliced Bacon, Caramelized Onion, American Cheese, on a Toasted Bun
5.75: Mushroom Swiss - Beef Patty, Mushrooms, Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, Tomato, on a Toasted Bun
5.75: Western Burger - Charboiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce, American Cheese, on a Toasted Bun
5.75: Don Cali Burger (VEGGIE OPTION FOR VEGETARIANS!) - Spring Mix Lettuce, Tomato, Red Onion, Avocado, Smoked Gouda, on a Toasted Bun
Please choose your option (Press q to exit): q
Bill:
2x De Anza Burger - 5.25 - 10.5
Subtotal - $10.5
Tax - $0
Total - $10.5

Are you a student or a staff member? Please enter yes or no: NO
That was an invalid input, please enter yes or no:
Are you a student or a staff member? Please enter yes or no: no
5.25: De Anza Burger - Charboiled Beef patty, Green Leaf, Tomato, Red Onion, White Cheddar, on a Toasted Bun
5.75: Bacon Cheese - Charboiled Beef Patty, Sliced Bacon, Caramelized Onion, American Cheese, on a Toasted Bun
5.75: Mushroom Swiss - Beef Patty, Mushrooms, Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, Tomato, on a Toasted Bun
5.75: Western Burger - Charboiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce, American Cheese, on a Toasted Bun
5.75: Don Cali Burger (VEGGIE OPTION FOR VEGETARIANS!) - Spring Mix Lettuce, Tomato, Red Onion, Avocado, Smoked Gouda, on a Toasted Bun
Please choose your option (Press q to exit): asdf
Burger does not exist.
5.25: De Anza Burger - Charboiled Beef patty, Green Leaf, Tomato, Red Onion, White Cheddar, on a Toasted Bun
5.75: Bacon Cheese - Charboiled Beef Patty, Sliced Bacon, Caramelized Onion, American Cheese, on a Toasted Bun
5.75: Mushroom Swiss - Beef Patty, Mushrooms, Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, Tomato, on a Toasted Bun
5.75: Western Burger - Charboiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce, American Cheese, on a Toasted Bun
5.75: Don Cali Burger (VEGGIE OPTION FOR VEGETARIANS!) - Spring Mix Lettuce, Tomato, Red Onion, Avocado, Smoked Gouda, on a Toasted Bun
Please choose your option (Press q to exit): De Anza Burger
How many do you want to buy? -1
That was an invalid input. Please enter a number greater than or equal to 0
How many do you want to buy? 1as
That was an invalid input. Please enter a number greater than or equal to 0
How many do you want to buy? 3
5.25: De Anza Burger - Charboiled Beef patty, Green Leaf, Tomato, Red Onion, White Cheddar, on a Toasted Bun
5.75: Bacon Cheese - Charboiled Beef Patty, Sliced Bacon, Caramelized Onion, American Cheese, on a Toasted Bun
5.75: Mushroom Swiss - Beef Patty, Mushrooms, Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, Tomato, on a Toasted Bun
5.75: Western Burger - Charboiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce, American Cheese, on a Toasted Bun
5.75: Don Cali Burger (VEGGIE OPTION FOR VEGETARIANS!) - Spring Mix Lettuce, Tomato, Red Onion, Avocado, Smoked Gouda, on a Toasted Bun
Please choose your option (Press q to exit): Bacon Cheese
How many do you want to buy? 5
5.25: De Anza Burger - Charboiled Beef patty, Green Leaf, Tomato, Red Onion, White Cheddar, on a Toasted Bun
5.75: Bacon Cheese - Charboiled Beef Patty, Sliced Bacon, Caramelized Onion, American Cheese, on a Toasted Bun
5.75: Mushroom Swiss - Beef Patty, Mushrooms, Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, Tomato, on a Toasted Bun
5.75: Western Burger - Charboiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce, American Cheese, on a Toasted Bun
5.75: Don Cali Burger (VEGGIE OPTION FOR VEGETARIANS!) - Spring Mix Lettuce, Tomato, Red Onion, Avocado, Smoked Gouda, on a Toasted Bun
Please choose your option (Press q to exit): Don Cali Burger
How many do you want to buy? 9
5.25: De Anza Burger - Charboiled Beef patty, Green Leaf, Tomato, Red Onion, White Cheddar, on a Toasted Bun
5.75: Bacon Cheese - Charboiled Beef Patty, Sliced Bacon, Caramelized Onion, American Cheese, on a Toasted Bun
5.75: Mushroom Swiss - Beef Patty, Mushrooms, Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, Tomato, on a Toasted Bun
5.75: Western Burger - Charboiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce, American Cheese, on a Toasted Bun
5.75: Don Cali Burger (VEGGIE OPTION FOR VEGETARIANS!) - Spring Mix Lettuce, Tomato, Red Onion, Avocado, Smoked Gouda, on a Toasted Bun
Please choose your option (Press q to exit): asdf
Burger does not exist.
5.25: De Anza Burger - Charboiled Beef patty, Green Leaf, Tomato, Red Onion, White Cheddar, on a Toasted Bun
5.75: Bacon Cheese - Charboiled Beef Patty, Sliced Bacon, Caramelized Onion, American Cheese, on a Toasted Bun
5.75: Mushroom Swiss - Beef Patty, Mushrooms, Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, Tomato, on a Toasted Bun
5.75: Western Burger - Charboiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce, American Cheese, on a Toasted Bun
5.75: Don Cali Burger (VEGGIE OPTION FOR VEGETARIANS!) - Spring Mix Lettuce, Tomato, Red Onion, Avocado, Smoked Gouda, on a Toasted Bun
Please choose your option (Press q to exit): q
Bill:
3x De Anza Burger - 5.25 - 15.75
5x Bacon Cheese - 5.75 - 28.75
9x Don Cali Burger - 5.75 - 51.75
Subtotal - $96.25
Tax - $8.66
Total - $104.91
"""