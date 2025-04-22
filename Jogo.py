import pygame
import time
import random

pygame.init()

# Configuração e criação da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da cobrinha")

# Cores Do JOgo
BRANCO = (255,255,255)
VERDE = (0,255,0)
PRETO = (0,0,0)
VERMELHO = (255,0,0)

# Criar um Relogio
clock = pygame.time.Clock()
velocidade = 15

# Tamanho da Comida
tamanho_bloco = 20

# Fonte
fonte = pygame.font.SysFont(None, 35)

# Função para mostrar a pontuação na tela
def mostrar_pontuacao(pontos):
    valor = fonte.render(f"Pontos: {pontos}", True, PRETO)
    tela.blit(valor, [10,10])

# Função principal do jogo
def jogo():
    # Definir a posição inicial da cobra
    x = largura // 2
    y = altura // 2
    x_mudanca = 0
    y_mudanca = 0

    cobra = []
    comprimento_cobra = 1

    # Posição aleatoria da comida  
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20) * 20
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20) * 20 

    fim_de_jogo = False

    while not fim_de_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0
        #Atualizar a posição da cobra
        x += x_mudanca
        y += y_mudanca

        #Verificando se a Cobra bateu Na Borda
        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_de_jogo = True

        tela.fill(BRANCO)

        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca = []
        cabeca.append(x)
        cabeca.append(y)
        cobra.append(cabeca)

        if len(cobra) > comprimento_cobra:
            del cobra[0]

        # Verificar se a cobra bateu nela mesma
        for bloco in cobra[:-1]:
            if bloco == cabeca:
                fim_de_jogo = True

        # Desenhar todos os blocos da cobra
        for bloco in cobra:
            pygame.draw.rect(tela, VERDE, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

        # Mostrar a pontuação
        mostrar_pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        # Verificar se a cobra comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20) * 20
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20) * 20 
            comprimento_cobra += 1

        clock.tick(velocidade)

    # Quando terminar o jogo
    tela.fill(BRANCO)
    mensagem = fonte.render(f"GAME OVER, PONTUAÇÂO: {comprimento_cobra - 1}", True, VERMELHO)
    tela.blit(mensagem, [largura / 6, altura / 3])
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

jogo() 