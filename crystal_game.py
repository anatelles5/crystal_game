import pygame 
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Jogo 2D - Menu")

# Fonte
fonte = pygame.font.SysFont("arial", 40, bold=True)

# Carrega imagens
background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background, (LARGURA, ALTURA))  # ajusta ao tamanho da tela

imagem_botao = pygame.image.load("botao.png").convert_alpha()
botao_largura, botao_altura = imagem_botao.get_size()

# Função para desenhar botão com texto
def desenhar_botao(texto, x, y):
    tela.blit(imagem_botao, (x, y))
    texto_render = fonte.render(texto, True, (0, 0, 0))
    texto_rect = texto_render.get_rect(center=(x + botao_largura // 2, y + botao_altura // 2))
    tela.blit(texto_render, texto_rect)
    return pygame.Rect(x, y, botao_largura, botao_altura)

# Loop principal do menu
def menu():
    rodando = True
    while rodando:
        # Desenha o fundo
        tela.blit(background, (0, 0))

        # Posição dos botões
        botao1 = desenhar_botao("1 Player", LARGURA//2 - botao_largura//2, ALTURA//2 - 100)
        botao2 = desenhar_botao("2 Players - Coop", LARGURA//2 - botao_largura//2, ALTURA//2 + 20)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if botao1.collidepoint(event.pos):
                    print("Iniciando jogo singleplayer...")
                    rodando = False
                if botao2.collidepoint(event.pos):
                    print("Iniciando jogo cooperativo...")
                    rodando = False

        pygame.display.flip()

# Executa o menu
menu()
