'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

from array_ordered_positional_list import ArrayOrderedPositionalList
import sys

class Pelicula:
    '''
    '''
    
    def __init__(self, titulo:str, director:str, anho_estreno:int, puntuacion_media:float):       
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
        if self.director == pelicula.director:
            return True
        
        elif self.anho_estreno == pelicula.anho_estreno:
            return True
        
        elif self.titulo == pelicula.titulo:
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
        if self.director > pelicula.director:
            return True
        
        elif self.anho_estreno > pelicula.anho_estreno:
            return True
        
        elif self.titulo > pelicula.titulo:
            return True
        
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
        if self.director < pelicula.director:
            return True
        
        elif self.anho_estreno < pelicula.anho_estreno:
            return True
        
        elif self.titulo < pelicula.titulo:
            return True
        
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
        if self.director >= pelicula.director:
            return True
        
        elif self.anho_estreno >= pelicula.anho_estreno:
            return True
        
        elif self.titulo >= pelicula.titulo:
            return True
        
        return False
    
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
            
            pelicula: Pelicula = Pelicula(director= director, titulo= titulo, anho_estreno= anho_estreno, puntuacion_media= puntuacion_media)

            lista_peliculas.add(pelicula)
        
        return lista_peliculas
    
    def eliminar_repetidos(self, lista_ordenada:ArrayOrderedPositionalList) -> ArrayOrderedPositionalList:
        '''
        '''
        for posicion_i in range(len(lista_ordenada)):
            for posicion_j in range(len(lista_ordenada)):
                print(posicion_i, posicion_j)
                if lista_ordenada.get_element(posicion_i) == lista_ordenada.get_element(posicion_j):
                    lista_ordenada.delete(posicion_j)
        
        return lista_ordenada

def main():
    '''
    '''
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        texto_peliculas: str = f.read()
        
        simulador: SimuladorPeliculas = SimuladorPeliculas()
        lista_peliculas_original: ArrayOrderedPositionalList = simulador.crear_lista_peliculas(texto_peliculas) # Creamos la lista de películas con repetidos
        lista_peliculas_procesada: ArrayOrderedPositionalList = simulador.eliminar_repetidos(lista_peliculas_original) # Procesamos la lista de películas para eliminar repetidos
        
        
        for i in lista_peliculas_original:
            print(i)
        
        for j in lista_peliculas_procesada:
            print(j)


if __name__ == '__main__':
    main()