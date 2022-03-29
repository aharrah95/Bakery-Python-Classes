class Desserts:
    def __init__(self, kind, flavor, price):
        self.type = kind
        self.flavor = flavor
        self.price = price


class Cake(Desserts):
            cake1 = Desserts('Cake', 'Black Forest Cake', '$30')
            cake2 = Desserts('Cake', 'Red Velvet Cake', '$25')
            cake3 = Desserts('Cake', 'Devils Food Cake', '$50')
            cake4 = Desserts('Cake', 'Angel Food Cake', '$40')
            cake5 = Desserts('Cake', 'Funfetti Cake', '$20')

            print("I'd love a slice of " + cake1.flavor + "!")
            print("Certainly. That will be " + cake1.price + " dollars.")