import requests

def main():
    url = 'https://www.tagesschau.de/api2u/homepage/'

    response = requests.get(url)

    print(response.status_code)
    #print(response.text)

    data = response.json()
    # print(type(data))

    news = data['news']
    for element in news:
        print('--------')
        print(element['date'])
        print(element['title'])
        print(element['topline'])


if __name__ == '__main__':
    main()