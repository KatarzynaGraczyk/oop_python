from model.Bacteria import Bacteria
from model.Aerobs import Aerobs
from model.Anaerobs import Anaerobs

def main():
    print "Let's create new bacteria!"
    "This would create first object of Bacteria class"
    bacteria_1 = Bacteria("Ecola", "Escherichia Coli")

    "This would create second object of  bacteria class"
    bacteria_2 = Bacteria("Psea", "Pseudomonas aeruginosa")

    bacteria_1.displayName()
    bacteria_1.displaySpecies()

    anaerobBacteria = Anaerobs()
    anaerobBacteria.displayMetabolism()

    print "Total bacterial count: %d " % Bacteria.bacteriaCount

if __name__ == "__main__":
    main()