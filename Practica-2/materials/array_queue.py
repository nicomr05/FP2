'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""

    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned

    def __str__(self):
        s = "[\n"
        for i in range(self._front, self._size):
            s += "\t" + self._data[i].__str__() + "\n"
        s += "]\n"
        return s

class Proceso:
    '''
    Clase abstracta para un proceso.
    Esta clase tiene por atributos un identificador para el proceso y otro para
    el usuario que lo requiere, un marcador para el tipo de recurso que necesita
    el proceso, el tiempo necesario estimado para la completación del proceso y
    el tiempo real que costará procesarlo en unidades enteras.
    
    Attributes 
    ---------- 
    ID_proceso : str
     Identificador de un proceso.
     
    ID_usuario : str
     Identificador de un usuario.
     
    recurso : str
     Tipo de recurso (CPU/GPU).
     
    tiempo_estimado : str
     Aproximación del tiempo que durará una instrucción.
     
    tiempo_real : int
     Unidades de tiempo que realmente le costarán a la máquina ejecutar el proceso.
     
    tiempo_arranque : int
     Momento en unidades de tiempo en el que se inició la ejecución del proceso.
     
    tiempo_entrada : int
     Momento en unidades de tiempo en el que el proceso entró a la cola de ejecución.
    
    Methods 
    ------- 
    __init__(self) -> None: 
        Asigna atributos al objeto.
        
    __str__(self) -> str:
        Devuelve un string informativo sobre el proceso y todos sus atributos.
    '''
    def __init__(self, ID_proceso:str, ID_usuario:str, recurso:str, tiempo_estimado:str, tiempo_real:int) -> None:
        '''
        Clase abstracta para un proceso.
        Esta clase tiene por atributos un identificador para el proceso y otro para
        el usuario que lo requiere, un marcador para el tipo de recurso que necesita
        el proceso, el tiempo necesario estimado para la completación del proceso y
        el tiempo real que costará procesarlo en unidades enteras.
        
        Attributes
        ---------- 
        ID_proceso : str
         Identificador de un proceso.
         
        ID_usuario : str
         Identificador de un usuario.
         
        recurso : str
         Tipo de recurso (CPU/GPU).
         
        tiempo_estimado : str
         Aproximación del tiempo que durará una instrucción.
         
        tiempo_real : int
         Unidades de tiempo que realmente le costarán a la máquina.
        
        Methods 
        ------- 
        __init__(self) -> None: 
            Asigna atributos al objeto.
            
        __str__(self) -> str:
            Devuelve un string informativo sobre el proceso y todos sus atributos.
        '''
        self._ID_proceso: str = ID_proceso
        self._ID_usuario: str = ID_usuario
        self._recurso: str = recurso
        self._tiempo_estimado: str = tiempo_estimado
        self._tiempo_real: int = tiempo_real
        self._tiempo_arranque: int = 0
        self._tiempo_entrada: int = 0
    
    def __str__(self) -> str:
        '''
        Función que se llama al intentar hacer un print() sobre un objeto Proceso.
        Muestra la ID del proceso, la ID del usuario, el recurso necesario para ejecutar
        el proceso, el tiempo estimado para completarlo (short/long) y las unidades de
        tiempo necesarias para completar la ejecución.

        Returns
        -------
        str
         String informativo de un Proceso.
        '''
        cadena =  f'{self.ID_proceso}'
        cadena += f'  {self.ID_usuario}'
        cadena += f'  {self.recurso}'
        cadena += f'  {self.tiempo_estimado}'
        return cadena

    
    @property
    def ID_proceso(self) -> str:
        return self._ID_proceso
    
    @property
    def ID_usuario(self) -> str:
        return self._ID_usuario
    
    @property
    def recurso(self) -> str:
        return self._recurso
    
    @property
    def tiempo_estimado(self) -> str:
        return self._tiempo_estimado
    
    @property
    def tiempo_real(self) -> int:
        return self._tiempo_real
    
    @property
    def tiempo_arranque(self) -> int:
        return self._tiempo_arranque
    
    @property
    def tiempo_entrada(self) -> int:
        return self._tiempo_entrada
    
    @ID_proceso.setter
    def ID_proceso(self, nueva_ID):
        if isinstance(nueva_ID, str) and len(nueva_ID) > 0:
            self._ID_proceso = nueva_ID
        else:
            ValueError('La ID de proceso tiene que ser un string de longitud mayor que 0.')

    @ID_usuario.setter
    def ID_usuario(self, nueva_ID):
        if isinstance(nueva_ID, str) and len(nueva_ID) > 0:
            self._ID_usuario = nueva_ID
        else:
            ValueError('La ID de usuario tiene que ser un string de longitud mayor que 0.')

    @recurso.setter
    def recurso(self, nuevo_recurso):
        if isinstance(nuevo_recurso, str) and len(nuevo_recurso) > 0 and nuevo_recurso in ['cpu','gpu']:
            self._recurso = nuevo_recurso
        else:
            ValueError('El tipo de recurso tiene que ser o "cpu" o "gpu".')
            
    @tiempo_estimado.setter
    def tiempo_estimado(self, nuevo_tiempo):
        if isinstance(nuevo_tiempo, str) and len(nuevo_tiempo) > 0 and nuevo_tiempo in ['long','short']:
            self._tiempo_estimado = nuevo_tiempo
        else:
            ValueError('El tiempo estimado tiene que ser o "long" o "short".')
    
    @tiempo_real.setter
    def tiempo_real(self, nuevo_tiempo):
        if isinstance(nuevo_tiempo, int) and nuevo_tiempo > 0:
            self._tiempo_real = nuevo_tiempo
        else:
            ValueError('El tiempo real tiene que ser un entero positivo.')
    
    @tiempo_arranque.setter
    def tiempo_arranque(self, nuevo_tiempo):
        if isinstance(nuevo_tiempo, int) and nuevo_tiempo > 0:
            self._tiempo_arranque = nuevo_tiempo
        else:
            ValueError('El tiempo de arranque tiene que ser un entero positivo.')
    
    @tiempo_entrada.setter
    def tiempo_entrada(self, nuevo_tiempo):
        if isinstance(nuevo_tiempo, int) and nuevo_tiempo > 0:
            self._tiempo_entrada = nuevo_tiempo
        else:
            ValueError('El tiempo de entrada tiene que ser un entero positivo.')

