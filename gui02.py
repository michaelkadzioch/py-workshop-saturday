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

    # Radiobuttons
    radioVar = tkinter.StringVar()
    radioVar.set('Option 1 gewählt')

    radio1 = tkinter.Radiobutton(appWindow, text='Option 1', variable=radioVar, value='Option 1 gewählt')
    radio1.pack()
    radio2 = tkinter.Radiobutton(appWindow, text='Option 2', variable=radioVar, value='Option 2 gewählt')
    radio2.pack()
    radio3 = tkinter.Radiobutton(appWindow, text='Option 3', variable=radioVar, value='Option 3 gewählt')
    radio3.pack()

    # Combobox
    combobox1Var = tkinter.StringVar()
    combobox1Var.set('Option 1')

    combobox1 = tkinter.OptionMenu(appWindow, combobox1Var, 'Option 1', 'Option 2', 'Option 3')
    combobox1.pack()


    # App starten und Fenster als Loop offen halten.
    print('Hallo Welt!')
    appWindow.mainloop()
    print('Bye!')


if __name__ == '__main__':
    main()