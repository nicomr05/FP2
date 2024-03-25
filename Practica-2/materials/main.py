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
        
        print(cola_entrada)
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
            
            simulador.tiempo += 1
            
            proceso_actual: Proceso = cola_principal.dequeue()
            gestor.add_proceso_en_cola_ejecucion(proceso_actual)
            proceso_actual.tiempo_entrada = simulador.tiempo

            print(f'Proceso añadido a cola de ejecución: {proceso_actual}')

        while not gestor.buffer_is_empty():
            
            for recurso in gestor.buffer.keys():
                for longitud in gestor.buffer[recurso].keys():
                    print(gestor.buffer[recurso][longitud])
                    if not gestor.buffer[recurso][longitud].is_empty():
                        gestor.ejecutar(gestor.buffer[recurso][longitud].first(), simulador.tiempo)
                        break
                
                                    
            if proceso_actual.ID_usuario not in gestor.penalizados:
                gestor.ejecutar(proceso_actual, simulador.tiempo)
                gestor.penalizar(proceso_actual, simulador)
                    
            else:
                proceso_erroneo: Proceso = gestor.buffer[proceso_actual.recurso]['short'].dequeue()
                gestor.buffer[proceso_erroneo.recurso]['long'].enqueue(proceso_erroneo)
                gestor.penalizados.remove(proceso_erroneo.ID_usuario)
                
            for usuario in gestor.penalizados:
                print(f'Penalización activa: {simulador.tiempo} {usuario}\n')

                
                
        # Bucles que muestran los elementos de los diccionarios de
        # colas de ejecución y ejecución respectivamente:
        
        print()
        for r in gestor.buffer.keys():
            for l in gestor.buffer[r].keys():
                print(gestor.buffer[r][l])
                
        print()
        for r in gestor.ejecucion.keys():
            for l in gestor.ejecucion[r].keys():
                print(gestor.ejecucion[r][l])
        

if __name__ == '__main__':
    main()