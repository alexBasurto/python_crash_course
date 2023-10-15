#módulo pizza
def make_pizza(size, *toppings):
    """Resume la pizza que estamos a punto de hacer."""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")
