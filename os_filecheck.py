import os

def main(): 
    filename = 'test1.txt'

    if os.path.exists(filename):
        print(f'{filename} existiert.')

        if os.path.isfile(filename):
            print(f'{filename} ist ein Datei.')
            print(f'Dateigröße: {os.path.getsize(filename)} Bytes.')
        else:
            print(f'{filename} ist keine Datei.')

    else:
        print(f'{filename} existiert nicht.')

if __name__ == '__main__':
    main()