def main():
    # Textdatei zu lesen öffnen
    file = open('test1.txt', 'rt')

    # Daten aus Daten lesen
    fileData = file.read()

    print(fileData)

    file.close()



if __name__ == '__main__':
    main()