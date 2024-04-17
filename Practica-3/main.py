'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

from array_ordered_positional_list import ArrayOrderedPositionalList
from linked_ordered_positional_list import LinkedOrderedPositionalList
import sys

class Pelicula:
    '''
    '''
    
    def __init__(self, director:str, titulo:str, anho_estreno:int, puntuacion_media:float):       
        '''
        

        Parameters
        ----------
        titulo : str
         Título de la película.
        director : str
         Director de la película.
        anho_estreno : int
         Año de estreno de la película.
        puntuacion_media : int
         Puntuación media de la película.
        '''
        self._director = director
        self._titulo = titulo
        self._anho_estreno = anho_estreno
        self._puntuacion_media = puntuacion_media
    
    def __str__(self) -> str:
        '''
        Implementación del método mágico "str".
        '''
        cadena: str = f'{self.director} | '
        cadena += f'{self.titulo} | '
        cadena += f'{self.anho_estreno} | '
        cadena += f'{self.puntuacion_media}'
        
        return cadena
    
    def __eq__(self, pelicula:'Pelicula') -> bool:
        '''
        Implementación del método mágico "==".
        
        Parameters
        ----------
        pelicula : Pelicula
         Película sobre la que se quiere comprobar la igualdad.
        
        Returns
        -------
        bool
        '''
        if self.director == pelicula.director and \
           self.anho_estreno == pelicula.anho_estreno and \
           self.titulo == pelicula.titulo:
            return True
        
        return False
    
    def __gt__(self, pelicula:'Pelicula') -> bool:
        '''
        Implementación del método mágico ">".
        
        Parameters
        ----------
        pelicula : Pelicula
         Película sobre la que se quiere comprobar la desigualdad.
        
        Returns
        -------
        bool
        '''
        if self.director != pelicula.director:
            return self.director > pelicula.director
        
        elif self.anho_estreno != pelicula.anho_estreno:
            return self.anho_estreno > pelicula.anho_estreno
        
        elif self.titulo != pelicula.titulo:
            return self.titulo > pelicula.titulo
        
        return False

    def __lt__(self, pelicula:'Pelicula') -> bool:
        '''
        Implementación del método mágico "<".
        
        Parameters
        ----------
        pelicula : Pelicula
         Película sobre la que se quiere comprobar la desigualdad.
        
        Returns
        -------
        bool
        '''
        if self.director != pelicula.director:
            return self.director < pelicula.director
        
        elif self.anho_estreno != pelicula.anho_estreno:
            return self.anho_estreno < pelicula.anho_estreno
        
        elif self.titulo != pelicula.titulo:
            return self.titulo < pelicula.titulo
        
        return False
    
    def __ge__(self, pelicula:'Pelicula') -> bool:
        '''
        Implementación del método mágico ">=".
        
        Parameters
        ----------
        pelicula : Pelicula
         Película sobre la que se quiere comprobar la (des)igualdad.
        
        Returns
        -------
        bool
        '''
        return self == pelicula or self > pelicula
    
    @property
    def director(self) -> str:
        return self._director
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def anho_estreno(self) -> int:
        return self._anho_estreno
    
    @property
    def puntuacion_media(self) -> int:
        return self._puntuacion_media

class SimuladorPeliculas:
    '''
    '''
    def crear_lista_peliculas(self, texto:str) -> ArrayOrderedPositionalList:
        '''
        '''
        lista_peliculas: ArrayOrderedPositionalList = ArrayOrderedPositionalList()
        lineas: str = str(texto).split('\n')
        
        for linea in lineas:
            partes_linea: str = str(linea).split('; ')
            
            director: str = str(partes_linea[0])
            titulo: str = str(partes_linea[1])
            anho_estreno: int = int(partes_linea[2])
            puntuacion_media: float = float(partes_linea[3])
            
            pelicula: Pelicula = Pelicula(director, titulo, anho_estreno, puntuacion_media)

            lista_peliculas.add(pelicula)
        
        return lista_peliculas
    
    def eliminar_repetidos(self, lista_ordenada:ArrayOrderedPositionalList) -> ArrayOrderedPositionalList:
        '''
        '''
        for posicion in range(len(lista_ordenada)):
            if lista_ordenada.get_element(posicion) == lista_ordenada.after(posicion):
                lista_ordenada.delete(posicion)
        
        return lista_ordenada
    
    def menu(self, lista_original:ArrayOrderedPositionalList) -> None:
        '''
        '''
        
        linea = '-'*50
        
        menu  = f'\n{linea}'
        menu += '\nA - Mostrar todas las películas'
        menu += '\nB - Buscar películas de un director'
        menu += '\nC - Buscar películas de un año concreto'
        menu += '\n\nQ - Salir del menú'
        menu += f'\n{linea}'
        
        opciones = 'AaBbCcQq'
        
        while True:

            print(menu) # Imprimimos las opciones a elegir
            respuesta: str = str(input('\nEscoge una opción: ')) # Solicitamos la opción dentro del menú
            
            print('\n' + linea + '\n')
            
            if respuesta == 'A' or respuesta == 'a':
                for pelicula in lista_original:
                    print(pelicula)
            
            elif respuesta == 'B' or respuesta == 'b':
                director: str = str(input('Introduce el director que deseas buscar (Formato: Apellido, Nombre): '))
                print('\nPelículas disponibles:')
                if isinstance(director, str) and len(director) > 0:
                    for pelicula in lista_original:
                        if pelicula.director == director:
                            print(pelicula)
                
                else:
                    print('Los caracteres introducidos deben ser una cadena de texto no vacía.')

            elif respuesta == 'C' or respuesta == 'c':
                anho: int = int(input('Introduce el año de las películas que deseas buscar: '))
                print('\nPelículas disponibles:')
                
                if isinstance(anho, int) and anho > 0:
                    for pelicula in lista_original:
                        if pelicula.anho_estreno == anho:
                            print(pelicula)
                
                else:
                    print('El año introducido debe ser un entero positivo.')

            elif respuesta == 'Q' or respuesta == 'q':
                print('\nSaliendo...\n')
                break

            elif respuesta not in opciones:
                print('La opción no se encuentra en la lista.')
            

def main():
    '''
    '''
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        texto_peliculas: str = f.read()
        
        simulador: SimuladorPeliculas = SimuladorPeliculas()
        lista_peliculas_original: ArrayOrderedPositionalList = simulador.crear_lista_peliculas(texto_peliculas) # Creamos la lista de películas con repetidos
        #lista_peliculas_procesada: ArrayOrderedPositionalList = simulador.eliminar_repetidos(lista_peliculas_original) # Procesamos la lista de películas para eliminar repetidos
        
        simulador.menu(lista_peliculas_original)

#    with open('peliculas_ordenadas.txt', 'w', encoding='utf-8') as g:
#        g.

if __name__ == '__main__':
    main()