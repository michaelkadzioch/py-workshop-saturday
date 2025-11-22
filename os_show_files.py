import os

def main():
    sumOfSize = 0
    print(f'akuelles Verzeichnis: {os.getcwd()}')

    dirList = os.scandir('.')

    for entry in dirList:
        entryInfo = 'unkown'
        if entry.is_file():
            entryInfo = 'file'
            print(f'{entryInfo:<7} | {os.path.getsize(entry.name):>6} | {entry.name} ')
            sumOfSize += os.path.getsize(entry.name)
        elif entry.is_dir():
            entryInfo = 'dir'
            empty = '..'
            print(f'{entryInfo:<7} | {empty:>6} | {entry.name} ')

    print(f'Speichplatz insgesamt: {sumOfSize} Bytes')

        


if __name__ == '__main__':
    main()