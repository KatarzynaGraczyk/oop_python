import os
os.chdir('..')
directory = os.getcwd()
import sys
sys.path.insert(1, f'{directory}')
from modelToParseFile.parseFileBacteriaList import parseFileBacteriaList

def main():
    print("Let's parse file")
    bacteriaList = parseFileBacteriaList('bacteriaList')

    bacteriaList.readFile()

if __name__ == '__main__':
    main()
