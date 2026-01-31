class MyClass:
    a = 5
    b = 7 

    def summe(self):
        return self.a + self.b


def main():
    print('Python mit Klassen und Objekten')

    object1 = MyClass()
    object2 = MyClass()

    print(object1.a)
    print(object2.a)

    print(object1.summe())


if __name__ == '__main__':
    main()