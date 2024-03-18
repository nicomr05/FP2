import sys
from array_queue import ArrayQueue, Proceso, GestorColas

class SimuladorProcesos:
    '''
    Clase del simulador de procesos, que extraerá información de un archivo de texto y
    creará los procesos a ejecutar.
    
    Attributes 
    ---------- 
    
 
    Methods 
    ------- 
    metodo1(param1): 
        Una línea de resumen. 
    '''
    def crear_procesos(self, texto:str):
        
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
        
        return GestorColas(buffer= cola_entrada)
    

def main():
    '''
    Función principal que lee el archivo y ejecuta la simulación de los procesos.
    '''
    with open(sys.argv[1]) as f:
        texto_procesos = f.read()
        
        simulador = SimuladorProcesos()
        
        for i in simulador.crear_procesos(texto_procesos).buffer:
            print(i)

if __name__ == '__main__':
    main()