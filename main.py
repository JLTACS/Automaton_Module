import tkinter as tk 
from tkinter import filedialog
import M1
import M2
import M3
import M4
import M5
import M6

class Gui():
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Find Reg Exp")
        self.root.resizable(0,0)
        self.process = None
        self.defaultbg = self.root.cget('bg')
        self.frame = tk.Frame(self.root,height=500, width = 800)
        
        self.et1 = tk.Label(self.root,text = "Ingrese Expresión Regular:",font='Arial 10 bold')
        self.reg_entry = tk.Entry(self.root)
        self.bttn1 = tk.Button(self.root,text = "File", command = self.regFile)

        self.et2 = tk.Label(self.root,text = "Archivo de entrada:",font='Arial 10 bold')
        self.file_entry = tk.Entry(self.root)
        self.bttn2 = tk.Button(self.root,text = "File", command = self.inputFile)
        self.bttn3 = tk.Button(self.root,text = "Start", command = lambda: self.process(self))

        self.load = tk.Text(self.root, height = 12, width = 30, bg=self.defaultbg, state='disabled')
        self.et3 = tk.Label(self.root,text = "Palabras Encontradas:",font='Arial 10 bold')
        self.finds = tk.Text(self.root, height = 35, width = 68, state='disabled')


        self.frame.grid(column = 0, row = 0)
        self.et1.place(x=50,y=30)
        self.reg_entry.place(x=50,y=50)
        self.bttn1.place(x=200,y=50)

        self.et2.place(x=50,y=90)
        self.file_entry.place(x=50,y=110)
        self.bttn2.place(x=200,y=110)
        self.bttn3.place(x=100,y=150)
        self.load.place(x=50, y = 220)
        self.et3.place(x = 280, y = 30)
        self.finds.place(x = 280, y = 50)
        
    def start(self):
        self.root.mainloop()

    def regFile(self):
        filename = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo",filetypes = (("text files","*.txt"),("all files","*.*")))
        f = open(filename, 'r')
        reg_exp = f.readline()
        self.reg_entry.delete(0, tk.END)
        self.reg_entry.insert(0, reg_exp[:-1])
        f.close()
    
    def inputFile(self):
        filename = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo",filetypes = (("text files","*.txt"),("all files","*.*")))
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, filename)
    
    def getProcess(self, function):
        self.process = function

def automaton(automat):
    #automat = Gui()
    index = 1.0

    automat.load.config(state='normal')
    automat.load.insert(str(index),"Inicializando...\n")
    index+=1
    exp = automat.reg_entry.get()
    automat.load.config(state='disabled')
    
    automat.load.config(state='normal')
    automat.load.insert(str(index),"Convirtiendo a posfijo...\n")
    index+=1
    pos_exp = M1.postfixNotation(exp)
    automat.load.config(state='disabled')

    automat.load.config(state='normal')
    automat.load.insert(str(index),"Creando AFN...\n")
    index+=1
    alf, matriz_Trans, init_st, final_st = M2.regularExpressionToNFA_e(pos_exp)
    automat.load.config(state='disabled')

    automat.load.config(state='normal')
    automat.load.insert(str(index),"Eliminando epsilon transiciones...\n")
    index+=1
    matriz_Trans, final_st, alf = M3.NFAconverter(alf,matriz_Trans,init_st,final_st)
    automat.load.config(state='disabled')

    automat.load.config(state='normal')
    automat.load.insert(str(index),"Convirtiendo AFN a AFD...\n")
    index+=1
    matriz_Trans, final_st = M4.afdConverter(matriz_Trans, final_st)
    automat.load.config(state='disabled')

    automat.load.config(state='normal')
    automat.load.insert(str(index),"Minimizando AFD...\n")
    index+=1
    matriz_Trans, final_st =  M5.Minimize(matriz_Trans, final_st)
    automat.load.config(state='disabled')

    automat.load.config(state='normal')
    automat.load.insert(str(index),"Parsing...\n")
    index+=1
    file = automat.file_entry.get()
    f = open(file, 'r')
    M6.parse(matriz_Trans,final_st,f,alf)
    f.close()
    automat.load.config(state='disabled')

    ind = 1.0
    f = open("resultados.txt",'r')
    automat.finds.config(state='normal')
    for rs in f:
        automat.finds.insert(str(ind),rs)
        ind+=1
    automat.finds.config(state='disabled')
    automat.load.config(state='normal')
    automat.load.insert(str(index),"Finish\n")
    automat.load.config(state='disabled')
    


def main():
    automat = Gui()
    automat.getProcess(automaton)
    automat.start()
    return 0

if __name__ == '__main__':
    main()




print("----M1------")
exp = "padre&*&*"
pos_exp = M1.postfixNotation(exp)
print(pos_exp)
print("\n")

print("----M2------")
alf, matriz_Trans, init_st, final_st = M2.regularExpressionToNFA_e(pos_exp)
M2.printTransTable(matriz_Trans,alf)
print("\n")

print("----M3------")
matriz_Trans, final_st, alf = M3.NFAconverter(alf,matriz_Trans,init_st,final_st)
M2.printTransTable(matriz_Trans, alf)
print("\n")

print("----M4------")
matriz_Trans, final_st = M4.afdConverter(matriz_Trans, final_st)
M2.printTransTable(matriz_Trans, alf)
print("\n")

print("----M5------")
matriz_Trans, final_st =  M5.Minimize(matriz_Trans, final_st)
M2.printTransTable(matriz_Trans, alf)
print("\n")

print("----M6------")
f = open("input.txt",'r')
M6.parse(matriz_Trans,final_st,f,alf)
f.close()
print("\n")