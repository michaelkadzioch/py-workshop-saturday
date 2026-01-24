import tkinter
from tkinter import messagebox


def btnClose_click():
    if messagebox.askokcancel('Programm Beenden', 'Soll das Programm wirklich beendet werden?'):
        appWindow.destroy()



# def calculateMwst(value, mwst_value):
def calculateMwst():
    # global ebValue, cbMwstVar
    
    # Mwst-String formatieren und umwandeln
    mwstStr = cbMwstVar.get()
    mwstFloat = float(mwstStr.replace("%", "").strip())

    # Usereingabe prüfen und in Float umwandeln
    try:
        value = float(ebValue.get())
    except ValueError:
        messagebox.showerror('Fehler', 'Bitte eine gültige Zahl eingeben.')
        return
    else:
        # print('Mehrwertsteuer berechnen...', value * (1 + (mwstFloat / 100)))
        # Mehrwertsteuer berechnen und ausgeben
        labelOutput.config(text=f'Ergebnis: {value * (1 + (mwstFloat / 100)):.2f}')
        return 



def main():
    global appWindow
    appWindow = tkinter.Tk()
    appWindow.title('Mehrwertsteuer Berechnen')
    appWindow.geometry('500x200')

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

    global labelOutput
    labelOutput = tkinter.Label(appWindow, text='', font=('', 18))
    labelOutput.grid(row=1, column=0, padx=15, pady=15, sticky='w')

    btnCalculate = tkinter.Button(appWindow, text='Berechnen', command=calculateMwst)
    btnCalculate.grid(row=1, column=1, padx=15, pady=15, sticky='w')

    appWindow.mainloop()


if __name__ == '__main__': 
    main()