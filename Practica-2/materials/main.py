import sys
from array_queue import Proceso, GestorColas

class SimuladorProcesos:
    
    def crear_procesos(self, texto:str):
        
        lista_procesos = []
        lineas = texto.split('\n')
        
        for linea in lineas[0:-1]:
            
            partes_linea = linea.split(' ')

            ID_proceso = partes_linea[0]
            ID_usuario = partes_linea[1]
            recurso = partes_linea[2]
            tiempo_estimado = partes_linea[3]
            tiempo_real = partes_linea[4]
            
            proceso = Proceso(ID_proceso= ID_proceso, ID_usuario= ID_usuario, recurso= recurso, tiempo_estimado= tiempo_estimado, tiempo_real= tiempo_real)
            
            lista_procesos.append(proceso)
        
        gestor = GestorColas(procesos= lista_procesos)
        
        return gestor
    

def main():
    '''
    Función principal que lee el archivo y ejecuta la simulación de los procesos.
    '''
    with open(sys.argv[1]) as f:
        texto_procesos = f.read()
        
        simulador = SimuladorProcesos()
        
        for i in simulador.crear_procesos(texto_procesos).procesos:
            print(i)

if __name__ == '__main__':
    main()