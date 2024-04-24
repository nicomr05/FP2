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
            lineas: str = str(texto1).split('\n')[1:len(lineas)-1] # Leemos el archivo
            
            for linea in lineas:
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
            lineas: str = str(texto2).split('\n')[1:len(lineas)-1]
            
            for linea in lineas:
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
        '''
        
    def oferta_comun(self) -> AVL:
        '''
        '''
    
    def opcion_leer_archivos(self) -> None:
        '''
        Método que permite elegir entre leer o no leer los ficheros de texto.
        
        Returns
        -------
        None
        '''
        linea = '-'*50
        texto = '¿Leer ficheros de los cursos A y B? (Y/N)'
        
        print(f'\n{linea}\n{texto}\n{linea}')
        
        eleccion: str = str(input('\nResponde aquí: '))
        
        while True:
            if eleccion.upper() == 'Y':
                print('\n  Leyendo ficheros...')
                return True
            
            elif eleccion.upper() == 'N':
                print('\n  Saliendo...')
                return False
            
            else:
                print('\n  Respuesta no válida.')
        
        
    def menu(self) -> None:
        '''
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
    pass
        

if __name__ == '__main__':
    main()