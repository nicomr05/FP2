import sys
from array_queue import ArrayQueue, Proceso, GestorColas

class SimuladorProcesos:
    '''
    Clase del simulador de procesos, que extraerá información de un archivo de texto y
    creará los procesos a ejecutar.
    
    Methods 
    ------- 
    __init__(self):
        Asigna atributos al objeto.   
        
    crear_procesos(self, texto:str): 
        Crea los procesos a partir de un archivo de texto.
    '''
    def __init__(self) -> None:
        '''
        Clase del simulador de procesos, que extraerá información de un archivo de texto y
        creará los procesos a ejecutar.
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
        cola_entrada : ArrayQueue
         Cola de registro con los procesos a ejecutar.
        '''
        cola_entrada: ArrayQueue = ArrayQueue()
        lineas: str = texto.split('\n')
        
        for linea in lineas[0:-1]: # Siempre hay una línea vacía al final del archivo, por lo que no la cogeremos.
            
            partes_linea: str = str(linea.split(' '))
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
    '''
    with open(sys.argv[1]) as f:
        texto_procesos: str = f.read()
        
        simulador = SimuladorProcesos()
        cola_principal: ArrayQueue = simulador.crear_procesos(texto_procesos)
        
        gestor = GestorColas()
        
        while not cola_principal.is_empty():
            
            proceso_actual: Proceso = cola_principal.dequeue()
            gestor.add_proceso(proceso_actual)
            
            print(f'Proceso añadido a cola de ejecución: {proceso_actual}')

            if proceso_actual.ID_usuario not in gestor.penalizados:
                gestor.ejecutar(proceso_actual, simulador.tiempo)
                
                if proceso_actual.ID_usuario not in gestor.penalizados and proceso_actual.tiempo_real > 5 and proceso_actual.tiempo_estimado == 'short':
                    gestor.penalizados.append(proceso_actual.ID_usuario)
            
            else:
                proceso_erroneo: Proceso = gestor.buffer[proceso_actual.recurso]['short'].dequeue()
                gestor.buffer[proceso_erroneo.recurso]['long'].enqueue(proceso_erroneo)
            
            print(gestor.penalizados)
            
            if gestor.proceso_terminado(proceso_actual, simulador.tiempo):
                gestor.ejecucion[proceso_actual.recurso][proceso_actual.tiempo_estimado] = None
            
            proceso_actual.tiempo_entrada = simulador.tiempo
            simulador.tiempo += 1
        
        #Comprobador de los elementos de diccionario de ejecución:
        print()
        for r in gestor.ejecucion.keys():
            for l in gestor.ejecucion[r].keys():
                print(gestor.ejecucion[r][l])
        

if __name__ == '__main__':
    main()