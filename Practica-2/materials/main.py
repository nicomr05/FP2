from array_queue import Proceso

class SimuladorProcesos:
    
    def crear_procesos(self, texto:str):
        
        lista_procesos = []
        lineas = texto.split(sep= '\n')
        
        for linea in lineas:
            
            partes_linea = linea.split(sep= ' ')
            
            ID_proceso = partes_linea[0]
            ID_usuario = partes_linea[1]
            recurso = partes_linea[2]
            tiempo_estimado = partes_linea[3]
            tiempo_real = partes_linea[4]
            
            proceso = Proceso(ID_proceso= ID_proceso, ID_usuario= ID_usuario, recurso= recurso, tiempo_estimado= tiempo_estimado, tiempo_real= tiempo_real)
            
            lista_procesos.append(proceso)
        
        return lista_procesos
    

def main():
    '''
    Función principal que lee el archivo y ejecuta la simulación de los procesos.
    '''
    pass

if __name__ == '__main__':
    
    tx = 'eiHf3b9i user1007 gpu short 13\neDh3xk9e user1005 gpu short 6\na5NgkKZV user1009 cpu short 5\nAyzruXkM user1003 cpu long 15\nXb7g5R2Z user1005 gpu long 7\ncBJTLcaL user1002 gpu short 3'

    lista = SimuladorProcesos().crear_procesos(tx)
    for i in lista:
        print(i)