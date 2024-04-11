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
        '''
        cadena: str = f'{self.director} | '
        cadena += f'{self.titulo} | '
        cadena += f'{self.anho_estreno} | '
        cadena += f'{self.puntuacion_media}'
        
        return cadena
    
    def __eq__(self, pelicula:'Pelicula') -> bool:
        '''
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
    def crear_peliculas(self, texto:str) -> ArrayOrderedPositionalList:
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

def main():
    '''
    '''
    with open(sys.argv[1]) as f:
        texto_peliculas: str = f.read()
        
        simulador: SimuladorPeliculas = SimuladorPeliculas()
        lista_peliculas: ArrayOrderedPositionalList = simulador.crear_peliculas(texto_peliculas)
        
        for pelicula1 in lista_peliculas:
            for pelicula2 in lista_peliculas:
                if pelicula1 == pelicula2:
                    pelicula1: Pelicula = Pelicula
                    lista_peliculas.delete(pelicula1)

        print(lista_peliculas)

if __name__ == '__main__':
    main()