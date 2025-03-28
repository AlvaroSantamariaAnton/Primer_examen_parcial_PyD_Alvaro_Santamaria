"""
Módulo encargado de simular la recepción de imágenes desde diferentes satélites.
"""

import time
import random

def receive_images(image_queue, stop_event):
    """
    1.  Para gestionar la llegada constante e impredecible de imágenes y su
        posterior procesamiento lento, aseguramos que no se pierdan datos 
        empleando una cola de multiprocessing (image_queue). Esto permite que 
        las imágenes se vayan acumulando en la cola mientras se procesan en 
        paralelo, sin bloquear la recepción.

        He decidido usar multiprocessing en lugar de threading porque la
        recepción de imágenes puede ser intensiva en CPU y se evita el GIL.

        Se simula la recepción de nuevas 'imágenes' (en este caso, cadenas de texto)
        con un retardo aleatorio para imitar la naturaleza impredecible de la llegada
        de datos. Cada nueva imagen se coloca en la cola para ser procesada.
    """

    image_count = 0
    while not stop_event.is_set():
        # Simular la creación/recepción de una imagen
        image_data = f"Imagen_{image_count}"
        print(f"[RECEPCION] Recibida {image_data}")

        # Insertar la imagen en la cola
        image_queue.put(image_data)

        image_count += 1

        # Simular un tiempo de llegada impredecible (entre 0.5 y 2 segundos)
        time.sleep(random.uniform(0.5, 2.0))