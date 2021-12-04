from Order import Order

if __name__ == "__main__":
    flag = True
    while flag:
        order = Order()
        order.get_inputs()
        order.save_to_file(order.print_bill())
