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
    def crear_arboles_cursos(self) -> tuple[AVL,AVL]:
        '''
        Método que permite leer dos archivos de texto con la información de las los cursos
        que se quieren organizar y los mete en dos árboles A y B respectivamente.

        Returns
        -------
        tuple[AVL,AVL]
         Tupla de los dos árboles de cursos.
        '''
        arbol_cursos_A: AVL = AVL()
        arbol_cursos_B: AVL = AVL()
        
        with open(argv[1], 'r', encoding='utf-8') as archivoA:
            texto1: str = archivoA.read()
            lineas: str = str(texto1).split('\n') # Leemos el archivo
            
            for linea in lineas[1:len(lineas)-1]:
                partes_linea: str = str(linea).split(',')

                nombre: str = str(partes_linea[0])
                duracion: int = int(partes_linea[1])
                estudiantes: int = int(partes_linea[2])
                nivel: str = str(partes_linea[3])
                idioma: str = str(partes_linea[4])
                precio: float = float(partes_linea[5])

                cursoA: Curso = Curso(nombre, duracion, estudiantes, nivel, idioma, precio)
                
                arbol_cursos_A[cursoA.clave] = cursoA

        with open(argv[2], 'r', encoding='utf-8') as archivoB:
            texto2: str = archivoB.read()
            lineas: str = str(texto2).split('\n')
            
            for linea in lineas[1:len(lineas)-1]:
                partes_linea: str = str(linea).split(',')

                nombre: str = str(partes_linea[0])
                duracion: int = int(partes_linea[1])
                estudiantes: int = int(partes_linea[2])
                nivel: str = str(partes_linea[3])
                idioma: str = str(partes_linea[4])
                precio: float = float(partes_linea[5])

                cursoB: Curso = Curso(nombre, duracion, estudiantes, nivel, idioma, precio)
                
                arbol_cursos_B[cursoB.clave] = cursoB

        return (arbol_cursos_A, arbol_cursos_B)
    
    
    def oferta_agregada(self) -> AVL:
        '''
        Método que agrega los cursos realizados por cada una de las academias a un árbol común.
        
        Returns
        -------
        AVL
         Árbol con los cursos de cada una de las academias.
        '''
        NotImplemented('Implementar oferta_agregada.')
    

    def oferta_comun(self) -> AVL:
        '''
        Método que agrega los cursos realizados únicamente en ambas academias a un árbol común.
        
        Returns
        -------
        AVL
         Árbol con los cursos que aparecen en ambas academias.
        '''
        NotImplemented('Implementar oferta_comun.')
    
    
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
        
        print(f'{linea}\n\n{texto}\n\n{linea}')
        
        while True:
            eleccion: str = str(input('\nResponde aquí: '))
            
            if eleccion.upper() == 'S':
                print(f'\n{linea}\n\n  Leyendo ficheros...\n')
                sleep(0.25)
                return True
            
            elif eleccion.upper() == 'N':
                print(f'\n{linea}\n\n  Saliendo...\n')
                return False
            
            else:
                print('\n  Respuesta no válida.')
        
        
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
            respuesta: str = str(input('\nEscoge una opción: ')) # Solicitamos la opción dentro del menú
            print('\n' + linea + '\n')
            
            self.crear_arboles_cursos()
            
            if respuesta.upper() == 'A':
                self.oferta_agregada()
            
            elif respuesta.upper() == 'B':
                self.oferta_comun()
            
            elif respuesta.upper() == 'C':
                Pandas().estad_totales()
            
            elif respuesta.upper() == 'Q':
                print('\n  Saliendo...\n')
                break
            
            elif respuesta not in opciones:
                print('La opción no se encuentra en el menú.')


def main() -> None:
    '''
    Función principal que lee el archivo de texto y crea los objetos Curso.
    
    Returns
    -------
    None
    '''
    simulador: SimuladorCursos = SimuladorCursos()
    simulador.menu()        



if __name__ == '__main__':
    main()