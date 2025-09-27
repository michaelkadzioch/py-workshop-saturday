def main():
    text = 'Das ist eine Ausgabe'
    zahl = '7.9'
    falscheZahl = 'Test'

    print(text)
    print(zahl)

    # Konvertiere die Zahl in einen Float
    print(5.0 + float(zahl))

    # Error beim Konvertieren einer ungültigen Zahl
    # print(5.0 + float(falscheZahl))
    
    # Exeption wird geworfen, da die Zahl nicht konvertierbar ist
    # Versuch zu konvertieren
    try:
        float(falscheZahl)
    # Ensteht ein Fehler bei der Konvertierung?
    except:
        print('Fehler beim Konvertieren der Zahl')
    # Wenn keine Fehler aufgetreten ist, führe Code aus    
    else:
        print(5.0 + float(falscheZahl))
   


if __name__ == "__main__":
    main()