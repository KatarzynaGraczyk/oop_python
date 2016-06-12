class Bacteria:
    'Common base class for all bacterias'
    name = ""
    species = ""
    metabolismType = ""
    bacteriaCount = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Bacteria.bacteriaCount += 1

    def displayName(self):
        print "My name is: ", self.name

    def displaySpecies(self):
        print "My species name is: ",  self.species

    def displayMetabolism(self):
        print "My metabolism type is: ", self.metabolismType