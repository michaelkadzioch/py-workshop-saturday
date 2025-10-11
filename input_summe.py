def main():
    summe = 0.0
    doNext = True


    while doNext:
        # alle Input sind Strings
        zahl = input('Geben Sie eine Zahl ein:  ')

        try:
            float(zahl)
        except:
            doNext = False
            print('Das war keine Zahl! Programm wird beendet.')
        else:    
            summe += float(zahl)
            userChoice =input('Weitere Zahl eingeben? (J/n):  ')

            if userChoice == 'n':
                doNext = False


    print(f'Es wurde einen Wert von {summe} berechnet.')



if __name__ == '__main__':
    main()