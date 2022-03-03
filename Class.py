from tkinter import *
from tkinter import ttk
import tkinter as tk

diccionario = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,
               "I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,
               "Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,
               "Y":24,"Z":25}

def techo_numero(Letra, Techo):
    global diccionario
    numero = Techo*26+diccionario[Letra]
    return numero

def numero_techo(cantidad):
    global diccionario
    if cantidad >= 10:
        cantidad -= 10
        letra = cantidad%26
        techos = cantidad//26
        for element in diccionario:
            if diccionario[element]==letra:
                letra = element
        resultado = "Letra: " + str(letra) +" Techos: "+ str(techos) + "\n"
        resultado += str(diccionario)
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