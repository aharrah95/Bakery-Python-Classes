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

        #print("CAKE MENU:")
        #print(cake1.flavor + " | " + cake1.price)
        #print(cake2.flavor + " | " + cake2.price)
        #print(cake3.flavor + " | " + cake3.price)
        #print(cake4.flavor + " | " + cake4.price)
        #print(cake5.flavor + " | " + cake5.price)
        #print(cake6.flavor + " | " + cake6.price)
        #print(cake7.flavor + " | " + cake7.price)
        #print(" ")

        #print("There is a beautiful " + cake3.flavor + "on display in the bakery window,")
        #print("")
        #print("How much for a " + cake7.flavor + "?")
        #print("A " + cake7.flavor + " will run you about " + cake7.price + ".")


class IceCream:
    iceCream1 = Desserts('Vanilla soft serve', '$2.50')
    iceCream2 = Desserts('Chocolate soft serve', '$2.50')
    iceCream3 = Desserts('Vanilla/Chocolate swirl', '$3.00')
    iceCream4 = Desserts('Strawberry', '$4.00')
    iceCream5 = Desserts('Mint Chocolate Chip', '$4.50')
    iceCream6 = Desserts('Cookies & Cream', '$4.50')
    iceCream7 = Desserts('Banana Split', '$5.50')
    iceCream8 = Desserts('Hot fudge sundae', '$4.50')

    print("ICE CREAM MENU:")
    print(iceCream1.flavor + " | " + iceCream1.price)
    print(iceCream2.flavor + " | " + iceCream2.price)
    print(iceCream3.flavor + " | " + iceCream3.price)
    print(iceCream4.flavor + " | " + iceCream4.price)
    print(iceCream5.flavor + " | " + iceCream5.price)
    print(iceCream6.flavor + " | " + iceCream6.price)
    print(iceCream7.flavor + " | " + iceCream7.price)
    print(iceCream8.flavor + " | " + iceCream8.price)
    print("")

    print("I'd like a " + iceCream7.flavor + " for me and my son to share, please.")
    print("Excellent choice! That'll be " + iceCream7.price + " please.")