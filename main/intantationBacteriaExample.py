from model.Bacteria import Bacteria
from model.Aerobs import Aerobs
from model.Anaerobs import Anaerobs

def main():
    print "Let's create new bacteria!"

    "This would create first object of Bacteria class"
    bacteriaFirst = Bacteria("Ecola", "Escherichia Coli", "Yes")

    bacteriaFirst.displayName()
    bacteriaFirst.displaySpecies()
    bacteriaFirst.displayPathogenicity()

    "Instantiation inherited reference object "
    anaerobBacteria = Anaerobs()
    anaerobBacteria.displayMetabolism()

    print "Total bacterial count: %d " % Bacteria.bacteriaCount


if __name__ == "__main__":
    main()
