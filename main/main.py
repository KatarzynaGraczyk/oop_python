from model.Bacteria import Bacteria

def main():
    print "Let's create new bacteria"

    bacteria = Bacteria("Escherichia")

    bacteria.printName()


if __name__ == "__main__":
    main()