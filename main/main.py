from model.Bacteria import Bacteria
from model.Aerobs import Aerobs
from model.Anaerobs import Anaerobs

def main():
    "Let's create new bacteria"

    bacteria = Bacteria("Ecola", "Escherichia Coli")

    bacteria.printName()
    bacteria.printSpecies()

    anaerobBacteria = Anaerobs()
    anaerobBacteria.printMetabolism()

if __name__ == "__main__":
    main()