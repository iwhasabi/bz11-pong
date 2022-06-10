import pygame

"""
        - algo de herencia: 

        - cosas fijas como el color y tamaño (ancho, alto)

        - método moverse verticalmente
        - Método chocar: Límite para no salirse de la pantalla
        
        - Método para interactual con la pelota??
    """

class Paleta(pygame.Rect):
    pass

class Pong:

    _ALTO = 600
    _ANCHO = 800
    _MARGEN_LATERAL = 20
    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))

        self.jugador1 = Paleta(
            self._MARGEN_LATERAL,                   #Coordenada X (izquierda)
             (self._ALTO-40)/2,                     #Coordenada Y (altura)
              10,                                   #Ancho
              40                                    #Alto
               )
        self.jugador2 = Paleta(
            self._ANCHO -self._MARGEN_LATERAL -10,   #Coordenada x (izquierda)
             (self._ALTO-40)/2,                      #Coordenada Y (altura)
              10,                                    #Ancho
              40                                     #Alto
              )

    def bucle_principal(self):
        print ("Estoy en el bucle principal")
        #rectangulo = pygame.Rect(0, 0, 20, 30)
        while True:
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.jugador1)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.jugador2)

            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()