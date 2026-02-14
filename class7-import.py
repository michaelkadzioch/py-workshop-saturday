import class6 as geometrie

def main():
    rechteck = geometrie.Rechteck(0, 0)
    kreis = geometrie.Kreis(0)
    
    laenge = 0
    breite = 0
    radius = 0

    laenge = input('Geben Sie die Länge des Rechtecks ein: ')
    rechteck.setA(laenge)

    breite = input('Geben Sie die Breite des Rechtecks ein: ')
    rechteck.setB(breite)

    radius = input('Geben Sie den Radius des Kreises ein: ')
    kreis.setRadius(radius)



    if not kreis.getError() and not rechteck.getError():
        print(f'Kreisfläche: {kreis.flaeche():.3f}')
        print(f'Rechteckfläche: {rechteck.flaeche():.3f}')
        print(f'Kreisumfang: {kreis.umfang():.3f}')
        print(f'Rechteckumfang: {rechteck.umfang():.3f}')
    
    else:
        print('Es sind Fehler bei der Eingabe')


if __name__ == '__main__':
    main()