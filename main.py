import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext as st
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
        self.et3 = tk.Label(self.root,text = "Expresiones Encontradas:",font='Arial 10 bold')
        self.finds = tk.Text(self.root, height = 35, width = 68, state='disabled')
        self.bttn4 = tk.Button(self.root, text = "Guardar Encontrados", command = self.saveResults)
        
        self.bttn5 = tk.Button(self.root, text = "?", command = self.helpMe)
        self.bttn6 = tk.Button(self.root, text = "Ver Proceso", state = 'disabled', command = self.showProcess)

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
        self.bttn4.place(x = 600, y=450)
        self.bttn5.place(x = 725, y = 20)
        self.bttn6.place(x = 100, y = 365)

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
    
    def saveResults(self):
        filename = filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como")
        f = open(filename, 'w')
        rs = self.finds.get("1.0", tk.END)
        f.write(rs)
        f.close()
    
    def getProcess(self, function):
        self.process = function
    
    def errorMess(self, error_message):
        messagebox.showerror("Error", error_message)
    
    def helpMe(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Ayuda")
        help_window.resizable(0,0)
        lb_frame = tk.LabelFrame(help_window, text = "Instrucciones", height = 400, width = 500)
        # scroll = tk.Scrollbar(help_window)
        # scroll.place(x = 10, y = 350)
        inst = tk.Text(help_window, height = 33, width = 65, bg=self.defaultbg, state='normal')
        
        lb_frame.grid(column = 0, row = 0)
        inst.place(x=5,y=15)
        #scroll.config( command = inst.xview )

        f = open("instrucciones.txt",'r')
        index = 1.0
        for rd in f:
            inst.insert(str(index),rd)
            index += 1
        f.close()
        inst.config(state='disabled')
    
    def writeTransTable(self,Matrix, alphabet):

        keys = list(alphabet.keys())
        title = "\t"
        for k in keys:
            title += k + '\t'
        
        mat = ''
        for i in range(len(Matrix)):
            mat += (str(i) + '   ' + str(Matrix[i]) + '\n')
        
        return title, mat
    
    def showProcess(self):
        show_window = tk.Toplevel(self.root)
        show_window.title('Proceso')
        #show_window.resizable(0,0)
        frame = tk.Frame(show_window)
        xscrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
        pross = st.ScrolledText(frame, xscrollcommand = xscrollbar.set, width = 50, state='normal')
        bttn = tk.Button(frame, text = "Guardar Proceso", command = self.saveResults)

        # frame.grid(column = 0, row = 0,  sticky = tk.NSEW)
        # pross.grid(column = 0, row =0, sticky = tk.NSEW)
        # xscrollbar.grid(row=1, column=0, sticky = tk.NSEW)
        # bttn.grid(row = 2, column = 0)


        frame.pack(fill = tk.BOTH, expand = tk.YES)
        pross.pack(fill = tk.BOTH, expand = tk.YES)
        xscrollbar.pack(fill = tk.X)
        bttn.pack(pady = 10, padx = 10)

        # frame.columnconfigure(0, weight = 1)
        # frame.rowconfigure(0, weight = 1)

        f = open("temp_proc.txt", 'r')
        index = 1.0
        for rd in f:
            pross.insert(str(index),rd)
            index += 1
        f.close()
        pross.config(state='disabled')





def automaton(automat):
    #automat = Gui()
    wr = ''
    index = 1.0

    automat.load.config(state='normal')
    automat.load.delete("1.0",tk.END)
    automat.load.insert(str(index),"Inicializando...\n")
    index+=1
    exp = automat.reg_entry.get()
    automat.load.delete("1.0",tk.END)
    automat.load.config(state='disabled')
    if exp == "":
        automat.errorMess("Ingrese expresión regular!")
        return
    wr += ("Expresión Regular: " + exp + '\n')
    
    wr += '\n----------M1----------\n'
    automat.load.config(state='normal')
    automat.load.insert(str(index),"Convirtiendo a posfijo...\n")
    index+=1
    pos_exp = M1.postfixNotation(exp)
    wr += ("Expresión posfija: " + pos_exp + '\n')
    automat.load.config(state='disabled')

    wr += '\n----------M2 AFN-Epsilon----------\n'
    automat.load.config(state='normal')
    automat.load.insert(str(index),"Creando AFN...\n")
    index+=1
    alf, matriz_Trans, init_st, final_st = M2.regularExpressionToNFA_e(pos_exp)
    tl, mt = automat.writeTransTable(matriz_Trans,alf)
    wr += (tl + '\n' + mt + '\n')
    automat.load.config(state='disabled')

    wr += '\n----------M3 AFN----------\n'
    automat.load.config(state='normal')
    automat.load.insert(str(index),"Eliminando epsilon transiciones...\n")
    index+=1
    matriz_Trans, final_st, alf = M3.NFAconverter(alf,matriz_Trans,init_st,final_st)
    tl, mt = automat.writeTransTable(matriz_Trans, alf)
    wr += (tl + '\n' + mt + '\n')
    automat.load.config(state='disabled')

    wr += '\n----------M4 AFD----------\n'
    automat.load.config(state='normal')
    automat.load.insert(str(index),"Convirtiendo AFN a AFD...\n")
    index+=1
    matriz_Trans, final_st = M4.afdConverter(matriz_Trans, final_st)
    tl, mt = automat.writeTransTable(matriz_Trans, alf)
    wr += (tl + '\n' + mt + '\n')
    automat.load.config(state='disabled')

    wr += '\n----------M5 AFD Minimizado----------\n'
    automat.load.config(state='normal')
    automat.load.insert(str(index),"Minimizando AFD...\n")
    index+=1
    matriz_Trans, final_st =  M5.Minimize(matriz_Trans, final_st)
    tl, mt = automat.writeTransTable(matriz_Trans, alf)
    wr += (tl + '\n' + mt + '\n')
    automat.load.config(state='disabled')

    automat.load.config(state='normal')
    automat.load.insert(str(index),"Parsing...\n")
    index+=1
    file = automat.file_entry.get()
    if file == "":
        automat.errorMess("Ingrese archivo de entrada!")
        automat.load.delete("1.0",tk.END)
        return
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
    f.close()

    automat.load.config(state='normal')
    automat.load.insert(str(index),"Finish\n")
    automat.load.config(state='disabled')

    f = open("temp_proc.txt", 'w')
    f.write(wr)
    f.close()
    automat.bttn6.config(state = 'normal')


def main():
    automat = Gui()
    automat.getProcess(automaton)
    automat.start()
    return 0

if __name__ == '__main__':
    main()




# print("----M1------")
# exp = "padre&*&*"
# pos_exp = M1.postfixNotation(exp)
# print(pos_exp)
# print("\n")

# print("----M2------")
# alf, matriz_Trans, init_st, final_st = M2.regularExpressionToNFA_e(pos_exp)
# M2.printTransTable(matriz_Trans,alf)
# print("\n")

# print("----M3------")
# matriz_Trans, final_st, alf = M3.NFAconverter(alf,matriz_Trans,init_st,final_st)
# M2.printTransTable(matriz_Trans, alf)
# print("\n")

# print("----M4------")
# matriz_Trans, final_st = M4.afdConverter(matriz_Trans, final_st)
# M2.printTransTable(matriz_Trans, alf)
# print("\n")

# print("----M5------")
# matriz_Trans, final_st =  M5.Minimize(matriz_Trans, final_st)
# M2.printTransTable(matriz_Trans, alf)
# print("\n")

# print("----M6------")
# f = open("input.txt",'r')
# M6.parse(matriz_Trans,final_st,f,alf)
# f.close()
# print("\n")