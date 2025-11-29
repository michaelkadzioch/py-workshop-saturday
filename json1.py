import json

def main():
    filename = 'datensatz.json'

    # Bei Lesen Datei wird JSON als String gelesen.
    with open(filename, 'r') as file:
        fileData = file.read()

    # JSON-String wird in ein Python-Dict umgewandelt.
    jsonData = json.loads(fileData)

    key = 'name'

    if key in jsonData:
        print(jsonData[key])
    else:
        print('Daten nicht vorhanden.')

if __name__ == '__main__':
    main()