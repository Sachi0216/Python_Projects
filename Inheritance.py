

# parent class

class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {} \nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

# Child class instance
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'
    Height = '6 ft'
    weight = '175 lbs'

    def information(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

# another child class instance
class Dog(Organism):
    name = "Spot"
    species = 'Canine'
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = 'Earth'
    color = 'Black'
    Breed = 'Husky'

    def information(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg


# another child class instance
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = 'Mars'

    def information(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms!"
        return msg











if __name__ == "__main__":
    human = Human()
    print(human.information())
    


    dog = Dog()
    print(dog.information())
    


    bacteria = Bacterium()
    print(bacteria.information())
    