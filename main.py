
import pygame
import random

# Setup
tamanho_quadrado = 30
qnt_quadrado = 25

LARGURA_TELA = tamanho_quadrado*qnt_quadrado
ALTURA_TELA = tamanho_quadrado*qnt_quadrado
FPS = 40
rodando = True
velocidade = 10

# Cores e fonte
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)

# Função para fim do jogo
def game_over():
    texto = fonte.render("GAME OVER", True, vermelho)
    tela.blit(texto, (LARGURA_TELA/2, ALTURA_TELA/2))
    pygame.display.flip()
    pygame.time.wait(4000)
    return False

# Função para gerar (x,y) aleatórios
def gerador_pos_aleatorio():
    x = random.randint(1, LARGURA_TELA-tamanho_quadrado)
    y = random.randint(1, ALTURA_TELA-tamanho_quadrado)
    return x, y

# Função para desenhar na tela
def desenha_na_tela(cor, x, y):
    pygame.draw.rect(tela, cor, (x, y, tamanho_quadrado, tamanho_quadrado))

    
# Função para ajudar a debugar mostrando a posição da cobra e do alimento
def ajuda_debugar():
    texto_cobra = fonte.render(f"Cobra: ({x_cobra}, {y_cobra})", True, vermelho)
    tela.blit(texto_cobra, (10, 10))
    
    
    texto_alimento= fonte.render(f"Alimento: ({x_alimento}, {y_alimento})", True, vermelho)
    tela.blit(texto_alimento, (10, 50))
    
    texto_distancia= fonte.render(f"Distancia: ({abs(x_cobra - x_alimento)}, {abs(y_cobra - y_alimento)}, {tamanho_quadrado/2})", True, vermelho)
    tela.blit(texto_distancia, (10, 90))
    
# Colidir com alimento    
def colisao(x_cobra, x_alimento, y_cobra, y_alimento):
    
    if ((abs(x_cobra - x_alimento) <= tamanho_quadrado/2) and 
        (abs(y_cobra - y_alimento) <= tamanho_quadrado/2)):
        texto_colisao = fonte.render("Colidiu", True, verde)
        tela.blit(texto_colisao, (LARGURA_TELA/2, 130))

# Início
pygame.init()
fonte = pygame.font.Font(None, 36)

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()
x_cobra, y_cobra = LARGURA_TELA/2, ALTURA_TELA/2 #Posição inicial da cobrinha
x_alimento, y_alimento = gerador_pos_aleatorio() #Posição inicial do alimento

while rodando:
    
    
    evento = pygame.event.get()
    
    for evento in evento:
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    
    # Mover para esquerda
    if teclas[pygame.K_LEFT]:
        x_cobra -= velocidade
        if x_cobra < -1:
            rodando = game_over()
    
    # Mover para direita
    if teclas[pygame.K_RIGHT]:
        x_cobra += velocidade
        if x_cobra > LARGURA_TELA-tamanho_quadrado+1:
            rodando = game_over()
    
    # Mover para cima
    if teclas[pygame.K_UP]:
        y_cobra -= velocidade
        if y_cobra < -1:
            rodando = game_over()
    
    # Mover para baixo    
    if teclas[pygame.K_DOWN]:
        y_cobra += velocidade
        if y_cobra > ALTURA_TELA-tamanho_quadrado+1:
            rodando = game_over()
    


    tela.fill(preto) # Fundo da tela
    ajuda_debugar()  # Posição da cobra e do alimento
    desenha_na_tela(verde, x_alimento, y_alimento) # Desenha alimento na tela
    desenha_na_tela(branco, x_cobra, y_cobra) # Desenha cobra na tela
    colisao(x_cobra, x_alimento, y_cobra, y_alimento)
    pygame.display.flip() # Mostra na tela
    relogio.tick(FPS) # FPS

pygame.quit()