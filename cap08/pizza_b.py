def make_pizza(*toppings):
    """Resume la pizza que estamos a punto de hacer."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
