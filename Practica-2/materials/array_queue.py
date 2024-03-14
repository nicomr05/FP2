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
    '''
    def __init__(self, ID_proceso:str, ID_usuario:str, recurso:str, tiempo_estimado:str, tiempo_real:int):
        self._ID_proceso = ID_proceso
        self._ID_usuario = ID_usuario
        self._recurso = recurso
        self._tiempo_estimado = tiempo_estimado
        self._tiempo_real = tiempo_real
    
    def __str__(self) -> str:
        cadena = f'{self.ID_proceso}'
        cadena += f'    {self.ID_usuario}'
        cadena += f'    {self.recurso}'
        cadena += f'    {self.tiempo_estimado}'
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
            ValueError('El tiempo estimado tiene que ser un string de longitud mayor que 0.')

class GestorColas:
    
    def __init__(self, procesos):
        self._procesos = procesos

    @property
    def procesos(self) -> list:
        return self._procesos
    
    @procesos.setter
    def procesos(self, nueva_lista):
        if isinstance(nueva_lista, list) and len(nueva_lista) > 0:
            self._procesos = nueva_lista
        else:
            ValueError('La lista de procesos debe ser una lista con elementos.')