"""
Jonathan Ignacio Marley Ramirez
#2019200176 Examen de tercer parcial

Primer ejercicio
"""

import csv
from collections import Counter


class Persona:
    def __init__(self, nombre, apellido, edad, salario, deducciones, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)
        self.salario = int(salario)
        self.deducciones = int(deducciones)
        self.genero = genero


class ProcesadorCSV:
    def __init__(self, archivo):
        self.personas = self.cargar_datos(archivo)

    def cargar_datos(self, archivo):
        personas = []
        with open(archivo, 'r') as f:
            lector = csv.reader(f)
            next(lector)  # Saltar la cabecera
            for fila in lector:
                personas.append(Persona(*fila))
        return personas

    def persona_con_mayor_edad(self):
        return max(self.personas, key=lambda p: p.edad)

    def persona_con_menor_edad(self):
        return min(self.personas, key=lambda p: p.edad)

    def M_F(self):
        generos = Counter(p.genero for p in self.personas)
        return generos

    def promedio_salario(self):
        total_salario = sum(p.salario for p in self.personas)
        return total_salario / len(self.personas)

    def persona_con_mas_deducciones(self):
        return max(self.personas, key=lambda p: p.deducciones)

    def persona_con_mayor_salario(self):
        return max(self.personas, key=lambda p: p.salario)


# Uso del programa
proccess = ProcesadorCSV('archivo.csv')
print('Persona con mayor edad:', proccess.persona_con_mayor_edad().nombre)
print('Persona con menor edad:', proccess.persona_con_menor_edad().nombre)
print('Conteo de géneros:', proccess.M_F())
print('Promedio de salario:', proccess.promedio_salario())
print('Persona con más deducciones:',
      proccess.persona_con_mas_deducciones().nombre)
print('Persona con mayor salario:', proccess.persona_con_mayor_salario().nombre)