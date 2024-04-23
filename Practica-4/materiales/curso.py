'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

class Curso:
    '''
    Clase abstracta para un curso.
    La clase tiene como atributos el nombre, duración (h),
    nº de estudiantes, nivel, idioma y precio del curso.

    Attributes
    ----------
    nombre : str
     Nombre del curso.
    duracion : str
     Duración en horas del curso.
    estudiantes : int
     Número de estudiantes del curso.
    nivel : int
     Nivel del curso.
    idioma : str
     Idioma del curso.
    precio : float
     Precio del curso.
   
    Methods
    -------
    __init__(self, nombre:str, duracion:int, estudiantes:int, nivel:str, idioma:str, precio:float) -> None:
        Asigna atributos al objeto.
    
    
    '''
   
    def __init__(self, nombre:str, duracion:int, estudiantes:int, nivel:str, idioma:str, precio:float) -> None:       
        '''
        Método mágico que asigna atributos al objeto.

        Parameters
        ----------
        nombre : str
         Nombre del curso.
        duracion : str
         Duración en horas del curso.
        estudiantes : int
         Número de estudiantes del curso.
        nivel : int
         Nivel del curso.
        idioma : str
         Idioma del curso.
        precio : float
         Precio del curso. 
        '''
        self._nombre = nombre
        self._duracion= duracion
        self._estudiantes = estudiantes
        self._nivel = nivel
        self._idioma = idioma
        self._precio= precio

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def duracion(self) -> str:
        return self._duracion
    
    @property
    def estudiantes(self) -> str:
        return self._estudiantes
    
    @property
    def nivel(self) -> str:
        return self._nivel
    
    @property
    def idioma(self) -> str:
        return self._idioma
    
    @property
    def precio(self) -> str:
        return self._precio