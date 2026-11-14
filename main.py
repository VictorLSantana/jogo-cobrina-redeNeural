
import pygame

# Setup
LARGURA_TELA = 1280
ALTURA_TELA = 720
FPS = 60
rodando = True

# Cores 
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)

pygame.init()

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()

x, y = LARGURA_TELA/2, ALTURA_TELA/2
velocidade = 5

while rodando:
    
    evento = pygame.event.get()
    
    for evento in evento:
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    tela.fill((30, 30, 30))
    pygame.draw.rect(tela, branco, (x, y, 40, 40))
    pygame.display.flip()
    relogio.tick(FPS)

pygame.quit()