class parseFileBacteriaList:
    'Class for read and print information from text file'
    bacteriaName = []
    fileName = ""

    def __init__(self,fileName):
        self.fileName = fileName

    def readFile(self):
        file = open(self.fileName).readlines()
        listBacteria = []
        listDeseases = []
        for linia in file:
            line = linia.split("\t")
            listBacteria.append(line[0])
            listDeseases.append(line[1])
        print(listBacteria)
        print(listDeseases)