from classes import Cart

def get_orders():    
    cart = Cart()

    while True:
        try: 
            item = input("Enter item: ")
            if cart.add(item):
                print(cart)
        except EOFError:
            print()
            break