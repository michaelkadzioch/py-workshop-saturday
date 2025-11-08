# Datei neu erstellen und schreiben

def main():
    filename = 'test_output.txt'
    newContent = 'Das ist ein neuer Inhalt.'

    try:
        open(filename, 'xt')

    except:
        print(f'Es gab einen Fehler beim Öffnen der Datei {filename}.')

    else:
        with open(filename, 'wt') as file:
            file.write(newContent)


if __name__ == '__main__':
    main()