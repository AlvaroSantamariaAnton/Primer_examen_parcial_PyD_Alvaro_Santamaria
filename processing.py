"""
Módulo encargado de simular el procesamiento y análisis de las imágenes recibidas.
"""

import time

def process_images(image_queue, stop_event):
    """
    2.  Se utiliza una estructura de datos tipo cola (Queue) para gestionar
        las imágenes pendientes de procesar. Esto se justifica porque una cola FIFO
        (First In, First Out) es natural para flujos de datos y asegura que se
        mantenga el orden de llegada, evitando pérdidas de información.

    3.  Si no se utiliza una gestión adecuada del almacenamiento temporal (por ejemplo,
        si no existiera la cola o fuese muy pequeña), se podrían perder imágenes cuando 
        llegasen ráfagas de datos. Además, el sistema podría bloquearse si el procesamiento
        es muy lento y no hay espacio para las imágenes entrantes. Para mitigarlo, se puede
        configurar la cola con un tamaño adecuado, usar almacenamiento en disco en caso de
        overflow y escalar el número de procesos de procesamiento si la carga aumenta.

    4.  Para organizar el trabajo concurrente, un proceso se dedica a recibir 
        las imágenes (reception.py) y otro proceso a procesarlas (este archivo). De esta forma,
        ambas tareas se ejecutan de manera independiente y simultánea. El proceso de recepción
        no se ve bloqueado por el procesamiento lento y viceversa, optimizando el flujo global.
    """

    # Mientras no se solicite el fin y haya imágenes en la cola, seguimos procesando
    while not stop_event.is_set() or not image_queue.empty():
        try:
            # Extraer la imagen de la cola (con timeout para no bloquear indefinidamente)
            image_data = image_queue.get(timeout=1)
            print(f"[PROCESAMIENTO] Procesando {image_data}...")
            
            # Simular un procesamiento complejo y lento
            time.sleep(3)
            
            print(f"[PROCESAMIENTO] Finalizado {image_data}")
        except:
            # Si la cola está vacía momentáneamente, continuar
            pass