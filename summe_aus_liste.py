def main():
    zahlenliste =[6, 7.8, 9.4, 'hugo', 10, 11.5, 12.0, 13, 'test', 7.8]
    summe = 0.0

    for zahl in zahlenliste:
        try:
            float(zahl)
        except:
            continue
        else:
            summe += float(zahl)


    print(f'Es wurde {summe} berechnet.')



if __name__ == '__main__':
    main()