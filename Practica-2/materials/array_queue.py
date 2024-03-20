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
     Unidades de tiempo que realmente le costarán a la máquina.
    
    Methods 
    ------- 
    __init__(self): 
        Asigna atributos al objeto.
    __str__(self) -> None:
        Devuelve un string informativo sobre el proceso y todos sus atributos.
    '''
    def __init__(self, ID_proceso:str, ID_usuario:str, recurso:str, tiempo_estimado:str, tiempo_real:int):
        '''
        Clase abstracta para un proceso.
        Esta clase tiene por atributos un identificador para el proceso y otro para
        el usuario que lo requiere, un marcador para el tipo de recurso que necesita
        el proceso, el tiempo necesario estimado para la completación del proceso y
        el tiempo real que costará procesarlo en unidades enteras.
        
        Parameters 
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
        '''
        self._ID_proceso = ID_proceso
        self._ID_usuario = ID_usuario
        self._recurso = recurso
        self._tiempo_estimado = tiempo_estimado
        self._tiempo_real = tiempo_real
        self._tiempo_arranque = 0
        self._tiempo_entrada = 0
    
    def __str__(self) -> str:
        cadena =  f'{self.ID_proceso}'
        cadena += f'\t{self.ID_usuario}'
        cadena += f'\t{self.recurso}'
        cadena += f'\t{self.tiempo_estimado}'
        cadena += f' ({self.tiempo_real})'
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
    __init__(self):
        Asigna atributos al objeto.
    '''
    def __init__(self):
        '''
        Clase del gestor de colas, que organiza los procesos en 4 colas según el recurso necesario,
        gestiona las penalizaciones de los usuarios y el almacenamiento temporal de los procesos en
        ejecución en cada recurso.
        '''
        self._penalizados = []
        
        self._buffer = {
            'cpu':{
                'short':ArrayQueue(),
                'long': ArrayQueue()
            },
            'gpu':{
                'short':ArrayQueue(),
                'long': ArrayQueue()
            }
        }
        
        self._ejecucion = {
            'cpu':{
                'short':None,
                'long': None
            },
            'gpu':{
                'short':None,
                'long': None
            }
        }
    
    def add_proceso(self, proceso:Proceso) -> Proceso:
        '''
        
        Parameters
        ----------
        
        '''
        self.buffer[proceso.recurso][proceso.tiempo_estimado] = proceso
        
        return proceso
    
    def proceso_terminado(self, proceso:Proceso, tiempo:int) -> bool:
        if tiempo >= proceso.tiempo_arranque + proceso.tiempo_real:
            return True
        else:
            return False
    
    def ejecutar(self, proceso:Proceso, tiempo:int) -> Proceso:
        '''
        '''
        if self.ejecucion[proceso.recurso][proceso.tiempo_estimado] != None and self.proceso_terminado(proceso, tiempo):
            self.ejecucion[proceso.recurso][proceso.tiempo_estimado] = proceso
            return proceso
            
        elif self.ejecucion[proceso.recurso][proceso.tiempo_estimado] == None:
            self.ejecucion[proceso.recurso][proceso.tiempo_estimado] = proceso
            return proceso
    
    @property
    def buffer(self) -> dict:
        return self._buffer
    
    @property
    def ejecucion(self) -> dict:
        return self._ejecucion
    
    @property
    def penalizados(self) -> list:
        return self._penalizados
