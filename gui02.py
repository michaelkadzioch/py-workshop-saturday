import tkinter

def btnAppClose_click():
    appWindow.destroy()    


def main():
    # Initialisiere ein neues Tkinter-Fenster.
    global appWindow
    appWindow = tkinter.Tk()
    appWindow.title('Meine erste GUI')
    appWindow.geometry('500x400')

    # Label
    label1 = tkinter.Label(appWindow, text='Das ist ein Label mit etwas Text')
    label1.pack()

    # Eingabefeld
    entrybox1 = tkinter.Entry(appWindow)
    entrybox1.pack()

    # Checkbutton
    cbox1Var = tkinter.BooleanVar()
    cbox1Var.set(False)
    cbox1 = tkinter.Checkbutton(appWindow, text='Checkbox', variable=cbox1Var)
    cbox1.pack()

    btnAppClose = tkinter.Button(appWindow, text='Schließen', command=btnAppClose_click)
    btnAppClose.pack()


    # App starten und Fenster als Loop offen halten.
    print('Hallo Welt!')
    appWindow.mainloop()
    print('Bye!')


if __name__ == '__main__':
    main()