# Importerar tkinter
from tkinter import *
# Importerar popup-fönster som jag använder för att visa användaren ifall den skrivt rätt eller fel lösenord
from tkinter import messagebox

# Skapar ett fönster i genom konstanten w
w = Tk()
# Ändrar storleken på fönstret
w.geometry('350x500')
# Ändrar namn på fönstret
w.title('Logga in')
# Tar bort fullscreen knappen eftersom GUI'n inte får plats i fullscreen
w.resizable(0, 0)

# Skapar en bakgrund med en blå toning
j = 0
r = 10
for i in range(100):
    c = str(222222 + r)
    Frame(w, width=10, height=500, bg="#" + c).place(x=j, y=0)
    j = j + 10
    r = r + 1

# Skapar en vit ruta och modifierar storlek, färg och position
Frame(w, width=250, height=400, bg='white').place(x=50, y=50)

# Skriver ut texten "användarnamn" över rutan man skriver in det
l1 = Label(w, text='Användarnamn', bg='white')
l = ('Consolas', 13)
l1.config(font=l)
l1.place(x=80, y=200)

# Skapar en Entry funktion som låter användaren skriva in sitt användarnamn, ändrar även fonten på texten som skrivs in för att matcha resten av systemet
e1 = Entry(w, width=20, border=0)
l = ('Consolas', 13)
e1.config(font=l)
e1.place(x=80, y=230)

# Skapar en Entry funktion som låter användaren skriva in sitt lösenord, ändrar även fonten på texten som skrivs in för att matcha resten av systemet
e2 = Entry(w, width=20, border=0, show='*')
e2.config(font=l)
e2.place(x=80, y=310)

# Skriver ut texten "Lösenord" över rutan man skriver in det
l2 = Label(w, text='Lösenord', bg='white')
l = ('Consolas', 13)
l2.config(font=l)
l2.place(x=80, y=280)

# Skapar en linje under användernamnet och lösenordet för att snygga till inloggningssystemet
Frame(w, width=180, height=2, bg='#141414').place(x=80, y=332)
Frame(w, width=180, height=2, bg='#141414').place(x=80, y=252)

# Importerar PIL (Pillow) som används för att öppna, manipulera och spara bilder
from PIL import ImageTk, Image

# Refererar till bilden inloggning.png och skapar en lable (ruta) som den ska placeras i
imageA = Image.open("inloggning.png")
imageB = ImageTk.PhotoImage(imageA)

label1 = Label(image=imageB,
               border=0,

               justify=CENTER)

label1.place(x=115, y=50)


# Skapar ett nytt fönster där man får veta om man har använt rätt lösenord och användarnamn
def cmd():
    if e1.get() == 'Linus' and e2.get() == '12345678':
        messagebox.showinfo("INLOGGNINGEN LYCKADES", "         Välkomen till banken        ")
        q = Tk()
        q.mainloop()

    else:
        messagebox.showwarning("INLOGGNINGEN MISSLYCKADES", "        Fel lösenord, försök igen        ")


# Gör så att logga in knappen ändrar färg när man placerar muspekaren över den för att förtydligöra att man kan trycka på den
def bttn(x, y, text, ecolor, lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor  # ffcc66
        myButton1['foreground'] = lcolor  # 000d33

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground'] = ecolor

    myButton1 = Button(w, text=text,
                       width=20,
                       height=2,
                       fg=ecolor,
                       border=0,
                       bg=lcolor,
                       activeforeground=lcolor,
                       activebackground=ecolor,
                       command=cmd)

    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x, y=y)


bttn(100, 375, 'Logga in', 'white', '#994422')

# Säger till python att köra 'Tkinter event loop' som kollar varsen man har tryckt på en knapp i programmet eller till exempel stängt programmet
w.mainloop()