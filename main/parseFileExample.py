from modelToParseFile.parseFileBacteriaList import parseFileBacteriaList

def main():
    print "Let's parse file"

    bacteriaList = parseFileBacteriaList("/home/kasia/projects/oop_python/bacteriaList")
    bacteriaList.readFile()

if __name__ == '__main__':
    main()
