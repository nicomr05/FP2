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
        self._duracion = duracion
        self._estudiantes = estudiantes
        self._nivel = nivel
        self._idioma = idioma
        self._precio = precio
        self._clave = f'{self._nombre}_{self._nivel}_{self._idioma}'
        self._beneficio = self._precio*self._duracion*self._estudiantes
    

    def __str__(self) -> str:
        '''
        Implementación del método mágico "str".
        Imprime un string informativo del curso.

        Returns
        -------
        str
         String informativo del curso.
        '''
        cadena: str = f'{self._nombre:14} | '
        cadena += f'{self._duracion:4} | '
        cadena += f'{self._estudiantes:4} | '
        cadena += f'{self._nivel} | '
        cadena += f'{self._idioma:3} | '
        cadena += f'{self._precio:5.2f} €'
        
        return cadena
    

    def __eq__(self, curso:'Curso') -> bool:
        '''
        Implementación del método mágico "==".
        
        Parameters
        ----------
        curso : Curso
         Curso sobre la que se quiere comprobar la igualdad.
        
        Returns
        -------
        bool
        '''
        if self.nombre == curso.nombre:
            if self.nivel == curso.nivel:
                if self.idioma == curso.idioma:
                    return True
        
        return False


    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            ValueError('El del curso debe ser un string no vacío.')
    
    @property
    def duracion(self) -> int:
        return self._duracion
    
    @property
    def estudiantes(self) -> int:
        return self._estudiantes
    
    @estudiantes.setter
    def estudiantes(self, nuevo_valor:int) -> None:
        if isinstance(nuevo_valor, int) and nuevo_valor > 0:
            self._estudiantes = nuevo_valor
        else:
            ValueError('El número de estudiantes debe de ser un entero positivo.')
    
    @property
    def nivel(self) -> str:
        return self._nivel
    
    @property
    def idioma(self) -> str:
        return self._idioma
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @property
    def clave(self) -> str:
        return self._clave
    
    @property
    def beneficio(self) -> float:
        return self._beneficio