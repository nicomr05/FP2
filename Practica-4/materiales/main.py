'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

from avl_tree import AVL
from curso import Curso
from sys import argv

class SimuladorCursos:
    '''
    Clase del simulador de gestión de cursos, que extrae información de un string 
    y la convierte en cursos, añadiéndolas a un árbol.

    Methods
    -------
    '''
    def crear_arbol_cursos(self, texto:str) -> AVL:
        '''
        Método que permite leer un string de texto con la información de las los cursos
        que se quieren organizar.

        Parameters
        ----------
        texto : str
         String de texto del que se extrae la información de las películas.

        Returns
        -------
        arbol_cursos
         Árbol de los cursos.
        '''
        arbol_cursos: AVL = AVL()
        lineas: str = str(texto).split('\n')[1:len(lineas)-1]
        
        for linea in lineas:
            partes_linea: str = str(linea).split(',')
            
            nombre: str = str(partes_linea[0])
            duracion: int = int(partes_linea[1])
            estudiantes: int = int(partes_linea[2])
            nivel: str = str(partes_linea[3])
            idioma:str = str(partes_linea[4])
            precio:float = float(partes_linea[5])

            pelicula: Curso = Curso(nombre, duracion, estudiantes, nivel, idioma, precio)

            arbol_cursos.add(pelicula) # No se puede hacer simplemente "add".
        
        return arbol_cursos
    

def main() -> None:
    '''
    Función principal que lee el archivo de texto y crea los objetos Curso.
    
    Returns
    -------
    None
    '''
    with open(argv[1], 'r', encoding='utf-8') as archivo:
        texto_cursos: str = archivo.read()
        

if __name__ == '__main__':
    main()