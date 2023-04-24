# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 18:50:04 2022

@author: cjose
"""

from matplotlib import pyplot
from numpy import linspace

def cargar_datos(file):
    archivo = open(file, encoding="utf8")
    datos={}
    archivo.readline()
    for linea in archivo:
        l = linea.split(';')
        datos.append(l)
    archivo.close()
    return datos

datos = cargar_datos("chat.csv")

def lenr(datos):
    if datos:
        print(datos[0])
        return 1 + lenr(datos[1:])
    else:
        return 0
        
#print(lenr(datos))

#k = input("ingrese el valor de k")

        


def crear_d(datos):
    dic = {}
    datos = datos.split(";")
    for mensaje in datos:
        if mensaje not in datos:
            dic[mensaje] = 1
        else:
            dic[mensaje] += 1
    return datos    



     