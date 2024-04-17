'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''
from sys import argv

tipo = False #Cambiar a 'False' si se quiere cambiar el tipo de lista ordenada

if tipo:
    from array_ordered_positional_list import ArrayOrderedPositionalList as ListaOrdenada
else:
    from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada

class Pelicula:
    '''
    Clase abstracta para una película.
    La clase tiene como atributos el director, título, año de estreno y puntuación media
    de la película.

    Attributes
    ----------
    titulo : str
     Título de la película.
    director : str
     Director de la película.
    anho_estreno : int
     Año de estreno de la película.
    puntuacion_media : int
     Puntuación media de la película.

    Methods
    -------
    __init__(self, director:str, titulo:str, anho_estreno:int, puntuacion_media:float) -> None:
        Asigna atributos al objeto.
    
    __str__(self) -> str:
        Implementación del método mágico "str".
        Imprime un string informativo de la película.
    
    __eq__(self, pelicula:'Pelicula') -> bool:
        Implementación del método mágico "==".
    
    __gt__(self, pelicula:'Pelicula') -> bool:
        Implementación del método mágico ">".

    __lt__(self, pelicula:'Pelicula') -> bool:
        Implementación del método mágico "<".

    __ge__(self, pelicula:'Pelicula') -> bool:
        Implementación del método mágico ">=".
    '''
    
    def __init__(self, director:str, titulo:str, anho_estreno:int, puntuacion_media:float) -> None:       
        '''
        Método mágico que asigna atributos al objeto.

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
        Imprime un string informativo de la película.

        Returns
        -------
        str
         String informativo de una película.
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
        return (self == pelicula or self > pelicula)
    
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
    Clase del simulador de gestión de películas, que extrae información de un string y la convierte en películas,
    añadiéndolas a una lista ordenada.

    Methods
    -------
    crear_lista_peliculas(self, texto:str) -> ListaOrdenada:
        Permite leer un string de texto con la información de las películas que se quieren ordenar y
        crear una lista ordenada con ellas.
    
    eliminar_repetidos(self, lista_ordenada:ListaOrdenada) -> ListaOrdenada:
        Elimina las películas repetidas de una lista ordenada.
    
    menu(self, lista_original:ListaOrdenada) -> None:
        Imprime por pantalla el menú de opciones para navegar entre las películas y le permite escoger a un usuario
        entre 3 opciones de visualización/filtrado de la lista, además de la opción de poder salir del menú.
    '''
    def crear_lista_peliculas(self, texto:str) -> ListaOrdenada:
        '''
        Método que permite leer un string de texto con la información de las películas que se quieren ordenar y
        crear una lista ordenada con ellas.

        Parameters
        ----------
        texto : str
         String de texto del que se extrae la información de las películas.

        Returns
        -------
        ListaOrdenada
         Lista ordenada de las películas (ArrayPositionalList o LinkedPositionalList).
        '''
        lista_peliculas: ListaOrdenada = ListaOrdenada()
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
    
    def eliminar_repetidos(self, lista_ordenada:ListaOrdenada) -> ListaOrdenada:
        '''
        Método que elimina las películas repetidas de una lista ordenada.

        Parameters
        ----------
        ListaOrdenada
         Lista ordenada de las películas (ArrayPositionalList o LinkedPositionalList) de la que se quieren eliminar las películas repetidas.

        Returns
        -------
        ListaOrdenada
         Lista ordenada de las películas (ArrayPositionalList o LinkedPositionalList) sin películas repetidas.
        '''
        nueva_lista: ListaOrdenada = ListaOrdenada()

        for posicion in range(1, len(lista_ordenada)):
            print(posicion)
            pelicula: Pelicula = lista_ordenada.get_element(posicion)
            pelicula_anterior: Pelicula = lista_ordenada.get_element(lista_ordenada.before(posicion))

            if pelicula not in nueva_lista:
                if pelicula >= pelicula_anterior:
                    nueva_lista.add(pelicula)
                else:
                    nueva_lista.add(pelicula_anterior)

        return nueva_lista
    
    def menu(self, lista_original:ListaOrdenada) -> None:
        '''
        Imprime por pantalla el menú de opciones para navegar entre las películas y le permite escoger a un usuario
        entre 3 opciones de visualización/filtrado de la lista, además de la opción de poder salir del menú.
        
        Parameters 
        ---------- 
        lista_original : ListaOrdenada 
         Lista ordenada (ArrayPositionalList o LinkedPositionalList) de la que se muestran los resultados del menú.
        
        Returns
        -------
        None
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
                director: str = str(input('Introduce el director que deseas buscar (Formato de búsqueda: Apellido, Nombre): '))
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
                print('\n  Saliendo...\n')
                break

            elif respuesta not in opciones:
                print('La opción no se encuentra en la lista.')
            

def main() -> None:
    '''
    Función principal que lee el archivo de texto, crea los objetos Pelicula y los añade ordenándolos automáticamente.
    Además, crea un nuevo archivo de texto sin películas repetidas.

    Returns
    -------
    None
    '''
    with open(argv[1], 'r', encoding='utf-8') as archivo:
        texto_peliculas: str = archivo.read()
        
        simulador: SimuladorPeliculas = SimuladorPeliculas()
        lista_peliculas_original: ListaOrdenada = simulador.crear_lista_peliculas(texto_peliculas) # Creamos la lista de películas con repetidos
        
        simulador.menu(lista_peliculas_original) #Mostramos el menú y ejecutamos la función del menú (implementación más arriba).

        
        with open('peliculas_sin_repetidos.txt', 'w', encoding='utf-8') as archivo_sin_repetidos: # Creamos un nuevo archivo sin películas repetidas
            
            lista_peliculas_procesada: ListaOrdenada = simulador.eliminar_repetidos(lista_peliculas_original) # Procesamos la lista de películas para eliminar repetidos
            
            for pelicula in lista_peliculas_procesada:
                archivo_sin_repetidos.write(f'{pelicula.director}; {pelicula.titulo}; {pelicula.anho_estreno}; {pelicula.puntuacion_media}\n')
        
if __name__ == '__main__':
    main()