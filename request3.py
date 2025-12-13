import requests

def main():
    url = 'https://upload.wikimedia.org/wikipedia/commons/d/de/Nr_2_Berlin_Panorama_von_der_Siegess%C3%A4ule_2021.jpg'
    headers = {'user-agent': 'hugo-bot/1.0'}
    filename = 'downloaded_image.jpg'

    response = requests.get(url, headers=headers)

    print(response.status_code)

    # print(response.text)
    with open(filename, 'wb') as file:
            file.write(response.content)




if __name__ == '__main__':
    main()