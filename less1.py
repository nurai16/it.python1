class Computer:
    def __init__(self, model, price, qty):
        self.model = model
        self.price = price
        self.qty = qty


class Laptop(Computer):
    mobile = True

    def __init__(self, model, price, qty, battery):
        super().__init__(model, price, qty)
        self.battery = battery


class MacBook(Laptop):
    def __init__(self, price, qty, type):
        battery = 10
        model = f"MacBook {type}"
        super().__init__(model, price, qty, battery)
        self.type = type


class Cup:
    def __init__(self, price, qty):
        self.price = price
        self.qty = qty


class Money:
    count = 0

    def sell(self, good_object):
        if good_object.qty == 0:
            print(f"Товара {good_object.model} НЭТ!")
        else:
            self.count += good_object.price
            good_object.qty -= 1

        self.report()

    def report(self):
        print(f"Бюджет - {self.count}")


comp_1 = Computer("HP probook 321", 750, 2)
# print(comp_1.price)
comp_2 = Computer("Asus Nitro 5", 900, 10)

august_money = Money()
august_money.sell(comp_1)
august_money.sell(comp_1)
august_money.sell(comp_1)
august_money.sell(Cup(100, 4))

laptop_1 = Laptop("Lenovo", 500, 20, 3)
august_money.sell(laptop_1)
print(laptop_1.battery)
mac_1 = MacBook(1000, 5, "Air")
print(mac_1.model)