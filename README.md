# Como Executar
## Para executar o programa, siga os passos abaixo:

- Certifique-se de ter o Python instalado no seu sistema.
- Instale as bibliotecas necessárias executando os comandos:
```python
  pip install pygame
  pip install numpy
```
- Baixe o código-fonte deste projeto.
- Execute o arquivo Python main.py.
- Pressione as teclas A e D para controlar a velocidade de rotação.
- Pressione as teclas W e S para controlar o zoom.
- Pressione a tecla Q para sair do programa.

## Utilização
- Movimentação: Use as teclas W, A, S, D para mover o cubo na tela.
- Rotação: Use as teclas Q e E para controlar a velocidade de rotação do cubo.
- Zoom: Use a roda do mouse para aumentar ou diminuir o zoom do cubo.
  
# Descrição Matemática
### O cubo é renderizado usando uma técnica de projeção perspectiva, onde cada ponto tridimensional é transformado em um ponto bidimensional na tela.

As transformações aplicadas são as seguintes:

- **Matriz de Projeção**: Uma matriz de projeção é aplicada para transformar os pontos tridimensionais em coordenadas 2D na tela, simulando a perspectiva. Esta matriz é ajustada para controlar o fator de zoom.
- **Matrizes de Rotação**: São aplicadas três matrizes de rotação para permitir a rotação do cubo em torno dos eixos X, Y e Z. Cada matriz de rotação é uma transformação linear que altera a orientação dos pontos em relação ao eixo de rotação.
- **Matriz de Translação**: Uma matriz de translação é aplicada para mover o cubo na tela, permitindo que ele seja movido horizontalmente e verticalmente.
As teclas do teclado e a roda do mouse são usadas para interagir com o cubo, alterando as variáveis que controlam as transformações e a posição do cubo na tela.
