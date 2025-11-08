def readDataFromFile(filename):
    try:
        open(filename, 'rt')

    except:
        fileData = None

    else:
        with open(filename, 'rt') as file:
            fileData = file.read()
            
    return fileData



def calcSum(data):
    summe = 0.0

    for zahl in data:
        try:
            float(zahl)
        except:
            continue
        else:
            summe += float(zahl)
    return summe



# bouns
def writeDataToFile(filename, data):
    return



def main():
    inputFile = 'zahlenliste1.txt'

    fileData = readDataFromFile(inputFile)
    
    if fileData != None:
        summe = calcSum(fileData)
        print(f'Summe der Zahlen: {summe}')
    else:
        print(f'Fehler beim Lesen der Datei {inputFile}.')



if __name__ == '__main__':
    main()