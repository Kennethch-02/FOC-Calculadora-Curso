from Class import *
# Clases que contienen las ventanas a utilizar

class Menu(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora FOC")
        self.main = main_window
        self.text = ttk.Label(self, text="Menu")
        self.text.grid(row=0,column=1)

        self.btn = ttk.Button(self,command= self.go_techo_numero, text="Techo->Numero")
        self.btn.grid(row=1,column=0)

        self.btn_1 = ttk.Button(self,command = self.go_numero_techo, text="Numero->Techo")
        self.btn_1.grid(row=1,column=1)

        self.btn_2 = ttk.Button(self,command = self.go_operaciones, text="Operaciones")
        self.btn_2.grid(row=1,column=2)

        self.btn_6 = ttk.Button(self,command = self.go_conversion, text="Conversion")
        self.btn_6.grid(row=2,column=0)

        self.btn_6 = ttk.Button(self,command = self.go_tablas_multiplicar, text="Tablas de Multiplicar")
        self.btn_6.grid(row=2,column=2)

        self.btn_3 = ttk.Button(self,command = self.go_metodo_resta, text="Metodo Resta")
        self.btn_3.grid(row=3,column=0)

        self.btn_4 = ttk.Button(self,command = self.go_metodo_suma, text="Metodo Suma")
        self.btn_4.grid(row=3,column=1)

        self.btn_5 = ttk.Button(self,command = self.go_numeros_magicos, text="Numeros Magicos")
        self.btn_5.grid(row=3,column=2)

        

        self.pack()

    def go_tablas_multiplicar(self):
        self.pack_forget()
        Tablas_de_Multiplicar(self.main)

    def go_techo_numero(self):
        self.pack_forget()
        Techo_Numero(self.main)

    def go_numero_techo(self):
        self.pack_forget()
        Numero_Techo(self.main)
    
    def go_operaciones(self):
        self.pack_forget()
        Operaciones(self.main)

    def go_metodo_resta(self):
        self.pack_forget()
        Metodo_Resta(self.main)
    
    def go_metodo_suma(self):
        self.pack_forget()
        Metodo_Suma(self.main)

    def go_numeros_magicos(self):
        self.pack_forget()
        Numeros_Magicos(self.main)

    def go_conversion(self):
        self.pack_forget()
        Conversiones(self.main)

class Numeros_Magicos(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora FOC - Metodo de la Resta")
        self.main = main_window
        self.text = ttk.Label(self, text="Numeros Magicos")
        self.text.grid(row=0, column=1)

        self.button = ttk.Button(self,command= self.go_main, text="Menu")
        self.button.grid(row=1, column=1)

        self.txt_baseI = ttk.Label(self, text="Digite la base Incial")
        self.txt_baseI.grid(row=3, column=0)

        self.entry_baseI = self.entry = ttk.Entry(self)
        self.entry_baseI.grid(row=3, column=2)

        self.txt_baseF = ttk.Label(self, text="Digite la base Final")
        self.txt_baseF.grid(row=4, column=0)

        self.entry_baseF = self.entry = ttk.Entry(self)
        self.entry_baseF.grid(row=4, column=2)

        self.txt_num = ttk.Label(self, text="Digite la cantidad de Numeros Magicos")
        self.txt_num.grid(row=5, column=0)

        self.entry_num = self.entry = ttk.Entry(self)
        self.entry_num.grid(row=5, column=2)

        self.btn_calc = ttk.Button(self,command= self.calc, text="Calcular")
        self.btn_calc.grid(row=6, column=1)

        self.t_result = tk.StringVar()
        self.t_result.set("Resultado = ")
        self.txt_result =  ttk.Label(self, textvariable=self.t_result)
        self.txt_result.grid(row=7, column=1)

        self.pack()

    def go_main(self):
        self.pack_forget()
        Menu(self.main)

    def calc(self):
        baseI = int(self.entry_baseI.get())
        baseF = int(self.entry_baseF.get())
        nums = int(self.entry_num.get())
        resultado = ""
        for i in range(nums):
            if(i != 0):
                resultado += "NM " + str(i) + " " + str((baseI**i)-(baseF**i)) + "\n"
        self.t_result.set(resultado)

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

class Metodo_Resta(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora FOC - Metodo de la Resta")
        self.main = main_window
        self.text = ttk.Label(self, text="Metodo de la Resta")
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
        numero = int(self.entry_cantidad.get())
        resultado = ""
        num = ""
        potencia = 0
        while 2**potencia < numero:
            potencia+=1
        potencia-=1
        while numero>0:
            if(numero>=2**potencia):
                resultado += "Potencia: " + str(potencia) + " Agregamos 1 y a " + str(numero) + " restamos " + str(2**potencia) + "\n"
                numero-=(2**potencia)
                num += " 1"
                potencia-=1
            else:
                resultado += "Potencia: " + str(potencia) + " Agregamos 0 porque " + str(numero) + " no es mayor que " + str(2**potencia) + "\n"
                num+=" 0"
                potencia-=1
        resultado += str(num)
        self.t_result.set(resultado)

class Metodo_Suma(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora FOC - Metodo de la Resta")
        self.main = main_window
        self.text = ttk.Label(self, text="Metodo de la Suma")
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
        numero = int(self.entry_cantidad.get())
        num = str(numero)
        resultado = ""
        int_result = 0
        for i in range(len(num)):
            if num[len(num)-1-i] == "1":
                int_result += 2**i
                resultado += "Como el digito es 1 se eleva a " + str(i) + " sumando " + str(2**i) + "\n"
            else:
                resultado += "Como la posicion " + str(i)+ " es cero se continua " + "\n"
        resultado += str(int_result)
        self.t_result.set(resultado)
        
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

class Conversiones(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora FOC - Conversiones")
        self.main = main_window
        self.text = ttk.Label(self, text="Conversiones")
        self.text.grid(row=0, column=1)

        self.button = ttk.Button(self,command= self.go_main, text="Menu")
        self.button.grid(row=1, column=1)
 
        self.txt_cantidad = ttk.Label(self, text="Digite el Numero y la baseI")
        self.txt_cantidad.grid(row=2, column=0)

        self.entry_cantidad = ttk.Entry(self)
        self.entry_cantidad.grid(row=2, column=1)

        self.entry_baseI = ttk.Entry(self)
        self.entry_baseI.grid(row=2, column=2)

        self.txt_BaseF = ttk.Label(self, text="Digite la Base Final")
        self.txt_BaseF.grid(row=3, column=0)

        self.entry_baseF = ttk.Entry(self)
        self.entry_baseF.grid(row=3, column=1)

        self.btn_div = ttk.Button(self,command= self.convertir, text="Calcular")
        self.btn_div.grid(row=4, column=1)

        self.t_result = tk.StringVar()
        self.t_result.set("Resultado = ")
        self.txt_result =  ttk.Label(self, textvariable=self.t_result)
        self.txt_result.grid(row=5, column=1)

        self.pack()

    def go_main(self):
        self.pack_forget()
        Menu(self.main)

    def convertir(self):
        list = []
        for n in self.entry_cantidad.get().split("-"):
            list.append(int(n))
        decimal = base_decimal(list,int(self.entry_baseI.get()))
        base = decimal_base(decimal, int(self.entry_baseF.get()))

        self.t_result.set(str(base))

class Tablas_de_Multiplicar(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora FOC - Tablas")
        self.main = main_window
        self.text = ttk.Label(self, text="Tablas de Mltiplicar")
        self.text.grid(row=0, column=1)

        self.button = ttk.Button(self,command= self.go_main, text= "Menu")
        self.button.grid(row=1, column=1)
 
        self.txt_base = ttk.Label(self, text="Digite la Base")
        self.txt_base.grid(row=3, column=0)

        self.entry_base = self.entry = ttk.Entry(self)
        self.entry_base.grid(row=3, column=2)

        self.txt_tabla = ttk.Label(self, text="Digite la Tabla")
        self.txt_tabla.grid(row=4, column=0)

        self.entry_tabla = self.entry = ttk.Entry(self)
        self.entry_tabla.grid(row=4, column=2)

        self.btn_calc = ttk.Button(self,command= self.calc, text="Calcular")
        self.btn_calc.grid(row=5, column=1)

        self.t_result = tk.StringVar()
        self.t_result.set("Resultado = ")
        self.txt_result =  ttk.Label(self, textvariable=self.t_result)
        self.txt_result.grid(row=6, column=1)

        self.pack()

    def go_main(self):
        self.pack_forget()
        Menu(self.main)

    def calc(self):
        resultado = ""
        base = int(self.entry_base.get())
        tabla = int(self.entry_tabla.get())
        for  i in range(base):
            multi = i*tabla
            resultado += str(i) + "x" + str(tabla) + " = " + str(decimal_base(multi, base)) + "\n"
        
        self.t_result.set(resultado)

main_window = tk.Tk()
app = Menu(main_window)
app.mainloop()
