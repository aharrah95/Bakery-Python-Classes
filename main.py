class Desserts:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price

        print("Welcome to our sweets shop! Take your time looking over our menu.")


class Cake(Desserts):
        cake1 = Desserts('Black Forest Cake', '$30')
        cake2 = Desserts('Red Velvet Cake', '$25')
        cake3 = Desserts('Devils Food Cake', '$50')
        cake4 = Desserts('Angel Food Cake', '$40')
        cake5 = Desserts('Funfetti Cake', '$20')
        cake6 = Desserts('Tuxedo Cake', '$35')
        cake7 = Desserts('German Chocolate Cake', '$35')

        print("CAKE MENU:")
        print(cake1.flavor + " | " + cake1.price)
        print(cake2.flavor + " | " + cake2.price)
        print(cake3.flavor + " | " + cake3.price)
        print(cake4.flavor + " | " + cake4.price)
        print(cake5.flavor + " | " + cake5.price)
        print(cake6.flavor + " | " + cake6.price)
        print(cake7.flavor + " | " + cake7.price)
        print(" ")

        print("I'd love a slice of " + cake1.flavor + "!")
        print("Certainly. That will be " + cake1.price + ".")