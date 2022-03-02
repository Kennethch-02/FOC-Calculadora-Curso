from tkinter import *
from tkinter import ttk
import tkinter as tk

diccionario = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,
               "I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,
               "Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,
               "Y":34,"Z":35}

def techo_numero(Letra, Techo):
    global diccionario
    numero = Techo*26+diccionario[Letra]
    return numero

def numero_techo(cantidad):
    global diccionario
    if cantidad >= 10:
        cantidad -= 10
        letra = cantidad%26+10
        techos = cantidad//26
        for element in diccionario:
            if diccionario[element]==letra:
                letra = element
        resultado = "Letra: " + str(letra) +" Techos: "+ str(techos)
        return resultado
    else:
        return cantidad

def suma_numeros(num1,num2,base):
    num1 = base_decimal(num1,base)
    num2 = base_decimal(num2,base)
    suma = num1+num2
    return decimal_base(suma,base)

def resta_numeros(num1,num2,base):
    num1 = base_decimal(num1,base)
    num2 = base_decimal(num2,base)
    resta = num1-num2
    return decimal_base(resta,base)

def multiplicacion_numeros(num1,num2,base):
    num1 = base_decimal(num1,base)
    num2 = base_decimal(num2,base)
    multi = num1*num2
    return decimal_base(multi,base)

def division_numeros(num1,num2,base):
    num1 = base_decimal(num1,base)
    num2 = base_decimal(num2,base)
    divi = num1/num2
    print(divi)
    return decimal_base(divi,base)

def decimal_base(num,base):
    result = []
    if num<0:
        result.append(-1)
        num=num*-1
    while num>0:
        result.append(num%base)
        num = num//base
    return list(reversed(result))

def base_decimal(num, base):
    resultado = 0
    for n in range(len(num)):
        pos = len(num)-n-1
        resultado += num[pos]*(base**n)
    return resultado