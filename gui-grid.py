import tkinter
from tkinter import messagebox


def main():
    # Initialisiere ein neues Tkinter-Fenster.
    global appWindow
    appWindow = tkinter.Tk()
    appWindow.title('GUI mit Grid')
    appWindow.geometry('500x400')

    # Grid Layout
    # Konfiguriere Spalten
    appWindow.columnconfigure(0, weight=1)
    appWindow.columnconfigure(1, weight=1)
    # Konfiguriere Zeilen
    appWindow.rowconfigure(0, weight=1)
    appWindow.rowconfigure(1, weight=1)
    appWindow.rowconfigure(2, weight=1)

    # Buttons definieren
    btn1 = tkinter.Button(appWindow, text='Button 1', bg='limegreen')
    btn2 = tkinter.Button(appWindow, text='Button 2', bg='limegreen')
    btn3 = tkinter.Button(appWindow, text='Button 3', bg='limegreen')
    btn4 = tkinter.Button(appWindow, text='Button 4', bg='limegreen')
    btn5 = tkinter.Button(appWindow, text='Button 5', bg='limegreen', font=('Arial', 36, 'bold'))


    # Buttons positionieren
    btn1.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    btn2.grid(row=0, column=1, padx=5, pady=5, sticky='ns')
    btn3.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
    btn4.grid(row=1, column=1, padx=5, pady=5)
    btn5.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky='ew')


    appWindow.mainloop()


if __name__ == '__main__':
    main()