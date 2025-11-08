# Version mit Fehlererkennung

def main():
    filename = 'test1.txt'

    try:
        open(filename, 'rt')

    except:
        print(f'Es gab einen Fehler beim Öffnen der Datei {filename}.')

    else:
        with open(filename, 'rt') as file:
            fileData = file.read()
            print(fileData)


if __name__ == '__main__':
    main()