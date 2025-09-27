def main():
    print('Hallo das ist eine Ausgabe.')

    outputText = 'Das ist eine Ausgabe aus einer Variablen.'
    print(outputText)

    print('Das', 'ist', 'ein', 'Beispiel', 'aus', 'einer', 'Ausgabe.')

    a = 'Test'
    b = 'Ausgabe'

    print(a, b)

    # print mit Separator
    print('Das', 'ist', 'ein', 'Beispiel', 'aus', 'einer', 'Ausgabe.', sep = '-')
    print(a, b, sep = '-')

    z1 = '5'
    z2 = '10'
    z3 = '5.0'
    z4 = '7.9'

    print(z1, z2, z3, z4)
    
    print(z1, z2, z3, z4, sep = ' | ', end = ' #\n')
    print(z1, z2, z3, z4, sep = ' | ', end = ' #\n')
    print(z1, z2, z3, z4, sep = ' | ', end = ' #\n')
    print(z1, z2, z3, z4, sep = ' | ', end = ' #\n')



if __name__ == '__main__':
    main()