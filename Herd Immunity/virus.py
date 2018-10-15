class Virus:
    def __init__(self, name, infection_rate, mortality_rate):
        self.name = name
        self.infection_rate = infection_rate
        self.mortality_rate = mortality_rate

    def display(self,item):
        print("{}. {} - Basic Reproduction Number (R0): {}, Mortality_rate: {}".format(item,self.name,self.infection_rate*20, self.mortality_rate))

viruses = [
    Virus("Anthrax", .325, .20),
    Virus("Bubonic Plague", .5, 1),
    Virus("Chicken Pox", .435, 0),
    Virus("Ebola", .125, .7),
    Virus("Cold", .3, 0),
    Virus("Test Virus", 1, 0)
]