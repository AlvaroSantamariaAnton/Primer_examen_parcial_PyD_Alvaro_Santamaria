"""
Archivo principal que gestiona la recepción y el procesamiento de las imágenes
de forma concurrente, utilizando multiprocessing (programación con procesos).

En los comentarios de los diferentes módulos se incluyen las respuestas a las
preguntas enumeradas (1 a 4). He modificado algunas respuestas respecto al
supuesto práctico.
"""

import multiprocessing
import time
import reception
import processing

def main():
    # Creamos una cola de multiprocessing para compartir datos entre procesos
    image_queue = multiprocessing.Queue()
    # Creamos un evento para señalar el fin de la ejecución
    stop_event = multiprocessing.Event()

    # Creamos dos procesos: uno para la recepción de imágenes y otro para el procesamiento
    receiver_process = multiprocessing.Process(
        target=reception.receive_images, 
        args=(image_queue, stop_event),
        name="ReceiverProcess"
    )
    processor_process = multiprocessing.Process(
        target=processing.process_images, 
        args=(image_queue, stop_event),
        name="ProcessorProcess"
    )

    # Iniciamos ambos procesos
    receiver_process.start()
    processor_process.start()

    # Dejamos que el sistema funcione durante un tiempo simulado (por ejemplo, 30 segundos)
    """
    Esto solo aplica a la recepción de imágenes, ya que el procesamiento se realiza
    hasta que se finaliza de procesar la última imagen en la cola.
    """
    time.sleep(30)

    # Señalamos a ambos procesos que deben detenerse
    stop_event.set()

    # Esperamos a que terminen
    receiver_process.join()
    processor_process.join()

if __name__ == "__main__":
    main()