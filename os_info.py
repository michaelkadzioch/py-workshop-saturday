import os

def main(): 
    if os.name == 'nt':
        print('Das ist eine Windows-System.')
    elif os.name == 'posix':
        print('Linux-System.')
    else:
        print('Unbekanntes Betriebssystem.')

    print('Der Benutzername ist:', os.getlogin())    
    print('Der aktuelle Pfad ist:', os.getcwd())

    # Alle Umgebungsvariablen
    # print(os.environ)

    print('Der Name des Computer: ', os.environ['COMPUTERNAME'])


if __name__ == '__main__':
    main()