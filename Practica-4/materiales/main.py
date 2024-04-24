'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

from avl_tree import AVL
from curso import Curso
from clase_pandas import Pandas
from sys import argv

class SimuladorCursos:
    '''
    Clase del simulador de gestión de cursos, que extrae información de un string 
    y la convierte en cursos, añadiéndolas a un árbol.

    Methods
    -------
    crear_arbol_cursos(self, texto:str) -> AVL
    
    
    '''
    def crear_arboles_cursos(self) -> AVL:
        '''
        Método que permite leer un string de texto con la información de las los cursos
        que se quieren organizar.

        Returns
        -------
        AVL
         Árbol de los cursos.
        '''
        arbol_cursos1: AVL = AVL()
        arbol_cursos2: AVL = AVL()
        
        with open(argv[1], 'r', encoding='utf-8') as archivo1:
            texto1: str = archivo1.read()
            lineas: str = str(texto1).split('\n')[1:len(lineas)-1]
            
            for linea in lineas:
                partes_linea: str = str(linea).split(',')

                nombre: str = str(partes_linea[0])
                duracion: int = int(partes_linea[1])
                estudiantes: int = int(partes_linea[2])
                nivel: str = str(partes_linea[3])
                idioma: str = str(partes_linea[4])
                precio: float = float(partes_linea[5])

                curso: Curso = Curso(nombre, duracion, estudiantes, nivel, idioma, precio)

                arbol_cursos1.children(curso) # No se puede hacer simplemente "add".

        with open(argv[2], 'r', encoding='utf-8') as archivo1:
            texto2: str = archivo1.read()
            lineas: str = str(texto2).split('\n')[1:len(lineas)-1]
            
            for linea in lineas:
                partes_linea: str = str(linea).split(',')

                nombre: str = str(partes_linea[0])
                duracion: int = int(partes_linea[1])
                estudiantes: int = int(partes_linea[2])
                nivel: str = str(partes_linea[3])
                idioma: str = str(partes_linea[4])
                precio: float = float(partes_linea[5])

                curso: Curso = Curso(nombre, duracion, estudiantes, nivel, idioma, precio)

                arbol_cursos1.add(curso)

        return arbol_cursos1, arbol_cursos2
    
    def oferta_agregada(self) -> AVL:
        '''
        '''
        
    def oferta_comun(self) -> AVL:
        '''
        '''
        
    
    def menu(self) -> None:
        '''
        '''
        linea = '-'*50
        
        menu  = f'\n{linea}'
        menu += '\nA - Leer ficheros de los cursos'
        menu += '\nB - Realizar la operación "oferta agregada"'
        menu += '\nC - Realizar la operación "oferta común"'
        menu += '\nD - Mostrar estadísticas'
        menu += '\n\nQ - Salir del menú'
        menu += f'\n{linea}'
        
        opciones = 'AaBbCcQq'
        
        while True:
            
            print(menu) # Imprimimos las opciones a elegir
            respuesta: str = str(input('\nEscoge una opción: ')) # Solicitamos la opción dentro del menú
            print('\n' + linea + '\n')
            
            if respuesta.upper() == 'A':
                self.crear_arboles_cursos()
            
            elif respuesta.upper() == 'B':
                self.oferta_agregada()
            
            elif respuesta.upper() == 'C':
                self.oferta_comun()
            
            elif respuesta.upper() == 'D':
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
    pass
        

if __name__ == '__main__':
    main()