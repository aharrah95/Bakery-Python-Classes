class Desserts:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price


class Cake(Desserts):
        cake1 = Desserts('Black Forest Cake', '$30.00')
        cake2 = Desserts('Red Velvet Cake', '$25.50')
        cake3 = Desserts('Devils Food Cake', '$50.00')
        cake4 = Desserts('Angel Food Cake', '$40.99')
        cake5 = Desserts('Funfetti Cake', '$20.00')
        cake6 = Desserts('Tuxedo Cake', '$35.00')
        cake7 = Desserts('German Chocolate Cake', '$35.00')

        print("CAKE MENU:")
        print(cake1.flavor + " | " + cake1.price)
        print(cake2.flavor + " | " + cake2.price)
        print(cake3.flavor + " | " + cake3.price)
        print(cake4.flavor + " | " + cake4.price)
        print(cake5.flavor + " | " + cake5.price)
        print(cake6.flavor + " | " + cake6.price)
        print(cake7.flavor + " | " + cake7.price)
        print("")

        print("There is a beautiful " + cake3.flavor + "on display in the bakery window,")
        print("How much for a " + cake7.flavor + "?")
        print("A " + cake7.flavor + " will run you about " + cake7.price + ".")
        print(" ")
        print("--")
        print(" ")


class IceCream:
    iceCream1 = Desserts('Vanilla soft serve', '$2.50')
    iceCream2 = Desserts('Chocolate soft serve', '$2.50')
    iceCream3 = Desserts('Vanilla/Chocolate swirl', '$3.00')
    iceCream4 = Desserts('Strawberry', '$4.00')
    iceCream5 = Desserts('Mint Chocolate Chip', '$4.50')
    iceCream6 = Desserts('Cookies & Cream', '$4.50')
    iceCream7 = Desserts('Banana Split', '$5.50')
    iceCream8 = Desserts('Hot fudge sundae', '$4.50')
    iceCream9 = Desserts('Sea Salt', '$4.00')

    print("ICE CREAM MENU:")
    print(iceCream1.flavor + " | " + iceCream1.price)
    print(iceCream2.flavor + " | " + iceCream2.price)
    print(iceCream3.flavor + " | " + iceCream3.price)
    print(iceCream4.flavor + " | " + iceCream4.price)
    print(iceCream5.flavor + " | " + iceCream5.price)
    print(iceCream6.flavor + " | " + iceCream6.price)
    print(iceCream7.flavor + " | " + iceCream7.price)
    print(iceCream8.flavor + " | " + iceCream8.price)
    print(iceCream9.flavor + " | " + iceCream9.price)
    print(" ")

    print("I'd like a " + iceCream7.flavor + " for me and my son to share, please.")
    print("Excellent choice! That'll be " + iceCream7.price + " please.")
    print("Sometimes I like to go and sit on the clock tower with some " + iceCream9.flavor + " ice cream.")
    print(" ")
    print("--")
    print(" ")


class MilkshakesAndFloats:
    shake1 = Desserts('Vanilla Milkshake', '$6.00')
    shake2 = Desserts('Chocolate Milkshake', '$6.00')
    shake3 = Desserts('Strawberry Milkshake', '$6.00')
    shake4 = Desserts('Cookies & Cream Milkshake', '$6.50')
    soda1 = Desserts('Cream Soda', '$3.00')
    soda2 = Desserts('Cola', '$2.00')
    soda3 = Desserts('Diet Cola', '$2.00')
    soda4 = Desserts('Root Beer', '$3.00')
    rootBeerFloat = Desserts('Root Beer Float', '$4.00')

    print(shake1.flavor + " | " + shake1.price)
    print(shake2.flavor + " | " + shake2.price)
    print(shake3.flavor + " | " + shake3.price)
    print(shake4.flavor + " | " + shake4.price)
    print(soda1.flavor + " | " + soda1.price)
    print(soda2.flavor + " | " + soda2.price)
    print(soda3.flavor + " | " + soda3.price)
    print(soda4.flavor + " | " + soda4.price)
    print(rootBeerFloat.flavor + " | " + soda1.price)
    print(" ")

    print("Hey, let's split a " + rootBeerFloat.flavor + "! Only " + rootBeerFloat.price + " bucks, my treat!")
    print("Ahh, nothing like a good old " + soda1.flavor + " to take me back to the old days.")
    print("Hi, I need a " + shake2.flavor + " and a " + shake3.flavor + " please.")