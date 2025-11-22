import os

def checkFile(filename):
    if os.path.exists(filename):
        if os.path.isfile(filename):
            return True
        else:
            return False
    else:
        return False


def main():
    outputFile = 'output.log'
    outputText = 'Das ist der Inhalt für die neue Datei.'

    if checkFile(outputFile):
        userInput = input('Soll die Datei überschrieben werden (j/n)?')
        if userInput.lower() == 'j':
            with open(outputFile, 'wt') as file:
                file.write(outputText)
        else:
            with open(outputFile, 'at') as file:
                file.write(outputText)
    else:
        with open(outputFile, 'xt') as file:
            file.write(outputText)



if __name__ == '__main__':
    main()    