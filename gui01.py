import tkinter

def btn1_click():
    print('Nicht klicken!')

def btn2_click():
    print('Klick auf den Button!')

def btnAppClose_click():
    appWindow.destroy()    

def main():
    # Initialisiere ein neues Tkinter-Fenster.
    global appWindow
    appWindow = tkinter.Tk()
    appWindow.title('Meine erste GUI')
    appWindow.geometry('500x400')

    btn1 = tkinter.Button(appWindow, text='das ist ein Button', command=btn1_click)
    # btn1['height'] = 3
    # btn1['width'] = 20
    # btn1['bg'] = '#ff0000'
    # btn1['fg'] = '#ffffff'
    btn1.pack()
    # btn1.place(x=100, y=200)

    btn2 = tkinter.Button(appWindow, text='das ist ein weiterer Button', command=btn2_click)
    btn2.pack()
    # btn2.place(x=300, y=200)

    btnAppClose = tkinter.Button(appWindow, text='Schließen', command=btnAppClose_click)
    btnAppClose.pack()


    # App starten und Fenster als Loop offen halten.
    print('Hallo Welt!')
    appWindow.mainloop()
    print('Bye!')


if __name__ == '__main__':
    main()