import sys

def main():
    parameter1 = ''
    
    if len(sys.argv) > 1:
        parameter1 = sys.argv[1]

    print('hallo Welt!')
    print(parameter1)


if __name__ == '__main__':
    main()