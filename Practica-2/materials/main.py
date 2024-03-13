from array_queue import Proceso

class SimuladorProcesos:
    
    def crear_procesos(self, texto:str):
        lineas = texto.split(sep= '\n')
        procesos = []
        
        for linea in lineas:
            partes = linea.split(sep= ' ')
            ID_proceso = partes[0]
            ID_usuario = partes[1]
            recurso = partes[2]
            tiempo_estimado = partes[3]
            timepo_inicio = partes[4]
            
            proceso = Proceso(ID_proceso= ID_proceso, )
            
def main():
    pass

if __name__ == '__main__':
    main()