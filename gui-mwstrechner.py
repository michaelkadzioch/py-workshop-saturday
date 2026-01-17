import tkinter
from tkinter import messagebox


def btnClose_click():
    if messagebox.askokcancel('Programm Beenden', 'Soll das Programm wirklich beendet werden?'):
        appWindow.destroy()

# def calculateMwst(value, mwst_value):
def calculateMwst():
    # global ebValue, cbMwstVar
    print('Mehrwertsteuer berechnen...', ebValue.get(), cbMwstVar.get())

def main():
    global appWindow
    appWindow = tkinter.Tk()
    appWindow.title('Mehrwertsteuer Berechnen')
    appWindow.geometry('500x400')

    appWindow.columnconfigure(0, weight=1)
    appWindow.columnconfigure(1, weight=1)
   
    appWindow.rowconfigure(0, weight=1)
    appWindow.rowconfigure(1, weight=1)
    appWindow.rowconfigure(2, weight=1)

    btnClose = tkinter.Button(appWindow, text='Programm beenden', command=btnClose_click)
    btnClose.grid(row=2, column=1, padx=15, pady=15, sticky='w')


    global ebValue
    ebValue = tkinter.Entry(appWindow, font=('', 18))
    ebValue.grid(row=0, column=0, padx=15, pady=5, sticky='w')  

    global cbMwstVar
    cbMwstVar = tkinter.StringVar()
    cbMwstVar.set('19 %')

    cbMwst = tkinter.OptionMenu(appWindow, cbMwstVar, '0 %', '7 %', '19 %')
    cbMwst.grid(row=0, column=1, padx=15, pady=15, sticky='w')

    btnCalculate = tkinter.Button(appWindow, text='Berechnen', command=calculateMwst)
    btnCalculate.grid(row=1, column=0, padx=15, pady=15, sticky='e')

    appWindow.mainloop()


if __name__ == '__main__': 
    main()