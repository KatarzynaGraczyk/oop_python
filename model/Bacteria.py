class Bacteria:
    _name = ""

    def __init__(self, name):
        self._name = name

    def printName(self):
        print "My name is: " + self._name