def main():
    # alle Input sind Strings
    zahl = input('Geben Sie eine Zahl ein:  ')

    # Prüfen, ob die Eingabe eine Zahl ist
    try:
        float(zahl)
    except:
        print('Das war keine Zahl!')
    else:  
        print(10.0 + float(zahl))


if __name__ == '__main__':
    main()