class GestorColas:
    '''
    Clase del gestor de colas, que organiza los procesos en 4 colas según el recurso necesario,
    gestiona las penalizaciones de los usuarios y el almacenamiento temporal de los procesos en
    ejecución en cada recurso.
    
    Methods 
    ------- 
    __init__(self) -> None:
        Asigna atributos al objeto.
        
    add_proceso_en_cola_ejecucion(self, proceso:Proceso) -> Proceso:
        Añade un proceso a la cola de ejecución correspondiente según la duración aproximada del
        mismo y el recurso que requiera.
        
    proceso_terminado(self, proceso:Proceso, tiempo:int) -> bool:
        Nos permite revisar si un proceso ha terminado de ejecutarse.
        
    ejecutar(self, proceso:Proceso, tiempo:int) -> Proceso:
        Inserta un proceso en el diccionario de ejecución correspondiente según el
        tipo de recurso que necesita el proceso y la duración aproximada del mismo.
        Esto ocurre únicamente cuando no hay ya un proceso en ejecución en la cola
        correspondiente.
        
    penalizar(self, proceso:Proceso, tiempo:int) -> None:
        Añade al usuario del proceso indicado al conjunto de penalizados únicamente
        si el tiempo estimado del proceso es "short" y el tiempo que duró su ejecución fue mayor
        que cinco unidades.
        
    ejecucion_is_empty(self) -> bool:
        Comprueba si el diccionario de ejecución no está vacío.
    '''
    def __init__(self) -> None:
        '''
        Clase del gestor de colas, que organiza los procesos en 4 colas según el recurso necesario,
        gestiona las penalizaciones de los usuarios y el almacenamiento temporal de los procesos en
        ejecución en cada recurso.
        
        Methods 
        ------- 
        __init__(self) -> None:
            Asigna atributos al objeto.

        add_proceso_en_cola_ejecucion(self, proceso:Proceso) -> Proceso:
            Añade un proceso a la cola de ejecución correspondiente según la duración aproximada del
            mismo y el recurso que requiera.

        proceso_terminado(self, proceso:Proceso, tiempo:int) -> bool:
            Nos permite revisar si un proceso ha terminado de ejecutarse.

        ejecutar(self, proceso:Proceso, tiempo:int) -> Proceso:
            Inserta un proceso en el diccionario de ejecución correspondiente según el
            tipo de recurso que necesita el proceso y la duración aproximada del mismo.
            Esto ocurre únicamente cuando no hay ya un proceso en ejecución en la cola
            correspondiente.

        penalizar(self, proceso:Proceso, tiempo:int) -> None:
            Añade al usuario del proceso indicado al conjunto de penalizados únicamente
            si el tiempo estimado del proceso es "short" y el tiempo que duró su ejecución fue mayor
            que cinco unidades.

        ejecucion_is_empty(self) -> bool:
            Comprueba si el diccionario de ejecución está vacío.
        '''
        self._penalizados: set[str] = set()

        self._buffer: dict[str, dict[str, ArrayQueue[Proceso]]] = {
            'cpu':{
                'short':ArrayQueue(),
                'long': ArrayQueue()
            },
            'gpu':{
                'short':ArrayQueue(),
                'long': ArrayQueue()
            }
        }
        
        self._ejecucion: dict[str, dict[str, None|Proceso]] = {
            'cpu':{
                'short':None,
                'long': None
            },
            'gpu':{
                'short':None,
                'long': None
            }
        }
    
    def add_proceso_en_cola_ejecucion(self, proceso:Proceso) -> Proceso:
        '''
        Función que añade un proceso a una cola de ejecución según el recurso que requiera y
        la duración aproximada del proceso.
        
        Parameters
        ----------
        proceso : Proceso
         Proceso que se quiere añadir.
        
        Returns
        -------
        Proceso
         Mismo proceso que se añade.
        '''
        self.buffer[proceso.recurso][proceso.tiempo_estimado].enqueue(proceso)
        print(f'Proceso añadido a cola de ejecución: {proceso}\n')

        return proceso
    
    def proceso_terminado(self, proceso:Proceso, tiempo:int) -> bool:
        '''
        Función que nos permite revisar si un proceso ha terminado de ejecutarse.

        Parameters
        ----------
        proceso : Proceso
         Proceso del que se quiere comprobar si se ha terminado su ejecución.
        tiempo : int
         Tiempo en el que se quiere realizar la comprobación.

        Returns
        -------
        bool
         True si el proceso ha terminado.
         False si el proceso no ha terminado aún.
        '''
        if tiempo >= proceso.tiempo_arranque + proceso.tiempo_real:
            
            print(f'Proceso terminado:\nTiempo actual: {tiempo}\nProceso: {proceso}\nTiempo de entrada: {proceso.tiempo_entrada}\nTiempo de arranque: {proceso.tiempo_arranque}\n{tiempo - proceso.tiempo_arranque}\n')

            return True
        
        else:
            return False
    
    def ejecutar(self, proceso:Proceso, tiempo:int) -> Proceso:
        '''
        Función que inserta un proceso en el diccionario de ejecución correspondiente según
        el tipo de recurso que necesita el proceso y la duración aproximada del mismo.
        Esto ocurre únicamente cuando no hay ya un proceso en ejecución en la cola correspondiente.

        Parameters
        ----------
        proceso : Proceso
         Proceso que se quiere ejecutar.
        tiempo : int
         Tiempo de arranque del proceso.
        
        Returns
        -------
        Proceso
         Mismo proceso que se ejecuta.
        '''
        if self.ejecucion[proceso.recurso][proceso.tiempo_estimado] is None:
            proceso.tiempo_arranque = tiempo
            self.ejecucion[proceso.recurso][proceso.tiempo_estimado] = proceso
            
            return proceso
        
        return proceso
    
    def penalizar(self, proceso:Proceso, tiempo:int) -> None:
        '''
        Función que añade al usuario del proceso indicado al conjunto de penalizados únicamente
        si el tiempo estimado del proceso es "short" y el tiempo que duró su ejecución fue mayor
        que cinco unidades.
        
        Parameters
        ----------
        proceso : Proceso
         Proceso del que se saca la información del usuario.
        tiempo : int
         Unidades de tiempo actuales.
        
        Returns
        -------
        None
        '''
        if tiempo - proceso.tiempo_arranque > 5 and proceso.tiempo_estimado == 'short':
            self.penalizados.add(proceso.ID_usuario)
            
            print(f'Penalización aplicada: {tiempo} {proceso.ID_usuario}\n')
        
    def ejecucion_is_empty(self) -> bool:
        '''
        Función que comprueba si el diccionario de ejecución está vacío.
        
        Returns
        -------
        bool
         True si el diccionario ejecucion está vacío.
         False si el diccionario ejecucion no está vacío.
        '''
        for recurso in self.ejecucion.keys():
            for longitud in self.ejecucion[recurso].keys():
                if self.ejecucion[recurso][longitud] is not None:
                    return False
        return True
    
    def buffer_is_empty(self) -> bool:
        '''
        Función que comprueba si el buffer está vacío.
        
        Returns
        -------
        bool
         True si el diccionario ejecucion está vacío.
         False si el diccionario ejecucion no está vacío.
        '''
        for recurso in self.buffer.keys():
            for longitud in self.buffer[recurso].keys():
                if self.buffer[recurso][longitud] is not None:
                    return False
        return True
    
    @property
    def buffer(self) -> dict:
        return self._buffer
    
    @property
    def ejecucion(self) -> dict:
        return self._ejecucion
    
    @property
    def penalizados(self) -> set[str]:
        return self._penalizados