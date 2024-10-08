import pygame
import numpy as np
from math import *

WINDOW_SIZE =  800
window = pygame.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
clock = pygame.time.Clock()

pontosCubo = [n for n in range(8)]
pontosCubo[0] = [[-1],[-1],[1],[1]]
pontosCubo[1] = [[1],[-1],[1],[1]]
pontosCubo[2] = [[1],[1],[1],[1]]
pontosCubo[3] = [[-1],[1],[1],[1]]
pontosCubo[4] = [[-1],[-1],[-1],[1]]
pontosCubo[5] = [[1],[-1],[-1],[1]]
pontosCubo[6] = [[1],[1],[-1],[1]]
pontosCubo[7] = [[-1],[1],[-1],[1]] 

# Conecta os vertices do cubo
def conectaPontos(i, j, pontos):
    pygame.draw.line(window, (255, 255, 255), (pontos[i][0], pontos[i][1]) , (pontos[j][0], pontos[j][1]))

# Loop
velocideRotacao = 0.01
d = 50
moverX = moverY = 0
angulo_x = angulo_y = angulo_z = 0
z_translation = 2  # Initial z-translation value
while True:
    clock.tick(60)
    window.fill((0,0,0))
    if d < 1:
        d = 1
    # Matriz de projeção
    matrizProjecao = [[0, 0,   0, -d],
                    [1, 0,   0,  0],
                    [0, 1,   0,  0],
                    [0, 0, -1/d, 0]]
    # Matrizes de rotação
    # Rotação em torno do eixo X
    rotacao_x = [[1, 0, 0, 0],
                    [0, cos(angulo_x), -sin(angulo_x), 0],
                    [0, sin(angulo_x), cos(angulo_x), 0],
                    [0,0,0,1]]
    
    # Rotação em torno do eixo Y
    rotacao_y = [[cos(angulo_y), 0, sin(angulo_y), 0],
                    [0, 1, 0, 0],
                    [-sin(angulo_y), 0, cos(angulo_y), 1],
                    [0,0,0,1]]
    
    # Rotação em torno do eixo Z
    rotacao_z = [[cos(angulo_z), -sin(angulo_z), 0, 0],
                    [sin(angulo_z), cos(angulo_z), 0, 0],
                    [0, 0, 1, 0],
                    [0,0,0,1]]
    
    # Matriz de translação
    translacao = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, z_translation],
                  [0, 0, 0, 1]]

    angulo_x += velocideRotacao; angulo_y += velocideRotacao; angulo_z += velocideRotacao
    pontos = [0 for _ in range(len(pontosCubo))]
    i = 0
    for ponto in pontosCubo:
        matrizRotacionadaX = rotacao_x @ np.array(ponto)
        matrizRotacionadaY = rotacao_y @ matrizRotacionadaX
        matrizRotacionadaZ = rotacao_z @ matrizRotacionadaY
        matrizTransladada = translacao @ matrizRotacionadaZ
        ponto_2d = matrizProjecao @ matrizTransladada
        x = ((ponto_2d[1] / ponto_2d[3]) + WINDOW_SIZE/2) + moverX
        y = ((ponto_2d[2] / ponto_2d[3]) + WINDOW_SIZE/2) + moverY
        pontos[i] = (x[0],y[0])
        i += 1
        pygame.draw.circle(window, (255, 255, 255), (x[0], y[0]), 4)

    conectaPontos(0, 1, pontos)
    conectaPontos(0, 3, pontos)
    conectaPontos(0, 4, pontos)
    conectaPontos(1, 2, pontos)
    conectaPontos(1, 5, pontos)
    conectaPontos(2, 6, pontos)
    conectaPontos(2, 3, pontos)
    conectaPontos(3, 7, pontos)
    conectaPontos(4, 5, pontos)
    conectaPontos(4, 7, pontos)
    conectaPontos(6, 5, pontos)
    conectaPontos(6, 7, pontos)

    # Captura de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # Zoom apartir do scroll do mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        d += 25
                    elif event.button == 5:
                        d -= 25
    # Movimentação do cubo usando W, A, S, D
    # Controle de rotação usando Q e E
    # Controle de proximidade usando R e F
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        moverY -= 10
    if keys[pygame.K_s]:
        moverY += 10
    if keys[pygame.K_a]:
        moverX -= 10
    if keys[pygame.K_d]:
        moverX += 10
    if keys[pygame.K_e]:
        velocideRotacao -= 0.01
    if keys[pygame.K_q]:
        velocideRotacao += 0.01
    if keys[pygame.K_r]:
        z_translation += 0.1  # Move para longe
    if keys[pygame.K_f]:
        if z_translation >= 0.9:
            z_translation -= 0.1  # Mover para perto
        
          


    print(z_translation)
    pygame.display.update()
