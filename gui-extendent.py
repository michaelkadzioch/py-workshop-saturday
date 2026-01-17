import tkinter
from tkinter import messagebox


def btnClose_click():
    if messagebox.askokcancel('Programm Beenden', 'Soll das Programm wirklich beendet werden?'):
        appWindow.destroy()

def main():
    global appWindow
    appWindow = tkinter.Tk()
    appWindow.title('GUI mit Grid')
    appWindow.geometry('500x400')

    appWindow.columnconfigure(0, weight=1)
    appWindow.columnconfigure(1, weight=1)
   
    appWindow.rowconfigure(0, weight=1)
    appWindow.rowconfigure(1, weight=1)
    appWindow.rowconfigure(2, weight=1)

    btnClose = tkinter.Button(appWindow, text='Programm beenden', command=btnClose_click)
    btnClose.grid(row=2, column=1, padx=5, pady=5)

    appWindow.mainloop()


if __name__ == '__main__': 
    main()