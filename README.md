FamTech - MultiGame Project
História do Projeto:
FamTech foi desenvolvido em novembro de 2023 como parte de um projeto de tecnologia para demonstrar as diversas possibilidades que a programação oferece. O objetivo era criar uma plataforma interativa que combinasse jogos e funcionalidades práticas, como o controle de volume, utilizando visão computacional. O projeto foi concebido para mostrar como diferentes bibliotecas e ferramentas podem ser integradas para resolver problemas cotidianos e proporcionar entretenimento.

Descrição:
FamTech é um projeto interativo que combina três jogos e uma funcionalidade inovadora de controle de volume utilizando as mãos, através de tecnologias de visão computacional. O projeto inclui:

Jogo da Velha: Um clássico jogo de tabuleiro para dois jogadores.
Jogo da Cobrinha: Controle a cobra e coma frutas para crescer, evitando colisões.
Controle de Volume com as Mãos: Use gestos da mão capturados pela webcam para ajustar o volume do sistema.
Este projeto serve como uma demonstração das incríveis possibilidades que a programação pode proporcionar, tanto em termos de interatividade quanto de funcionalidades práticas.

Tecnologias Utilizadas:
O projeto FamTech utiliza diversas bibliotecas e frameworks para criar uma experiência completa e interativa:

NumPy: Manipulação de arrays e operações matemáticas.
Pygame: Desenvolvimento dos jogos, como a Cobrinha e a interface do projeto.
OpenCV: Captura e processamento de imagens da webcam para controle de volume.
MediaPipe: Detecção de mãos em tempo real.
PyCaw: Controle do volume do sistema no Windows.
ctypes e comtypes: Manipulação de interfaces de áudio no Windows.

Instalação:
Pré-requisitos
Python 3.10 ou superior
Biblioteca de gerenciamento de ambientes virtuais (venv ou virtualenv)

Passos de Instalação:

Clone este repositório:
git clone https://github.com/seu-usuario/famtech.git
cd famtech

Crie um ambiente virtual e ative-o:
python -m venv .venv
source .venv/Scripts/activate  # No Windows

Instale as dependências necessárias:
pip install -r requirements.txt

Execute o projeto:
python app.py

Como Usar
Ao iniciar o programa, você será apresentado a um menu com três opções de jogos e uma funcionalidade adicional de controle de volume com as mãos:

ESCOLHA UM JOGO:
[1] JOGO DA VELHA
[2] JOGO DA COBRINHA
[3] VOLUME COM AS MÃOS
[4] SAIR

Jogo da Velha: Cada jogador escolhe uma posição de 1 a 9 no tabuleiro para colocar seu símbolo. O primeiro a completar uma linha, coluna ou diagonal vence.
Jogo da Cobrinha: Use as setas do teclado para controlar a cobra. Coma frutas para crescer, mas evite colidir com as paredes ou consigo mesma.
Controle de Volume com as Mãos: Aproxime o polegar e o indicador para diminuir o volume e afaste-os para aumentar.
Sair: Encerre o programa.

Requisitos de Sistema
Sistema Operacional: Windows (necessário para o controle de volume via PyCaw)
Webcam (para a funcionalidade de controle de volume com as mãos)

Dependências
As principais bibliotecas e dependências do projeto são:

numpy
pygame
opencv-python
mediapipe
pycaw
ctypes, comtypes

Contribuições
Contribuições são bem-vindas! Se você deseja colaborar, sinta-se à vontade para enviar um pull request com suas melhorias ou sugestões.
