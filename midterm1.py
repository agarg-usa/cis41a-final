"""
Aryan Garg (worked with Rahul Sengupta)

this code asks for a user to pick an item from a menu, and then for the quantity of that item.
After the user is done ordering, it calculates the price of their food along with their tax
"""

"""
This method displays the menu for the user to choose and input their choice.
"""
def show_menu():
    print("Welcome to De Anza Grill!")
    print("1 - De Anza Burger - $5.25")
    print("2 - Bacon Cheese - $5.75")
    print("3 - Mushroom Swiss - $5.95")
    print("4 - Western Burger - $5.95")
    print("5 - Don Cali Burger - $5.95")
    print("6 - Exit")


"""
This method gets the input from the user, by repeatedly asking the user what it wants to order
then asking for the quantity of what the user will order
"""
def get_inputs():
    quantities = [0, 0, 0, 0, 0]

    while True:
        is_discount = input("Are you a student or a staff member? Please enter yes or no: ")
        if is_discount == "yes":
            is_discount = True
        elif is_discount == "no":
            is_discount = False
        else:
            print("That was an invalid input, please enter yes or no: ")
            continue
        break

    while True:
        show_menu()
        item = input("Please choose your option: ").strip()
        try:
            item = int(item)
            if item == 6:
                return print_bill(quantities[0], quantities[1], quantities[2], quantities[3], quantities[4],
                                  is_discount)

            elif item > 6 or item < 0:
                raise ValueError("invalid number")
            else:
                while True:
                    quantity = input("How many do you want to buy? ")
                    try:
                        quantity = int(quantity)
                        if quantity < 0:
                            raise ValueError("Negative number")
                        item = item - 1
                        quantities[item] += quantity
                        break
                    except ValueError:
                        print("That was an invalid input. Please enter a number greater than or equal to 0")
        except ValueError:
            print("That was an invalid input, please put a number between 1 - 6")


"""
This method is a helper method that computes the bill for the print function to call.
"""
def compute_bill(quantity1, quantity2, quantity3, quantity4, quantity5, is_discount):
    total_cost = (quantity1 * 5.25) + (quantity2 * 5.75) + (quantity3 * 5.95) + (quantity4 * 5.95) + (quantity5 * 5.95)
    if is_discount:
        tax = 0
        total_cost_after_tax = total_cost
    else:
        tax = total_cost * 0.09
        total_cost_after_tax = total_cost * 1.09

    return (total_cost, total_cost_after_tax, tax)


"""
This method displays the contents of the bill, including the total taxed value depending on discount status.
"""
def print_bill(quantity1, quantity2, quantity3, quantity4, quantity5, is_discount):
    price_before_tax, price_after_tax, tax = compute_bill(quantity1, quantity2, quantity3, quantity4, quantity5,
                                                          is_discount)
    print("Bill:")
    if quantity1 != 0:
        print("De Anza Burger - $5.25 - " + str(round(quantity1, 2)))
    if quantity2 != 0:
        print("Bacon Cheese - $5.75 - " + str(round(quantity2, 2)))
    if quantity3 != 0:
        print("Mushroom Swiss - $5.95 - " + str(round(quantity3, 2)))
    if quantity4 != 0:
        print("Western Burger - $5.95 - " + str(round(quantity4, 2)))
    if quantity5 != 0:
        print("Don Cali Burger - $5.95 - " + str(round(quantity5, 2)))
    print("Subtotal - $" + str(round(price_before_tax, 2)))
    print("Tax - $" + str(round(tax, 2)))
    print("Total - $" + str(round(price_after_tax, 2)))


"""
main method
"""
def main():
    get_inputs()


if __name__ == "__main__":
    main()

"""
test 1:

Are you a student or a staff member? Please enter yes or no: no
Welcome to De Anza Grill!
1 - De Anza Burger - $5.25
2 - Bacon Cheese - $5.75
3 - Mushroom Swiss - $5.95
4 - Western Burger - $5.95
5 - Don Cali Burger - $5.95
6 - Exit
Please choose your option: 2
How many do you want to buy? 45
Welcome to De Anza Grill!
1 - De Anza Burger - $5.25
2 - Bacon Cheese - $5.75
3 - Mushroom Swiss - $5.95
4 - Western Burger - $5.95
5 - Don Cali Burger - $5.95
6 - Exit
Please choose your option: 1
How many do you want to buy? 5
Welcome to De Anza Grill!
1 - De Anza Burger - $5.25
2 - Bacon Cheese - $5.75
3 - Mushroom Swiss - $5.95
4 - Western Burger - $5.95
5 - Don Cali Burger - $5.95
6 - Exit
Please choose your option: 6
Bill:
De Anza Burger - $5.25 - 5
Bacon Cheese - $5.75 - 45
Subtotal - $285.0
Tax - $25.65
Total - $310.65

test 2:

Are you a student or a staff member? Please enter yes or no: a
That was an invalid input, please enter yes or no:
Are you a student or a staff member? Please enter yes or no: yes
Welcome to De Anza Grill!
1 - De Anza Burger - $5.25
2 - Bacon Cheese - $5.75
3 - Mushroom Swiss - $5.95
4 - Western Burger - $5.95
5 - Don Cali Burger - $5.95
6 - Exit
Please choose your option:
That was an invalid input, please put a number between 1 - 6
Welcome to De Anza Grill!
1 - De Anza Burger - $5.25
2 - Bacon Cheese - $5.75
3 - Mushroom Swiss - $5.95
4 - Western Burger - $5.95
5 - Don Cali Burger - $5.95
6 - Exit
Please choose your option: 1
How many do you want to buy? 3
Welcome to De Anza Grill!
1 - De Anza Burger - $5.25
2 - Bacon Cheese - $5.75
3 - Mushroom Swiss - $5.95
4 - Western Burger - $5.95
5 - Don Cali Burger - $5.95
6 - Exit
Please choose your option: 5
How many do you want to buy? as
That was an invalid input. Please enter a number greater than or equal to 0
How many do you want to buy? 5
Welcome to De Anza Grill!
1 - De Anza Burger - $5.25
2 - Bacon Cheese - $5.75
3 - Mushroom Swiss - $5.95
4 - Western Burger - $5.95
5 - Don Cali Burger - $5.95
6 - Exit
Please choose your option: as
That was an invalid input, please put a number between 1 - 6
Welcome to De Anza Grill!
1 - De Anza Burger - $5.25
2 - Bacon Cheese - $5.75
3 - Mushroom Swiss - $5.95
4 - Western Burger - $5.95
5 - Don Cali Burger - $5.95
6 - Exit
Please choose your option: 2
How many do you want to buy? 4
Welcome to De Anza Grill!
1 - De Anza Burger - $5.25
2 - Bacon Cheese - $5.75
3 - Mushroom Swiss - $5.95
4 - Western Burger - $5.95
5 - Don Cali Burger - $5.95
6 - Exit
Please choose your option: 6
Bill:
De Anza Burger - $5.25 - 3
Bacon Cheese - $5.75 - 4
Don Cali Burger - $5.95 - 5
Subtotal - $68.5
Tax - $0
Total - $68.5
"""