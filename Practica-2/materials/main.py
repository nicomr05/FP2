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
    def __init__(self):
        '''
        Clase del simulador de procesos, que extraerá información de un archivo de texto y
        creará los procesos a ejecutar.
        '''
        self._tiempo = 0
    
    def crear_procesos(self, texto:str):
        '''
        Función que extrae las lineas de un string, crea los procesos a ejecutar
        mediante la clase Proceso y los mete en una cola de entrada de procesos.
        
        Parameters
        ----------
        texto : str
         String con las líneas que contienen la información de los procesos.
        '''
        cola_entrada = ArrayQueue()
        lineas = texto.split('\n')
        
        for linea in lineas[0:-1]: # Siempre hay una línea vacía al final del archivo, por lo que no la cogeremos.
            
            partes_linea = linea.split(' ')

            ID_proceso = partes_linea[0]
            ID_usuario = partes_linea[1]
            recurso = partes_linea[2]
            tiempo_estimado = partes_linea[3]
            tiempo_real = partes_linea[4]
            
            proceso = Proceso(ID_proceso= ID_proceso, ID_usuario= ID_usuario, recurso= recurso, tiempo_estimado= tiempo_estimado, tiempo_real= tiempo_real)
            
            cola_entrada.enqueue(proceso)
        
        return cola_entrada
    
    @property
    def tiempo(self) -> int:
        return self._tiempo
    
    @tiempo.setter
    def tiempo(self, nuevo_tiempo):
        if isinstance(nuevo_tiempo, int) and nuevo_tiempo >= 0:
            self._tiempo = nuevo_tiempo
        else:
            ValueError('El tiempo debe ser un entero positivo.')
    

def main():
    '''
    Función principal que lee el archivo y ejecuta la simulación de los procesos.
    '''
    with open(sys.argv[1]) as f:
        texto_procesos = f.read()
        
        simulador = SimuladorProcesos()
        cola_principal = simulador.crear_procesos(texto_procesos)
        
        gestor = GestorColas()
        
        for i in len(cola_principal):
            
            proceso_actual = cola_principal.dequeue()
            
            if proceso_actual.recurso == 'CPU':
                if proceso_actual.tiempo_estimado == 'short': # No detecta que el proceso actual sea de tipo Proceso.
                    gestor.buffer['CPU']['short']
                if proceso_actual.tiempo_estimado == 'long': # No detecta que el proceso actual sea de tipo Proceso.
                    gestor.buffer['CPU']['long']
                    
            if proceso_actual.recurso == 'GPU':
                if proceso_actual.tiempo_estimado == 'short': # No detecta que el proceso actual sea de tipo Proceso.
                    gestor.buffer['GPU']['short']
                if proceso_actual.tiempo_estimado == 'long': # No detecta que el proceso actual sea de tipo Proceso.
                    gestor.buffer['GPU']['long']
            
            simulador.tiempo += 1
        

if __name__ == '__main__':
    main()