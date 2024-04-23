'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

from sys import argv

class SimuladorCursos:
    '''
    '''
    NotImplemented('Implementar Simulador.')
    

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