def main():
    # Zahlen
    zahl = 10

    print(zahl)
    print(type(zahl))


    # listen
    liste = [1, 2, 3, 4, 5, 'hugo', 7.8, 8.5, 9.0, 'banana', 'test']

    print(liste)
    print(type(liste))

    print(liste[5])
    print(type(liste[5]))

    # dictionary (JSON-Format)
    dictionary = {'name': 'Hugo', 
                  'alter': 30, 
                  'geschlecht': 'männlich'}
    
    print(dictionary)
    print(type(dictionary))

    print(dictionary['name'])
    print(type(dictionary['name']))




if __name__ == '__main__':
    main()