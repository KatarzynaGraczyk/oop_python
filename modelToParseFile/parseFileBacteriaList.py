class parseFileBacteriaList:
    'Class for read and print information from text file'
    bacteriaName = []
    fileName = ""

    def __init__(self,fileName):
        self.fileName = fileName

    def readFile(self):
        file = open(self.fileName).readlines()
        for linia in file:
            print linia