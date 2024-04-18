'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''
from sys import argv
from time import sleep
import pandas as pd

tipo = True #Cambiar a 'False' si se quiere cambiar el tipo de lista ordenada

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
        lista_ordenada : ListaOrdenada
         Lista ordenada de las películas (ArrayPositionalList o LinkedPositionalList) de la que se quieren eliminar las películas repetidas.
        tipo_lista : bool
         True si es una ArrayPositionalList
         False si es una LinkedPositionalList
        
        Returns
        -------
        ListaOrdenada
         Lista ordenada de las películas (ArrayPositionalList o LinkedPositionalList) sin películas repetidas.
        '''
        copia_lista: ListaOrdenada = lista_ordenada
        nueva_lista: ListaOrdenada = ListaOrdenada()
        
    
        while True:
            
            posicion_pelicula: Pelicula = copia_lista.first()
            posicion_pelicula_posterior: Pelicula = copia_lista.after(posicion_pelicula)

            primera: Pelicula = copia_lista.get_element(posicion_pelicula)
            segunda: Pelicula = copia_lista.get_element(posicion_pelicula_posterior)


            if primera.anho_estreno == segunda.anho_estreno:
                if copia_lista.last() == posicion_pelicula_posterior:
                    nueva_lista.add(segunda)
                    break

                copia_lista.delete(posicion_pelicula)

            else:
                if copia_lista.last() == posicion_pelicula_posterior:
                    nueva_lista.add(primera)
                    nueva_lista.add(segunda)
                    break

                nueva_lista.add(primera)
                copia_lista.delete(posicion_pelicula)
                        
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
        menu += '\nD - Crear archivo de texto sin películas repetidas'
        menu += '\nE - Mostrar estadísticas'
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

            elif respuesta == 'D' or respuesta == 'd':
                
                print('Creando archivo...\n')
                with open('peliculas_sin_repetidos.txt', 'w', encoding='utf-8') as archivo_sin_repetidos: # Creamos un nuevo archivo sin películas repetidas
            
                    lista_peliculas_procesada: ListaOrdenada = self.eliminar_repetidos(lista_original) # Procesamos la lista de películas para eliminar repetidos y la guardamos en una variable

                    for pelicula in lista_peliculas_procesada:
                        archivo_sin_repetidos.write(f'{pelicula.director}; {pelicula.titulo}; {pelicula.anho_estreno}; {pelicula.puntuacion_media}\n')
                
                sleep(0.5)
                print('Archivo creado.')
                sleep(0.25)
            
            elif respuesta == 'E' or respuesta == 'e':
                
                lista_peliculas_procesada: ListaOrdenada = self.eliminar_repetidos(lista_original) # Procesamos la lista de películas para eliminar repetidos y la guardamos en una variable
                
                datos = Pandas()
                datos.estad_totales(lista_peliculas_procesada)
            
            elif respuesta == 'Q' or respuesta == 'q':
                print('\n  Saliendo...\n')
                break

            elif respuesta not in opciones:
                print('La opción no se encuentra en la lista.')


class Pandas:
    '''
    Clase que gestiona las estadísticas de las películas y las muestra por pantalla.

    Methods
    -------
    __init__(self) -> None:
        Asigna atributos al objeto.

    estad_totales(self, lista:ListaOrdenada) -> tuple:
        Recoge los valores de cada película y los añade al dataframe como diccionario.
        Luego devuelve una tupla con las estadísticas que se solicitaron.

    peliculas_por_director(self) -> None:
        Cuenta el número de películas por director/a.

    media_director(self) -> None:
        Realiza la media de la puntuación por director/a.

    media_por_anho(self) -> None:
        Realiza la media por año de estreno.
    '''
    def __init__(self) -> None:
        '''
        Asigna atributos al objeto.

        Returns
        -------
        None
        '''
        self._dataframe = pd.DataFrame(columns=['Director', 'Título', 'Fecha', 'Puntuación'])
    
    def estad_totales(self, lista:ListaOrdenada) -> tuple:
        '''
        Método que recoge los valores de cada película y los añade al dataframe como diccionario.
        Luego devuelve una tupla con las estadísticas que se solicitaron.

        Returns
        -------
        tuple
         Tupla con tres valores: número de películas por director, media de puntuación del
         director y la media de puntuación por año.
        '''
        for pelicula in lista:
            fila: dict = {'Director':pelicula.director, 'Título':pelicula.titulo, 'Fecha':pelicula.anho_estreno, 'Puntuación':pelicula.puntuacion_media}
            self.dataframe.loc[len(self.dataframe)] = fila # Añadimos cada diccionario al dataframe. Intentamos hacerlo con append pero daba error.
        
        return (self.peliculas_por_director(), self.media_director(), self.media_por_anho())
            
    def peliculas_por_director(self) -> None:
        '''
        Método que cuenta el número de películas por director/a.

        Returns
        -------
        None
        '''
        group_col = 'Director'
        target_col = 'Título'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['count']})
        print ("\n\n#############################################")
        print ("    Número de películas por director         ")
        print ("#############################################\n")
        print (data_directores)
    
    def media_director(self) -> None:
        '''
        Método que realiza la media de la puntuación por director/a.

        Returns
        -------
        None
        '''
        group_col = 'Director'
        target_col = 'Puntuación'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['mean']})
        print ("\n\n#############################################")
        print ("    Puntuación media agrupada por director   ")
        print ("#############################################\n")
        print (data_directores)
    
    def media_por_anho(self) -> None:
        '''
        Método que realiza la media por año de estreno.

        Returns
        -------
        None
        '''
        group_col = 'Fecha'
        target_col = 'Puntuación'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['mean']})
        print ("\n\n#############################################")
        print ("    Puntuación media agrupada por año        ")
        print ("#############################################\n")
        print (data_directores)

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._dataframe
    

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

        
if __name__ == '__main__':
    main()