'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

from tomlkit import value
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
    __init__(self) -> None:
        Asigna atributos al objeto.

    crear_arbol_cursos(self, texto:str) -> AVL:
        Permite leer dos archivos de texto con la información de las los cursos
        que se quieren organizar y los mete en dos árboles A y B respectivamente.
    
    oferta_agregada(self) -> AVL:
        Agrega los cursos realizados por cada una de las academias a un sólo árbol. Si dos cursos son iguales
        se escogerá el de mayor beneficio. Además, si dos cursos tienen mismo nombre, se le asignará el nombre de cada
        academia respectivamente.
    
    oferta_comun(self) -> AVL:
        Agrega los cursos realizados únicamente en ambas academias a un árbol común.
    
    opcion_leer_archivos(self) -> bool:
        Permite elegir entre leer o no leer los ficheros de texto mediante un menú auxiliar.
    
    menu(self) -> None:
        Imprime por pantalla el menú de opciones para navegar entre los cursos y le permite escoger
        a un usuario entre 3 opciones de visualización/filtrado, además de la opción de poder salir del menú.
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


    def crear_arboles_cursos(self) -> None:
        '''
        Método que permite leer dos archivos de texto con la información de las los cursos
        que se quieren organizar y los mete en dos árboles A y B respectivamente.

        Returns
        -------
        None
        '''
        
        with open(argv[1], 'r', encoding = 'utf-8') as archivoA:
            texto1: str = archivoA.read()
            lineas = str(texto1).split('\n') # Leemos el archivo
            
            for linea in lineas:
                if not linea.startswith('#'):
                    partes_linea = str(linea).split(',')

                    cursoA = Curso(nombre=      str(partes_linea[0]),
                                   duracion=    int(partes_linea[1]),
                                   estudiantes= int(partes_linea[2]),
                                   nivel=       str(partes_linea[3]),
                                   idioma=      str(partes_linea[4]),
                                   precio=      float(partes_linea[5]))
                    
                    self.arbol_A[cursoA.clave] = cursoA
        
        with open(argv[2], 'r', encoding = 'utf-8') as archivoB:
            texto2: str = archivoB.read()
            lineas = str(texto2).split('\n')
            
            for linea in lineas:
                if not linea.startswith('#'):
                    partes_linea = str(linea).split(',')
    
                    cursoB = Curso(nombre=      str(partes_linea[0]),
                                   duracion=    int(partes_linea[1]),
                                   estudiantes= int(partes_linea[2]),
                                   nivel=       str(partes_linea[3]),
                                   idioma=      str(partes_linea[4]),
                                   precio=      float(partes_linea[5]))
                    
                    self.arbol_B[cursoB.clave] = cursoB
    
    
    def oferta_agregada(self) -> None:
        '''
        Método que agrega los cursos realizados por cada una de las academias a un sólo árbol. Si dos cursos son iguales
        se escogerá el de mayor beneficio. Además, si dos cursos tienen mismo nombre, se le asignará el nombre de cada
        academia respectivamente.
        
        Returns
        -------
        None
        '''
        for curso_A in self.arbol_A.values():
            for curso_B in self.arbol_B.values():
                
                if curso_A == curso_B:

                    if curso_A.beneficio >= curso_B.beneficio:
                        curso_A.estudiantes += curso_B.estudiantes
                        curso_A.nombre += ' (A)'
                        curso_B.nombre += ' (B)'
                        self.arbol_agregado[curso_A.clave] = curso_A
                    
                    else:
                        curso_B.estudiantes += curso_A.estudiantes
                        curso_A.nombre += ' (A)'
                        curso_B.nombre += ' (B)'
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
            for curso_B in self.arbol_B.values():
                
                if curso_A == curso_B:

                    if curso_A.beneficio >= curso_B.beneficio:
                        curso_A.estudiantes += curso_B.estudiantes
                        self.arbol_comun[curso_A.clave] = curso_A
                    
                    else:
                        curso_B.estudiantes += curso_A.estudiantes
                        self.arbol_comun[curso_B.clave] = curso_B
    
    
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
        
        print(f'\n{"="*50}\n\n{texto}\n\n{"="*50}')
        
        while True:
            eleccion = str(input('\n  Responde aquí: '))
            
            if eleccion.upper() == 'S':
                print(f'\n{linea}\n\n  Leyendo ficheros...\n')
                self.crear_arboles_cursos()
                sleep(0.10)
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
        
        menu  = f'\n\n{"MENÚ":=^50}\n'
        menu += '\nA - Realizar la operación "oferta agregada"'
        menu += '\nB - Realizar la operación "oferta común"'
        menu += '\nC - Mostrar estadísticas'
        menu += '\n\nQ - Salir del menú'
        menu += f'\n\n{"="*50}\n'
        
        opciones = 'AaBbCcQq'
        
        valor: bool = self.opcion_leer_archivos()
        
        while valor:
            print(menu) # Imprimimos las opciones a elegir
            respuesta = str(input('  Escoge una opción: ')) # Solicitamos la opción dentro del menú
            print('\n' + linea + '\n')
            
            self.crear_arboles_cursos()
            
            if respuesta.upper() == 'A':
                print('\n  Creando oferta agregada...')
                
                self.oferta_agregada()
                self.agregado = True

                sleep(0.10)
                print('\n  Oferta terminada.\n')

                print(f'\n  Resultado:\n\n')
                self.arbol_agregado
                for curso_agregado in self.arbol_agregado.values():
                    print(curso_agregado)

            elif respuesta.upper() == 'B':
                print('\n  Creando oferta común...')

                self.oferta_comun()
                self.comun = True

                sleep(0.10)
                print('\n  Oferta terminada.\n')

                print(f'\n  Resultado:\n\n')
                for curso_comun in self.arbol_comun.values():
                    print(curso_comun)

            elif respuesta.upper() == 'C':

                if self.agregado and self.comun:
                    
                    pandas = Pandas()
                    
                    print(f'{linea}\n\nÁRBOL A:')
                    pandas.estad_totales(self.arbol_A)
                    print(f'\n{linea}\n\n')

                    print(f'{linea}\n\nÁRBOL B:')
                    pandas.estad_totales(self.arbol_B)
                    print(f'\n{linea}\n\n')

                    print(f'{linea}\n\nÁRBOL AGREGADO:')
                    pandas.estad_totales(self.arbol_agregado)
                    print(f'\n{linea}\n\n')

                    print(f'{linea}\n\nÁRBOL COMÚN:')
                    pandas.estad_totales(self.arbol_comun)
                    print(f'\n{linea}\n\n')
                    
                else:
                    print('  Se deben crear ambos árboles (oferta agregada y oferta común) antes de poder mostrar las estadísticas totales.')

            elif respuesta.upper() == 'Q':
                print('\n  Saliendo...\n')
                break
            
            elif respuesta not in opciones:
                print('  La opción no se encuentra en el menú.')
    
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
            ValueError('El para "agregado" valor debe ser un booleano.')
    
    @property
    def comun(self) -> bool:
        return self._comun
    
    @comun.setter
    def comun(self, booleano:bool) -> None:
        if isinstance(booleano, bool):
            self._comun = booleano
        else:
            ValueError('El valor para "comun" debe ser un booleano.')


def main() -> None:
    '''
    Función principal que lee inicia el simulador y el menú de cursos.
    
    Returns
    -------
    None
    '''
    simulador = SimuladorCursos()
    simulador.menu()



if __name__ == '__main__':
    main()