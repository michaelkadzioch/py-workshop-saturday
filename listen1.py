def main():
    obstsalat = ['Orange', 'Zwiebel', 'Zucchini', 'Kapern', 'Spinat', 'Appel', 'Kartoffel', 'Brot']

    # Ausgabe der gesamten Liste
    print(obstsalat)

    # Ausgabe einer bestimmten Position
    print(obstsalat[3])
    print(obstsalat[-1])

    # Veränderung eines bestimmten Listenelementes
    print(obstsalat)
    obstsalat[3] = 'Banane'
    print(obstsalat)

    # Ausgabe der Elemente einzeln (for und range)
    for i in range(len(obstsalat)):
        print(obstsalat[i])

    # Ausgabe der Elemente einzeln (for und in)
    for obst in obstsalat:
        print(obst) 
        
    # Elemente hinzufügen
    print(obstsalat)
    obstsalat.append('Mais')
    obstsalat.append('Gurke')
    print(obstsalat)

    # Elemente entfernen
    print(obstsalat)
    obstsalat.remove('Kartoffel')
    print(obstsalat)

    # Elemente sortieren
    print(obstsalat)
    obstsalat.sort()
    print(obstsalat)


if __name__ == '__main__':
    main()