import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Colores
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)

# Creación de la ventana
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Colonización Espacial")

# Clase para la nave del jugador


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO_PANTALLA // 4, ALTO_PANTALLA // 2)
        self.velocidad = 5

    def update(self):
        # Movimiento de la nave
        teclas_pulsadas = pygame.key.get_pressed()
        if teclas_pulsadas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        elif teclas_pulsadas[pygame.K_DOWN]:
            self.rect.y += self.velocidad

        # Restricciones de movimiento
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= ALTO_PANTALLA - self.rect.height:
            self.rect.y = ALTO_PANTALLA - self.rect.height

# Clase para los obstáculos


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, random.randint(30, 100)))
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO_PANTALLA
        self.rect.y = random.randint(0, ALTO_PANTALLA - self.rect.height)
        self.velocidad = random.randint(1, 5)

    def update(self):
        # Movimiento del obstáculo
        self.rect.x -= self.velocidad
        if self.rect.right <= 0:
            self.rect.x = ANCHO_PANTALLA
            self.rect.y = random.randint(0, ALTO_PANTALLA - self.rect.height)
            self.velocidad = random.randint(1, 5)


# Grupos de sprites
todos_los_sprites = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()

# Creación de la nave del jugador
nave = Nave()
todos_los_sprites.add(nave)

# Creación de los obstáculos
for _ in range(10):
    obstaculo = Obstaculo()
    todos_los_sprites.add(obstaculo)
    obstaculos.add(obstaculo)

# Reloj para controlar la velocidad de actualización de la pantalla
reloj = pygame.time.Clock()

# Bucle principal del juego
jugando = True
while jugando:
    # Actualización de sprites
    todos_los_sprites.update()

    # Comprobación de colisiones entre la nave y los obstáculos
    if pygame.sprite.spritecollide(nave, obstaculos, False):
        # Restar una vida o finalizar el juego si no quedan vidas
        pass

    # Eventos del juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Renderizado de la pantalla
    pantalla.fill(BLANCO)
    todos_los_sprites.draw(pantalla)
    pygame.display.flip()

    # Control de la velocidad de actualización
    reloj.tick(60)

# Cierre de Pygame
pygame.quit()
