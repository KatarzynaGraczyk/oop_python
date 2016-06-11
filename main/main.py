from model.Bacteria import Bacteria
from model.Aerobs import Aerobs

def main():
    "Let's create new bacteria"

    bacteria = Bacteria("Ecola", "Escherichia Coli")

    bacteria.printName()
    bacteria.printSpecies()

    aerobBacteria = Aerobs()
    aerobBacteria.printMetabolism()

if __name__ == "__main__":
    main()