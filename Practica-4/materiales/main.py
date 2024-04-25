'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

from avl_tree import AVL
from curso import Curso
from clase_pandas import Pandas
from sys import argv
from time import sleep

class SimuladorCursos:
    '''
    Clase del simulador de gestión de cursos, que extrae información de un string 
    y la convierte en cursos, añadiéndolas a un árbol.

    Methods
    -------
    crear_arbol_cursos(self, texto:str) -> AVL:
        Permite leer dos archivos de texto con la información de las los cursos
        que se quieren organizar y los mete en dos árboles A y B respectivamente.
    
    oferta_agregada(self) -> AVL:
        Agrega los cursos realizados por cada una de las academias a un árbol común.
    
    oferta_comun(self) -> AVL:
        Agrega los cursos realizados únicamente en ambas academias a un árbol común.
    
    opcion_leer_archivos(self) -> bool:
        Permite elegir entre leer o no leer los ficheros de texto.
    '''

    def __init__(self) -> None:
        '''
        Método que asigna atributos al objeto.

        Returns
        -------
        None
        '''
        self._arbol_A = AVL()
        self._arbol_B = AVL()
        self._arbol_agregado = AVL()
        self._arbol_comun = AVL()
        self._agregado = False
        self._comun = False


    def crear_arboles_cursos(self) -> tuple[AVL,AVL]:
        '''
        Método que permite leer dos archivos de texto con la información de las los cursos
        que se quieren organizar y los mete en dos árboles A y B respectivamente.

        Returns
        -------
        tuple[AVL,AVL]
         Tupla de los dos árboles de cursos.
        '''
        
        with open(argv[1], 'r', encoding='utf-8') as archivoA:
            texto1: str = archivoA.read()
            lineas = str(texto1).split('\n') # Leemos el archivo
            
            for linea in lineas[1:len(lineas) - 1]:
                partes_linea = str(linea).split(',')

                nombre      = str(partes_linea[0])
                duracion    = int(partes_linea[1])
                estudiantes = int(partes_linea[2])
                nivel       = str(partes_linea[3])
                idioma      = str(partes_linea[4])
                precio      = float(partes_linea[5])

                cursoA = Curso(nombre, duracion, estudiantes, nivel, idioma, precio)
                
                self._arbol_A[cursoA.clave] = cursoA

        with open(argv[2], 'r', encoding='utf-8') as archivoB:
            texto2: str = archivoB.read()
            lineas = str(texto2).split('\n')
            
            for linea in lineas[1:len(lineas) - 1]:
                partes_linea = str(linea).split(',')

                nombre      = str(partes_linea[0])
                duracion    = int(partes_linea[1])
                estudiantes = int(partes_linea[2])
                nivel       = str(partes_linea[3])
                idioma      = str(partes_linea[4])
                precio      = float(partes_linea[5])

                cursoB = Curso(nombre, duracion, estudiantes, nivel, idioma, precio)
                
                self.arbol_B[cursoB.clave] = cursoB

        return (self.arbol_A, self.arbol_B)
    
    
    def oferta_agregada(self) -> None:
        '''
        Método que agrega los cursos realizados por cada una de las academias a un árbol común.
        
        Returns
        -------
        None
        '''
        for curso_A in self.arbol_A.values():
            curso_A: Curso
            for curso_B in self.arbol_B.values():
                curso_B: Curso
                
                if curso_A == curso_B:

                    if curso_A.beneficio >= curso_B.beneficio:
                        curso_A.estudiantes += curso_B.estudiantes
                        self.arbol_agregado[curso_A.clave] = curso_A
                    
                    else:
                        curso_B.estudiantes += curso_A.estudiantes
                        self.arbol_agregado[curso_B.clave] = curso_B
                
                else:
                    self.arbol_agregado[curso_A.clave] = curso_A


    def oferta_comun(self) -> None:
        '''
        Método que agrega los cursos realizados únicamente en ambas academias a un árbol común.
        
        Returns
        -------
        None
        '''
        for curso_A in self.arbol_A.values():
            curso_A: Curso
            for curso_B in self.arbol_B.values():
                curso_B: Curso
                
                if curso_A == curso_B:
                    return
    
    
    def opcion_leer_archivos(self) -> bool:
        '''
        Método que permite elegir entre leer o no leer los ficheros de texto.
        
        Returns
        -------
        bool
         True si se decide leer los archivos.
         False si se decide no leer los archivos.
        '''
        linea = '-'*50
        texto = '¿Leer ficheros de los cursos A y B? (S/N)'
        
        print(f'\n{linea}\n\n{texto}\n\n{linea}')
        
        while True:
            eleccion = str(input('\nResponde aquí: '))
            
            if eleccion.upper() == 'S':
                print(f'\n{linea}\n\n  Leyendo ficheros...\n')
                sleep(0.25)
                return True
            
            elif eleccion.upper() == 'N':
                print(f'\n{linea}\n\n  Saliendo...\n')
                return False
            
            else:
                print(f'\n  Respuesta no válida.\n\n{linea}')
        
        
    def menu(self) -> None:
        '''
        Método que imprime por pantalla el menú de opciones para navegar entre los cursos y le permite escoger
        a un usuario entre 3 opciones de visualización/filtrado, además de la opción de poder salir del menú.
        
        Returns
        -------
        None
        '''
        linea = '-'*50
        
        menu  = f'\n{linea}'
        menu += '\nA - Realizar la operación "oferta agregada"'
        menu += '\nB - Realizar la operación "oferta común"'
        menu += '\nC - Mostrar estadísticas'
        menu += '\n\nQ - Salir del menú'
        menu += f'\n{linea}'
        
        opciones = 'AaBbCcQq'
        
        valor: bool = self.opcion_leer_archivos()
        
        while valor:
            print(menu) # Imprimimos las opciones a elegir
            respuesta = str(input('\nEscoge una opción: ')) # Solicitamos la opción dentro del menú
            print('\n' + linea + '\n')
            
            self.crear_arboles_cursos()
            
            if respuesta.upper() == 'A':
                print('\n  Creando oferta agregada...')
                
                self.oferta_agregada()
                self.agregado = True

                sleep(0.25)
                print('\n  Oferta terminada.\n')

                print(f'\n  Resultado:\n\n{self.arbol_agregado}')

            elif respuesta.upper() == 'B':
                print('\n  Creando oferta común...')

                self.oferta_comun()
                self.comun = True

                sleep(0.25)
                print('\n  Oferta terminada.\n')

                print(f'\n  Resultado:\n\n{self.arbol_comun}')

            elif respuesta.upper() == 'C':
                
                print(self.agregado, self.comun)

                if self.agregado and self.comun:
                    
                    pandas = Pandas()
                    bosque = (self.arbol_A, self.arbol_B, self.arbol_agregado, self.arbol_comun)
                    
                    for arbol in bosque:
                        pandas.estad_totales(arbol)
                        print(f'\n{linea}\n')
                    
                else:
                    print('  Se deben crear ambos árboles (oferta agregada y oferta común) antes de poder mostrar las estadísticas totales.')

            elif respuesta.upper() == 'Q':
                print('\n  Saliendo...\n')
                break
            
            elif respuesta not in opciones:
                print('La opción no se encuentra en el menú.')
    
    @property
    def arbol_A(self) -> AVL:
        return self._arbol_A
    
    @property
    def arbol_B(self) -> AVL:
        return self._arbol_B
    
    @property
    def arbol_agregado(self) -> AVL:
        return self._arbol_agregado
    
    @property
    def arbol_comun(self) -> AVL:
        return self._arbol_comun
    
    @property
    def agregado(self) -> bool:
        return self._agregado
    
    @agregado.setter
    def agregado(self, booleano:bool) -> None:
        if isinstance(booleano, bool):
            self._agregado = booleano
        else:
            print('El para "agregado" valor debe ser un booleano.')
    
    @property
    def comun(self) -> bool:
        return self._comun
    
    @comun.setter
    def comun(self, booleano:bool) -> None:
        if isinstance(booleano, bool):
            self._comun = booleano
        else:
            print('El valor para "comun" debe ser un booleano.')
    


def main() -> None:
    '''
    Función principal que lee el archivo de texto y crea los objetos Curso.
    
    Returns
    -------
    None
    '''
    simulador = SimuladorCursos()
    simulador.crear_arboles_cursos()
    simulador.menu()

    '''
    for cursoB in simulador.arbol_A.values():
        print(cursoB)
    print()
    for cursoA in simulador.arbol_B.values():
        print(cursoA)
    print()
    for curso_ag in simulador.arbol_agregado.values():
        print(curso_ag)
    print()
    for curso_com in simulador.arbol_comun.values():
        print(curso_com)
    '''


if __name__ == '__main__':
    main()