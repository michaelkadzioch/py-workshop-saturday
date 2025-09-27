def funtionMitReturn():
    text = 'Hallo aus der Funktion!'
    return text


def funtionMitParameter(text1, text2):
    output = f'{text1} aus der {text2}!'
    return output


def main():
    print('Hallo!')
    print(funtionMitReturn())
    print(funtionMitParameter('Guten Tag', 'Unterfunktion'))



if __name__ == '__main__':
    main()