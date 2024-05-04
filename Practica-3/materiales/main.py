'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''
from re import S
from sys import argv
from time import sleep

from numpy import isin
from zmq import CURVE_PUBLICKEY
from pelicula import Pelicula
from clase_pandas import Pandas

tipo = False # Cambiar a 'False' si se quiere cambiar el tipo de lista ordenada

if tipo:
    from array_ordered_positional_list import ArrayOrderedPositionalList as ListaOrdenada
else:
    from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada


class SimuladorPeliculas:
    '''
    Clase del simulador de gestión de películas, que extrae información de un string y la convierte en películas,
    añadiéndolas a una lista ordenada.

    Methods
    -------
    __init__(self) -> None:
        Asigna atributos al objeto.
    
    crear_lista_peliculas(self) -> None:
        Permite leer un string de texto con la información de las películas que se quieren ordenar y
        crear una lista ordenada con ellas.
    
    eliminar_repetidos(self) -> None:
        Elimina las películas repetidas de una lista ordenada.
    
    opcion_leer_archivos(self) -> bool:
        Permite elegir entre leer o no leer el fichero de texto.
    
    buscar_director(self, director:str) -> None:
        Busca un director en la lista ordenada de directores.
    
    buscar_anho(self, anho:int) -> None:
        Busca un año en la lista ordenada de directores.
    
    menu(self) -> None:
        Imprime por pantalla el menú de opciones para navegar entre las películas y le permite escoger a un usuario
        entre 3 opciones de visualización/filtrado de la lista, además de la opción de poder salir del menú.
    '''
    def __init__(self) -> None:
        '''
        Método que asigna atributos al objeto.
        
        Returns
        -------
        None
        '''
        self._lista_ordenada = ListaOrdenada()
        self._lista_ordenada_sin_repetidos = ListaOrdenada()
        
    
    def crear_lista_peliculas(self) -> None:
        '''
        Método que permite leer un string de texto con la información de las películas que se quieren ordenar y
        crear una lista ordenada con ellas.

        Returns
        -------
        None
        '''
        with open(argv[1], 'r', encoding='utf-8') as archivo:
            texto_peliculas: str = archivo.read()
            lineas: str = str(texto_peliculas).split('\n')
        
            for linea in lineas:
                partes_linea: str = str(linea).split('; ')

                pelicula = Pelicula(str(partes_linea[0]),
                                    str(partes_linea[1]),
                                    int(partes_linea[2]),
                                    float(partes_linea[3]))

                self.lista_ordenada.add(pelicula)
                
    
    def eliminar_repetidos(self) -> None:
        '''
        Método que elimina las películas repetidas de una lista ordenada.
        
        Returns
        -------
        None
        '''
        copia_lista: ListaOrdenada = ListaOrdenada() # Lista vacía sin repetidos que es la que devolverá la función.
        
        for pelicula in self.lista_ordenada:
            copia_lista.add(pelicula)
        
        while True:
            
            posicion_pelicula: Pelicula = copia_lista.first()
            posicion_pelicula_posterior: Pelicula = copia_lista.after(posicion_pelicula)

            primera: Pelicula = copia_lista.get_element(posicion_pelicula)
            segunda: Pelicula = copia_lista.get_element(posicion_pelicula_posterior)


            if primera.anho_estreno == segunda.anho_estreno:
                if copia_lista.last() == posicion_pelicula_posterior:
                    self.lista_ordenada_sin_repetidos.add(segunda)
                    break

                copia_lista.delete(posicion_pelicula)

            else:
                if copia_lista.last() == posicion_pelicula_posterior:
                    self.lista_ordenada_sin_repetidos.add(primera)
                    self.lista_ordenada_sin_repetidos.add(segunda)
                    break

                self.lista_ordenada_sin_repetidos.add(primera)
                copia_lista.delete(posicion_pelicula)

    
    def opcion_leer_archivos(self) -> bool:
        '''
        Método que permite elegir entre leer o no leer el fichero de texto.
        
        Returns
        -------
        bool
         True si se decide leer el archivo.
         False si se decide no leer el archivo.
        '''
        linea = '-'*50
        texto = '¿Leer el fichero de películas? (S/N)'
        
        print(f'\n{"="*50}\n\n{texto}\n\n{"="*50}')
        
        while True:
            eleccion = str(input('\n  Responde aquí: '))
            
            if eleccion.upper() == 'S':
                print(f'\n{linea}\n\n  Leyendo fichero...\n')
                self.crear_lista_peliculas()
                return True
            
            elif eleccion.upper() == 'N':
                print(f'\n{linea}\n\n  Saliendo...\n')
                return False
            
            else:
                print(f'\n  Respuesta no válida.\n\n{linea}')
    
    
    def buscar_director(self, director:str) -> None:
        '''
        Función que busca un director en la lista.
        
        Parameters
        ----------
        director : str
         Director por el que se quieren filtrar las películas.
                
        Returns
        -------
        None
        '''
        lista_peliculas: list = []
        
        if isinstance(director, str) and len(director) > 0:
            
            for pelicula in self.lista_ordenada:
                if director in pelicula.director:
                    lista_peliculas.append(pelicula)
            
            if len(lista_peliculas) != 0:
                    for peli in lista_peliculas:
                        print(peli)
            else:
                print(f'\n  No se han encontrado películas de "{director}".')
                
                
        else:
            print('El director introducido deben ser una cadena de texto no vacía.')

    
    def buscar_anho(self, anho:int) -> None:
        '''
        Función que busca un año en la lista ordenada de directores.
        
        Parameters
        ----------
        anho : str
         Año por el que se quieren filtrar las películas.
                
        Returns
        -------
        None
        '''
        lista_peliculas: list = []
        
        if isinstance(anho, int) and anho > 0:
            
            for pelicula in self.lista_ordenada:
                if anho == pelicula.anho_estreno:
                    lista_peliculas.append(pelicula)

            if len(lista_peliculas) != 0:
                for peli in lista_peliculas:
                    print(peli)

            else:
                print(f'\n  No se han encontrado películas del {anho}.')
        
        else:
            print('\n  El año introducido debe ser un entero positivo.')
    
    
    def menu(self) -> None:
        '''
        Imprime por pantalla el menú de opciones para navegar entre las películas y le permite escoger a un usuario
        entre 3 opciones de visualización/filtrado de la lista, además de la opción de poder salir del menú.
        
        Returns
        -------
        None
        '''
        linea = '-'*50
        
        menu: str = f'\n{" MENÚ ":=^50}'
        menu += '\nA - Mostrar todas las películas'
        menu += '\nB - Buscar películas de un director'
        menu += '\nC - Buscar películas de un año concreto'
        menu += '\nD - Crear archivo de texto sin películas repetidas'
        menu += '\nE - Mostrar estadísticas'
        menu += '\n\nQ - Salir del menú'
        menu += f'\n{"="*50}'
        
        opciones = 'AaBbCcQq'
        
        self.opcion_leer_archivos()
        
        while True:
            print(menu) # Imprimimos las opciones a elegir
            respuesta: str = str(input('\n  Escoge una opción: ')) # Solicitamos la opción dentro del menú
            
            print('\n' + linea + '\n')
            
            if respuesta.upper() == 'A':
                for pelicula in self.lista_ordenada:
                    print(pelicula)
            
            elif respuesta.upper() == 'B':
                director: str = str(input('  Introduce el director que deseas buscar (Formato de búsqueda: Apellido, Nombre): '))
                
                print('\n  Películas disponibles:')
                self.buscar_director(director)

            elif respuesta.upper() == 'C':
                try:
                    anho: int = int(input('  Introduce el año de las películas que deseas buscar: '))
                    
                    print('\n  Películas disponibles:')
                    self.buscar_anho(anho)
                    
                except ValueError:
                    print('\n  El año debe ser un entero.')
                    
            elif respuesta.upper() == 'D':
                print('Creando archivo...\n')
                self.eliminar_repetidos() # Procesamos la lista de películas para eliminar repetidos.
                
                with open('peliculas_sin_repetidos.txt', 'w', encoding='utf-8') as archivo_sin_repetidos: # Creamos un nuevo archivo sin películas repetidas

                    for pelicula in self.lista_ordenada_sin_repetidos:
                        pelicula: Pelicula
                        
                        archivo_sin_repetidos.write(f'{pelicula.director}; {pelicula.titulo}; {pelicula.anho_estreno}; {pelicula.puntuacion_media}\n')
                
                sleep(0.20)
                print('Archivo creado.')
                sleep(0.10)
            
            elif respuesta.upper() == 'E':
                
                self.eliminar_repetidos() # Procesamos la lista de películas para eliminar repetidos y la guardamos en una variable
                
                datos = Pandas()
                datos.estad_totales(self.lista_ordenada_sin_repetidos)
            
            elif respuesta.upper() == 'Q':
                print('\n  Saliendo...\n')
                break

            elif respuesta not in opciones:
                print('  La opción no se encuentra en el menú.')
    
    @property
    def lista_ordenada(self) -> ListaOrdenada:
        return self._lista_ordenada

    @property
    def lista_ordenada_sin_repetidos(self) -> ListaOrdenada:
        return self._lista_ordenada_sin_repetidos


def main() -> None:
    '''
    Función principal que lee el archivo de texto, crea los objetos Pelicula y los añade ordenándolos automáticamente.
    Además, crea un nuevo archivo de texto sin películas repetidas.

    Returns
    -------
    None
    '''
    simulador = SimuladorPeliculas()
    simulador.menu() #Mostramos el menú y ejecutamos la función del menú (implementación más arriba).


        
if __name__ == '__main__':
    main()