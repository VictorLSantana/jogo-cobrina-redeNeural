
import pygame
import random

pygame.init()

# Setup
LARGURA_TELA = 1280
ALTURA_TELA = 720
FPS = 60
rodando = True
velocidade = 10
tamanho_quadrado = 30
x_alimento_inicial = float(random.randint(0,LARGURA_TELA-tamanho_quadrado)) # x inicial do alimento
y_alimento_inicial = float(random.randint(0,ALTURA_TELA-tamanho_quadrado))  # y inicial do alimento
x, y = LARGURA_TELA/2, ALTURA_TELA/2 # Posição inicial da cobra

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
def alimento_cobra_inicial(x_alimento, y_alimento):
    pygame.draw.rect(tela, verde, (x_alimento, y_alimento, tamanho_quadrado/2, tamanho_quadrado/2))

# Função para gerar alimento para cobra
# def alimento_cobra(x_alimento, y_alimento):
#     x_alimento = float(random.randint(0,LARGURA_TELA-tamanho_quadrado)) # x inicial do alimento
#     y_alimento = float(random.randint(0,ALTURA_TELA-tamanho_quadrado))  # y inicial do alimento
#     pygame.draw.rect(tela, verde, (x_alimento, y_alimento, tamanho_quadrado/2, tamanho_quadrado/2))
#     return x_alimento, y_alimento

# Função para aumentar corpo da cobra 
def pegou_alimento():
    x_corpo_cobra = x - tamanho_quadrado
    y_corpo_cobra = y
    pygame.draw.rect(tela, branco, (x_corpo_cobra, y_corpo_cobra, tamanho_quadrado, tamanho_quadrado))
    
# Função para ajudar a debugar mostrando a posição da cobra e do alimento
def ajuda_debugar():
    texto_cobra = fonte.render(f"Cobra: ({x}, {y})", True, vermelho)
    tela.blit(texto_cobra, (10, 10))
    
    
    texto_alimento= fonte.render(f"Alimento: ({x_alimento_inicial}, {y_alimento_inicial})", True, vermelho)
    tela.blit(texto_alimento, (10, 50))
    
    texto_distancia= fonte.render(f"Distancia: ({abs(x - x_alimento_inicial)}, {abs(y - y_alimento_inicial)}, {tamanho_quadrado/2})", True, vermelho)
    tela.blit(texto_distancia, (10, 90))
    
# Colidir com alimento    
def colisao(x, x_alimento, y, y_alimento):
    
    if ((abs(x - x_alimento) <= tamanho_quadrado/2) and 
        (abs(y - y_alimento) <= tamanho_quadrado/2)):
        texto_colisao = fonte.render("Colidiu", True, verde)
        tela.blit(texto_colisao, (LARGURA_TELA/2, 130))
        
         
            
    


tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()


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
    
    
    # Comeu alimento vai aumentar o corpo
    if teclas[pygame.K_c]:
        pegou_alimento()
    


    tela.fill(preto) # Fundo da tela
    ajuda_debugar()  # Posição da cobra e do alimento
    pygame.draw.rect(tela, branco, (x, y, tamanho_quadrado, tamanho_quadrado)) # Desenha cobra
    alimento_cobra_inicial(x_alimento_inicial, y_alimento_inicial) # Desenha alimento
    colisao(x, x_alimento_inicial, y, y_alimento_inicial)
    pygame.display.flip() # Mostra na tela
    relogio.tick(FPS) # FPS

pygame.quit()