from tkinter import *
from captura import Captura
from scapy.all import *

root_window = Tk()
root_window.configure(background='aliceblue')
root_window.title('Clona Wireshark')
root_window.geometry('400x400')

filtru = StringVar(root_window)
filtru.set("")


def captura_pachete_filtrate():
    if filtru.get()=="":
        raise Exception("No filter applied")
    else:
        pachete = sniff(count=10, filter= filtru.get())
        for pachet in pachete:
            print(pachet.show())
        filtru.set("")
    print("/n")


entry_filtru = Entry(root_window,
              textvariable=filtru)
buton_captura = Captura()

buton_start = Button(root_window,
                    text='Start capture',
                    font=('ComicSans MS', 12),
                    background='cornflowerblue',
                    foreground='white',
                    command=buton_captura.captura_pachete
                     )

buton_grafic = Button(root_window,
                        text='Show statistics',
                       font=('ComicSans MS', 12),
                       background='cornflowerblue',
                       foreground='white',
                       command=buton_captura.grafic_pachete
                     )
buton_salvare_json= Button(root_window,
                       text='Save as JSON',
                       font=('ComicSans MS', 12),
                       background='cornflowerblue',
                       foreground='white',
                       command=buton_captura.salvare_json
                           )
buton_filtru = Button(root_window,
                       text='Filter',
                       font=('ComicSans MS', 12),
                       background='cornflowerblue',
                       foreground='white',
                       command=captura_pachete_filtrate
                      )

buton_start.place(x=10, y=200)
buton_grafic.place(x=10,y=240)
buton_salvare_json.place(x=10, y=280)
entry_filtru.place(x= 180,y=205)
buton_filtru.place(x=320, y=200)

root_window.mainloop()
