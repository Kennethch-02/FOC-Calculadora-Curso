from faulthandler import disable
from multiprocessing.context import set_spawning_popen

from black import main
from Class import *
# Clases que contienen las ventanas a utilizar

class Menu(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora FOC")
        self.main = main_window
        self.text = ttk.Label(self, text="Menu")
        self.text.pack()

        self.btn = ttk.Button(self,command= self.go_techo_numero, text="Techo->Numero")
        self.btn.pack(side=tk.LEFT)

        self.btn_1 = ttk.Button(self,command = self.go_numero_techo, text="Numero->Techo")
        self.btn_1.pack(side=tk.LEFT)

        self.btn_2 = ttk.Button(self,command = self.go_operaciones, text="Operaciones")
        self.btn_2.pack(side=tk.LEFT)

        self.pack()

    def go_techo_numero(self):
        self.pack_forget()
        Techo_Numero(self.main)

    def go_numero_techo(self):
        self.pack_forget()
        Numero_Techo(self.main)
    
    def go_operaciones(self):
        self.pack_forget()
        Operaciones(self.main)

class Techo_Numero(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main = main_window
        main_window.title("Calculadora FOC - Techo->Numero")

        self.text = ttk.Label(self, text="Techo->Numero")
        self.text.grid(row=0, column=1)

        self.button = ttk.Button(self,command= self.go_main, text="Menu")
        self.button.grid(row=1, column=1)
        
        self.txt_letra = ttk.Label(self, text="Digite la letra")
        self.txt_letra.grid(row=2, column=0)

        self.entry_letra = self.entry = ttk.Entry(self)
        self.entry_letra.grid(row=2, column=2)

        self.txt_techo = ttk.Label(self, text="Digite la cantidad de techos")
        self.txt_techo.grid(row=3, column=0)

        self.entry_techo = self.entry = ttk.Entry(self)
        self.entry_techo.grid(row=3, column=2)

        self.btn_calc = ttk.Button(self,command= self.calc, text="Calcular")
        self.btn_calc.grid(row=4, column=1)

        self.t_result = tk.StringVar()
        self.t_result.set("Resultado = ")
        self.txt_result =  ttk.Label(self, textvariable=self.t_result)
        self.txt_result.grid(row=5, column=1)

        self.pack()

    def go_main(self):
        self.pack_forget()
        Menu(self.main)

    def calc(self):
        Letra = self.entry_letra.get()
        Techo = int(self.entry_techo.get())
        self.t_result.set(techo_numero(Letra,Techo))

class Numero_Techo(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora FOC - Numero->Techo")
        self.main = main_window
        self.text = ttk.Label(self, text="Numero->Techo")
        self.text.grid(row=0, column=1)

        self.button = ttk.Button(self,command= self.go_main, text="Menu")
        self.button.grid(row=1, column=1)
 
        self.txt_cantidad = ttk.Label(self, text="Digite el Numero")
        self.txt_cantidad.grid(row=3, column=0)

        self.entry_cantidad = self.entry = ttk.Entry(self)
        self.entry_cantidad.grid(row=3, column=2)

        self.btn_calc = ttk.Button(self,command= self.calc, text="Calcular")
        self.btn_calc.grid(row=4, column=1)

        self.t_result = tk.StringVar()
        self.t_result.set("Resultado = ")
        self.txt_result =  ttk.Label(self, textvariable=self.t_result)
        self.txt_result.grid(row=5, column=1)

        self.pack()

    def go_main(self):
        self.pack_forget()
        Menu(self.main)

    def calc(self):
        self.t_result.set(numero_techo(int(self.entry_cantidad.get())))

class Operaciones(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora FOC - Operaciones")
        self.main = main_window
        self.text = ttk.Label(self, text="Operaciones")
        self.text.grid(row=0, column=1)

        self.button = ttk.Button(self,command= self.go_main, text="Menu")
        self.button.grid(row=1, column=1)
 
        self.txt_cantidad = ttk.Label(self, text="Digite el Primer Numero")
        self.txt_cantidad.grid(row=3, column=0)

        self.entry_cantidad = self.entry = ttk.Entry(self)
        self.entry_cantidad.grid(row=3, column=2)

        self.txt_cantidad_1 = ttk.Label(self, text="Digite el Segundo Numero")
        self.txt_cantidad_1.grid(row=4, column=0)

        self.entry_cantidad_1 = self.entry = ttk.Entry(self)
        self.entry_cantidad_1.grid(row=4, column=2)

        self.txt_base = ttk.Label(self, text="Digite la base")
        self.txt_base.grid(row=5, column=0)

        self.entry_base = self.entry = ttk.Entry(self)
        self.entry_base.grid(row=5, column=2)

        self.btn_sum = ttk.Button(self,command= self.suma, text="Suma")
        self.btn_sum.grid(row=6, column=0)

        self.btn_rest = ttk.Button(self,command= self.resta, text="Resta")
        self.btn_rest.grid(row=6, column=2)

        self.btn_mult = ttk.Button(self,command= self.multiplicacion, text="Multiplicar")
        self.btn_mult.grid(row=7, column=0)

        self.btn_div = ttk.Button(self,command= self.division, text="Division")
        self.btn_div.grid(row=7, column=2)

        self.t_result = tk.StringVar()
        self.t_result.set("Resultado = ")
        self.txt_result =  ttk.Label(self, textvariable=self.t_result)
        self.txt_result.grid(row=8, column=1)

        self.pack()

    def go_main(self):
        self.pack_forget()
        Menu(self.main)

    def suma(self):
        list_1 = []
        list_2 = []
        for n in self.entry_cantidad.get().split("-"):
            list_1.append(int(n))
        for i in self.entry_cantidad_1.get().split("-"):
            list_2.append(int(i))

        self.t_result.set(str(suma_numeros(list_1,list_2,int(self.entry_base.get()))))
        
    def resta(self):
        list_1 = []
        list_2 = []
        for n in self.entry_cantidad.get().split("-"):
            list_1.append(int(n))
        for i in self.entry_cantidad_1.get().split("-"):
            list_2.append(int(i))

        self.t_result.set(str(resta_numeros(list_1,list_2,int(self.entry_base.get()))))
    def multiplicacion(self):
        list_1 = []
        list_2 = []
        for n in self.entry_cantidad.get().split("-"):
            list_1.append(int(n))
        for i in self.entry_cantidad_1.get().split("-"):
            list_2.append(int(i))

        self.t_result.set(str(multiplicacion_numeros(list_1,list_2,int(self.entry_base.get()))))
    def division(self):
        list_1 = []
        list_2 = []
        
        for n in self.entry_cantidad.get().split("-"):
            list_1.append(int(n))
        for i in self.entry_cantidad_1.get().split("-"):
            list_2.append(int(i))

        self.t_result.set(str(division_numeros(list_1,list_2,int(self.entry_base.get()))))

main_window = tk.Tk()
app = Menu(main_window)
app.mainloop()