import os
import sys

def getFileSize(filename):
    size = 0
    try:
        os.path.getsize(filename)
    except FileNotFoundError:
        return size
    else:
        size = os.path.getsize(filename)
        
    if size > 1024:
        return size / 1024

def main():
    sumOfSize = 0
    workdir = os.getcwd()

    if len(sys.argv) > 1:
        workdir = sys.argv[1]

    print(f'akuelles Verzeichnis: {workdir}')

    print(workdir)

    dirList = os.scandir(workdir)

    for entry in dirList:
        entryInfo = 'unkown'
        if entry.is_file():
            entryInfo = 'file'
            size = getFileSize(entry.name)
            print(f'{entryInfo:<7} | {size:>6} | {entry.name} ')
            sumOfSize += getFileSize(entry.name)
        elif entry.is_dir():
            entryInfo = 'dir'
            empty = '..'
            print(f'{entryInfo:<7} | {empty:>6} | {entry.name} ')

    print(f'Speichplatz insgesamt: {sumOfSize} Bytes')

        


if __name__ == '__main__':
    main()