# Verkürzte Version

def main():
    # Textdatei zu lesen öffnen
    with open('test1.txt', 'rt') as file:
        # Daten aus Daten lesen
        fileData = file.read()

        print(fileData)


if __name__ == '__main__':
    main()