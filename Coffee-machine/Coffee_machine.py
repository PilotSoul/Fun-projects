class Machine:
    def __init__(self):
        self.ml_of_water = 400
        self.ml_of_milk = 540
        self.gr = 120
        self.cups = 9
        self.dollars = 550
        self.coffee = 0

    def machine_has(self):
        print()
        print("The coffee machine has:")
        print(f"{self.ml_of_water} of water")
        print(f"{self.ml_of_milk} of milk")
        print(f"{self.gr} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.dollars} of money")

    def check(self):
        global name
        a = 0
        if self.cups >= 1:
            if self.coffee == 1:
                if self.ml_of_water >= 250 and self.gr >= 16:
                    a = True
                else:
                    a = False
                    if self.ml_of_water < 250:
                        if self.gr < 16:
                            name = "water and coffee beans"
                        else:
                            name = "water"
                    else:
                        name = "coffee beans"
            elif self.coffee == 2:
                if self.ml_of_water >= 350 and self.gr >= 20 and self.ml_of_milk >= 75:
                    a = True
                else:
                    a = False
                    if self.ml_of_water < 350:
                        if self.gr < 20:
                            if self.ml_of_milk < 75:
                                name = "milk, coffee beans, water"
                            else:
                                name = "water and coffee beans"
                        else:
                            name = "water"
                    elif self.gr < 20:
                        name = "coffee beans"
                    else:
                        name = "milk"
            elif self.coffee == 3:
                if self.ml_of_water >= 200 and self.gr >= 12 and self.ml_of_milk >= 100:
                    a = True
                else:
                    a = False
                    if self.ml_of_water < 200:
                        if self.gr < 12:
                            if self.ml_of_milk < 100:
                                name = "milk, coffee beans, water"
                            else:
                                name = "water and coffee beans"
                        else:
                            name = "water"
                    elif self.gr < 12:
                        name = "coffee beans"
                    else:
                        name = "milk"
        return a

    def make_coffee(self, coffee):
        self.coffee = coffee
        #global ml_of_water, ml_of_milk, gr, cups, dollars
        d = Machine.check(self)
        if coffee == 1:
            if d == True:
                self.ml_of_water -= 250
                self.gr -= 16
                self.cups -= 1
                self.dollars += 4
                print("I have enough resources, making you a coffee!")
            else:
                print(f"Sorry, not enough {name}!")

        elif coffee == 2:
            if d == True:
                self.ml_of_water -= 350
                self.gr -= 20
                self.cups -= 1
                self.dollars += 7
                self.ml_of_milk -= 75
                print("I have enough resources, making you a coffee!")
            else:
                print(f"Sorry, not enough {name}!")

        elif coffee == 3:
            if d == True:
                self.ml_of_water -= 200
                self.gr -= 12
                self.cups -= 1
                self.dollars += 6
                self.ml_of_milk -= 100
                print("I have enough resources, making you a coffee!")
            else:
                print(f"Sorry, not enough {name}!")

    def fill_machine(self, ml_of_water, ml_of_milk, gr, cups):
        print("Write how many ml of water do you want to add:")
        self.ml_of_water += ml_of_water
        print("Write how many ml of milk do you want to add:")
        self.ml_of_milk += ml_of_milk
        print("Write how many grams of coffee beans do you want to add:")
        self.gr += gr
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += cups



machine = Machine()

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    choice = input()
    print()

    if choice == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee = input()
        if coffee == "back":
            continue
        else:
            machine.make_coffee(int(coffee))
            print()

    elif choice == "fill":
        machine.fill_machine(int(input()), int(input()), int(input()), int(input()))
        print()

    elif choice == "take":
        print(f"I gave you ${machine.dollars}")
        machine.dollars = 0
        print()

    elif choice == "remaining":
        machine.machine_has()

    elif choice == "exit":
        break