from model.Bacteria import Bacteria
from model.Aerobs import Aerobs

def main():
    print "Let's create new bacteria"

    bacteria = Bacteria("Escherichia", "Coli")

    bacteria.printName()
    bacteria.printSpecies()

    aerobBacteria = Aerobs()
    aerobBacteria.printMetabolism()

if __name__ == "__main__":
    main()