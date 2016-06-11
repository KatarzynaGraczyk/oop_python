class Bacteria:
    _name = ""
    _species = ""
    metabolismType = ""

    def __init__(self, name, species):
        self._name = name
        self._species = species

    def printName(self):
        print "My name is: " + self._name

    def printSpecies(self):
        print "My species name is: " + self._species

    def printMetabolism(self):
        print "My metabolism type is: " + self.metabolismType