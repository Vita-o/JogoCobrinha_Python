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
def mostrar_pontuacao(pontos)
    valor = fonte.render("Pontos:", str(pontos), True, PRETO)
    tela.blit(valor, [10,10])

# Função principal do jogo
def jogo():
    # Definir a posição inicial da cobra
    x = largura // 2
    y = altura // 2
    x_mudanca = 0
    y_mudanca = 0 
