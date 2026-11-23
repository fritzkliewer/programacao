from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys; 

peixes=["atum","tainha","anchova","bacalhau"]
selpeixes="Adicione os peixes que deseja:"

def select_items():
    tempeixes=False
    str=""
    for esc in escolha:
       if bool(esc.get()):
        str=str+peixes[escolha.index(esc)]+" "       
    if str!="":
     labsel.config(text="Peixes: "+ str)
    else:
     labsel.config(text=selpeixes)

def selection():
    labrad.config(text=f"Selected: {variable.get()}")


def return_pressed(event):
    label.config(text=event.widget.get())

def clique(event):
    messagebox.showinfo(title="mensagem", message="olá pessoal")

def acao_novo():
    messagebox.askokcancel("Novo arquivo", "Quer criar um novo arquivo?")
    print("Novo arquivo criado")

def quit(event):                    
    sys.exit() 

root = Tk()
root.geometry("600x500") 

menubar = Menu(root)
root.config(menu=menubar)

# 2. Cria um submenu (tearoff=0 remove a linha tracejada inicial)
menu_arquivo = Menu(menubar, tearoff=0)
menu_arquivo.add_command(label="Novo", command=acao_novo, accelerator="Ctrl+N")
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=root.quit)

# 3. Adiciona o submenu à barra principal
menubar.add_cascade(label="Arquivo", menu=menu_arquivo)

frm = ttk.Frame(root, padding=10)
frm.grid()

label=ttk.Label(frm, text="Olá pessoal!")
label.grid(column=0, row=0)

entry=ttk.Entry(frm, text="digite")
entry.bind("<Return>", return_pressed)
entry.grid(column=0, row=1)

botao = ttk.Button(frm, text='Clique aqui')
botao.bind('<Button-1>', clique)
botao.grid(column=0, row=2)

labsel = ttk.Label(frm, text=selpeixes)
labsel.grid(column=1, row=0, padx=10, pady=5, sticky="w")
labrad = ttk.Label(frm, text=peixes[0])
labrad.grid(column=2, row=0, padx=10, pady=5, sticky="w")

escolha=[]
variable = StringVar(root, f"{peixes[0]}")

for peixe in peixes:
 escolha.append( IntVar())
 index=len(escolha)-1
 chk=ttk.Checkbutton(frm,text=peixes[index],command=select_items,variable=escolha[index])
 chk.grid(column=1, row=1+index, padx=10, pady=5, sticky="w")
 ttk.Radiobutton(frm,text=peixe,variable=variable,value=peixe,command=selection,).grid(column=2, row=1+index, padx=10, pady=5, sticky="w")


canvas = Canvas(root, width=500, height=300, bg='white')

canvas.grid(column=0, row=5)   
canvas.create_line((50, 50), (100, 100), width=4, fill='red')
canvas.create_rectangle((100, 100), (300, 300), fill='green')
points = (
    (50, 150),
    (200, 350),
)
canvas.create_oval(*points, fill='purple')
points = (
    (100, 300),
    (200, 200),
    (300, 300),
)
canvas.create_polygon(*points, fill='blue')

canvas.create_text(
    (200, 100),
    text="Canvas Demo",
    fill="orange",
    font='tkDefaeultFont 24'
)

canvas.create_arc((10, 10), (200, 200), style=PIESLICE, width=2)
canvas.create_arc((10, 200), (200, 390), style=CHORD, width=2)
canvas.create_arc((10, 400), (200, 590), style=ARC, width=2)

python_image = PhotoImage(file='../char.png')
id =canvas.create_image(
    (100,100),
    image=python_image#.resize((50, 50))
)
#canvas.scale(id, 50, 50, 0.5, 0.5)

ttk.Button(frm, text="Sair", command=root.destroy).grid(column=0, row=3)
root.mainloop()
