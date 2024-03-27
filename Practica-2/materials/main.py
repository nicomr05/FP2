'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

import sys
from time import sleep
from array_queue import ArrayQueue, Proceso, GestorColas

class SimuladorProcesos:
    '''
    Clase del simulador de procesos, que extraerá información de un archivo de texto y
    creará los procesos a ejecutar.
    
    Methods 
    ------- 
    __init__(self) -> None:
        Asigna atributos al objeto.   
        
    crear_procesos(self, texto:str) -> ArrayQueue: 
        Crea los procesos a partir de un archivo de texto.
    '''
    def __init__(self) -> None:
        '''
        Clase del simulador de procesos, que extraerá información de un archivo de texto y
        creará los procesos a ejecutar.

        Methods 
        ------- 
        __init__(self) -> None:
            Asigna atributos al objeto.   

        crear_procesos(self, texto:str) -> ArrayQueue: 
            Crea los procesos a partir de un archivo de texto.
        '''
        self._tiempo: int = 0
    
    def crear_procesos(self, texto:str) -> None:
        '''
        Función que extrae las lineas de un string, crea los procesos a ejecutar
        mediante la clase Proceso y los mete en una cola de entrada de procesos.
        
        Parameters
        ----------
        texto : str
         String con las líneas que contienen la información de los procesos.
        
        Returns
        -------
        ArrayQueue
         Cola de registro con los procesos a ejecutar.
        '''
        cola_entrada: ArrayQueue = ArrayQueue()
        lineas: str = str(texto).split('\n')
        
        for linea in lineas[0:-1]: # Siempre hay una línea vacía al final del archivo, por lo que no la cogeremos.
            
            partes_linea: str = str(linea).split()
            
            ID_proceso: str = str(partes_linea[0])
            ID_usuario: str = str(partes_linea[1])
            recurso: str = str(partes_linea[2])
            tiempo_estimado: str = str(partes_linea[3])
            tiempo_real: int = int(partes_linea[4])
            
            proceso: Proceso = Proceso(ID_proceso= ID_proceso, ID_usuario= ID_usuario, recurso= recurso, tiempo_estimado= tiempo_estimado, tiempo_real= tiempo_real)
            
            cola_entrada.enqueue(proceso)
        
        return cola_entrada
    
    @property
    def tiempo(self) -> int:
        return self._tiempo
    
    @tiempo.setter
    def tiempo(self, nuevo_tiempo:int) -> None:
        if isinstance(nuevo_tiempo, int) and nuevo_tiempo >= 0:
            self._tiempo: int = nuevo_tiempo
        else:
            ValueError('El tiempo debe ser un entero positivo.')
    

def main() -> None:
    '''
    Función principal que lee el archivo y ejecuta la simulación de los procesos.
    
    Returns
    -------
    None
    '''
    with open(sys.argv[1]) as f:
        texto_procesos: str = f.read()
        
        simulador = SimuladorProcesos()
        cola_principal: ArrayQueue = simulador.crear_procesos(texto_procesos)
        
        gestor = GestorColas()
        
        while not (cola_principal.is_empty() and gestor.ejecucion_is_empty()):

            simulador.tiempo += 1 # Iniciamos el contador y hacemos que se repita en cada iteración.

            if not cola_principal.is_empty():
                proceso_actual: Proceso = cola_principal.dequeue() # Extraemos el primer proceso de la cola de registro.
                gestor.add_proceso_en_cola_ejecucion(proceso_actual) # Añadimos ese mismo proceso a la cola de ejecución correspondiente.
                proceso_actual.tiempo_entrada = simulador.tiempo # Fijamos el tiempo de entrada del proceso como el tiempo actual.
        
            for recurso in gestor.ejecucion.keys(): # Comprobamos si existe algún proceso que haya terminado su ejecución. Si es así, lo eliminamos del diccionario.
                for longitud in gestor.ejecucion[recurso].keys():
                    
                    if (gestor.ejecucion[recurso][longitud] is not None) and gestor.proceso_terminado(gestor.ejecucion[recurso][longitud], simulador.tiempo):
                        gestor.penalizar(gestor.ejecucion[recurso][longitud], simulador.tiempo) # Comprobamos si el usuario correspondiente al proceso terminado debe ser penalizado.
                        gestor.ejecucion[recurso][longitud] = None
            

            for recurso in gestor.buffer.keys(): 
                for longitud in gestor.buffer[recurso].keys():
                    
                    if not gestor.buffer[recurso][longitud].is_empty():
                        proceso_a_ejecutar: Proceso = gestor.buffer[recurso][longitud].first() # Seleccionamos el primer proceso de la cola de ejecución correspondiente.
                
                        if (proceso_a_ejecutar.ID_usuario in gestor.penalizados) and gestor.buffer[recurso].keys() == 'short': # Si un proceso estaba en una cola short y el usuario estaba penalizado, se .
                            proceso_erroneo: Proceso = gestor.buffer[recurso]['short'].dequeue()
                            gestor.buffer[recurso]['long'].enqueue(proceso_erroneo)

                            gestor.penalizados.remove(proceso_erroneo.ID_usuario)
                        
                        else:
                            gestor.ejecutar(proceso_a_ejecutar, simulador.tiempo) # Ejecutamos el proceso seleccionado
                            gestor.buffer[proceso_a_ejecutar.recurso][proceso_a_ejecutar.tiempo_estimado].dequeue() # Eliminamos el último proceso del buffer.

if __name__ == '__main__':
    main()