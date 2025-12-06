import requests

def main():
    # url = 'https://upload.wikimedia.org/wikipedia/commons/d/de/Nr_2_Berlin_Panorama_von_der_Siegess%C3%A4ule_2021.jpg'
    url = 'https://www.google.de'

    response = requests.get(url)

    print(response.status_code)




if __name__ == '__main__':
    main()