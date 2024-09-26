# Importando bibliotecas
import numpy as np
import pygame
import random
import cv2
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Loop principal de seleção de jogo
while True:
    print('-=-' * 20)
    print('ESCOLHA UM JOGO:')
    print('[1] JOGO DA VELHA\n[2] JOGO DA COBRINHA\n[3] VOLUME COM AS MÃOS\n[4] SAIR')
    print('-=-' * 20)

    userselec = int(input('Selecione sua opção: '))

    if userselec == 1:
        # Função para exibir o tabuleiro do jogo da velha
        def exibir_tabuleiro(tabuleiro):
            for linha in tabuleiro:
                print("|".join(str(posicao) for posicao in linha))
                print("-" * 5)

        # Função para verificar vitória no jogo da velha
        def verificar_vitoria(tabuleiro, simbolo):
            for i in range(3):
                if all(tabuleiro[i][j] == simbolo for j in range(3)) or all(tabuleiro[j][i] == simbolo for j in range(3)):
                    return True
            if all(tabuleiro[i][i] == simbolo for i in range(3)) or all(tabuleiro[i][2 - i] == simbolo for i in range(3)):
                return True
            return False

        # Função principal do jogo da velha
        def jogar_jogo_da_velha():
            tabuleiro = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
            jogador = 'X'
            jogo_continua = True

            while jogo_continua:
                exibir_tabuleiro(tabuleiro)
                escolha = input(f"Jogador {jogador}, escolha uma posição (1-9): ")

                if escolha.isdigit() and 1 <= int(escolha) <= 9:
                    escolha = int(escolha)
                    linha = (escolha - 1) // 3
                    coluna = (escolha - 1) % 3

                    if tabuleiro[linha][coluna] == str(escolha):
                        tabuleiro[linha][coluna] = jogador

                        if verificar_vitoria(tabuleiro, jogador):
                            exibir_tabuleiro(tabuleiro)
                            print(f"Parabéns! Jogador {jogador} venceu!")
                            jogo_continua = False
                        elif all(not posicao.isdigit() for linha in tabuleiro for posicao in linha):
                            exibir_tabuleiro(tabuleiro)
                            print("Empate!")
                            jogo_continua = False
                        else:
                            jogador = 'O' if jogador == 'X' else 'X'
                    else:
                        print("Posição ocupada. Escolha outra.")
                else:
                    print("Escolha inválida. Escolha um número de 1 a 9.")

        jogar_jogo_da_velha()

    elif userselec == 2:
        # Jogo da cobrinha
        pygame.init()

        PRETO = (0, 0, 0)
        ROXO = (128, 0, 128)
        VERDE = (0, 255, 0)

        LARGURA, ALTURA = 900, 600
        tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("FAMETRO PROJETO")
        relogio = pygame.time.Clock()

        TAMANHO = 10
        cobra_x, cobra_y = LARGURA // 2, ALTURA // 2
        velocidade_x, velocidade_y = 0, 0
        cobra = []
        comprimento = 1

        comida_x = random.randrange(0, LARGURA - TAMANHO, TAMANHO)
        comida_y = random.randrange(0, ALTURA - TAMANHO, TAMANHO)

        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        velocidade_x, velocidade_y = -TAMANHO, 0
                    if evento.key == pygame.K_RIGHT:
                        velocidade_x, velocidade_y = TAMANHO, 0
                    if evento.key == pygame.K_UP:
                        velocidade_x, velocidade_y = 0, -TAMANHO
                    if evento.key == pygame.K_DOWN:
                        velocidade_x, velocidade_y = 0, TAMANHO

            cobra_x += velocidade_x
            cobra_y += velocidade_y

            if cobra_x < 0 or cobra_x >= LARGURA or cobra_y < 0 or cobra_y >= ALTURA:
                rodando = False

            if cobra_x == comida_x and cobra_y == comida_y:
                comprimento += 1
                comida_x = random.randrange(0, LARGURA - TAMANHO, TAMANHO)
                comida_y = random.randrange(0, ALTURA - TAMANHO, TAMANHO)

            tela.fill(PRETO)
            pygame.draw.rect(tela, VERDE, [comida_x, comida_y, TAMANHO, TAMANHO])

            cabeca = (cobra_x, cobra_y)
            cobra.append(cabeca)
            if len(cobra) > comprimento:
                cobra.pop(0)

            if cabeca in cobra[:-1]:
                rodando = False

            for segmento in cobra:
                pygame.draw.rect(tela, ROXO, [segmento[0], segmento[1], TAMANHO, TAMANHO])

            pygame.display.flip()
            relogio.tick(15)

        pygame.quit()

    elif userselec == 3:
        # Controle de volume com as mãos
        largura_cam, altura_cam = 640, 480
        cap = cv2.VideoCapture(0)
        detector = mp.solutions.hands.Hands()

        min_vol, max_vol = 0, 100
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        while True:
            sucesso, img = cap.read()
            img = cv2.flip(img, 1)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = detector.process(img_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    x1, y1 = int(hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].x * largura_cam), int(hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y * altura_cam)
                    x2, y2 = int(hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].x * largura_cam), int(hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].y * altura_cam)

                    comprimento = math.hypot(x2 - x1, y2 - y1)
                    vol = np.interp(comprimento, [50, 300], [min_vol, max_vol])
                    volume.SetMasterVolumeLevelScalar(vol / 100, None)

                    if comprimento < 50:
                        cv2.circle(img, (x1, y1), 15, (0, 255, 0), cv2.FILLED)

            cv2.imshow("Controle de Volume", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    elif userselec == 4:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Escolha uma opção de 1 a 4.")
