# F-Strings in print() nutzen
def main():
    preis = 49.95
    artikel = 'T-Shirt'

    # Ausgabe nur mit print()
    print('Der Preis beträgt:', preis)
    print('Das T-Shirt kostet', preis, 'Euro.')

    # Ausgabe mit F-String
    print(f'Der Preis beträgt: {preis} Euro.')
    print(f'Das T-Shirt kostet {preis} Euro.')
    print(f'Das {artikel} kostet {preis + 5.0} Euro.')

    output = f'Das {artikel} kostet {preis} Euro.'
    print(output)



if __name__ == '__main__':
    main()