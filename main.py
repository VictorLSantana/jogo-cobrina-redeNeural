
import pygame
import random

pygame.init()

# Setup
LARGURA_TELA = 1280
ALTURA_TELA = 720
FPS = 120
rodando = True
velocidade = 10
tamanho_quadrado = 40
x_alimento = random.randint(0,LARGURA_TELA-tamanho_quadrado)
y_alimento = random.randint(0,ALTURA_TELA-tamanho_quadrado)
print(x_alimento, y_alimento)

# Cores e fonte
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)
fonte = pygame.font.Font(None, 36)

# Função para fim do jogo
def game_over():
    texto = fonte.render("GAME OVER", True, vermelho)
    tela.blit(texto, (LARGURA_TELA/2, ALTURA_TELA/2))
    pygame.display.flip()
    pygame.time.wait(4000)
    return False

# Função para gerar alimento para cobra
def alimento_cobra(x_alimento, y_alimento):
    pygame.draw.rect(tela, verde, (x_alimento, y_alimento, tamanho_quadrado/2, tamanho_quadrado/2))
    pygame.display.flip()

    


tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()

x, y = LARGURA_TELA/2, ALTURA_TELA/2

while rodando:
    
    evento = pygame.event.get()
    
    for evento in evento:
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    
    # Mover para esquerda
    if teclas[pygame.K_LEFT]:
        x -= velocidade
        if x < -1:
            rodando = game_over()
    
    # Mover para direita
    if teclas[pygame.K_RIGHT]:
        x += velocidade
        if x > LARGURA_TELA-tamanho_quadrado+1:
            rodando = game_over()
    
    # Mover para cima
    if teclas[pygame.K_UP]:
        y -= velocidade
        if y < -1:
            rodando = game_over()
    
    # Mover para baixo    
    if teclas[pygame.K_DOWN]:
        y += velocidade
        if y > ALTURA_TELA-tamanho_quadrado+1:
            rodando = game_over()
    
    # Alimento
    if teclas[pygame.K_a]:
        alimento_cobra()
    
    # Auxiliar
    if teclas[pygame.K_SPACE]:
        print(x,y)
        print(rodando)

    tela.fill(preto)
    pygame.draw.rect(tela, branco, (x, y, tamanho_quadrado, tamanho_quadrado))
    alimento_cobra(x_alimento, y_alimento)
    pygame.display.flip()
    relogio.tick(FPS)

pygame.quit()