class Bacteria:
    'Common base class for all bacterias'
    name = ""
    species = ""
    metabolismType = ""
    bacteriaCount = 0
    pathogenicity = ""

    def __init__(self, name, species, pathogenicity):
        self.name = name
        self.species = species
        self.pathogenicity = pathogenicity
        Bacteria.bacteriaCount += 1

    def displayName(self):
        print "My name is: ", self.name

    def displaySpecies(self):
        print "My species name is: ",  self.species

    def displayMetabolism(self):
        print "My metabolism type is: ", self.metabolismType

    #Checking and printing pathogenicity of bacteria

    def displayPathogenicity(self):
        if self.pathogenicity == "Yes":
            print "I'm pathogenic"
        else:
            print "I'm not pathogenic"
