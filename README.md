# Siga Bem Caminhoneiro

**Número da Lista**: 25<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0101617  |  Guilherme de Morais Richter |
| 18/0102613  |  Ítalo Fernandes Sales de Serra |

## Apresentação

<i>Ainda não disponível.</i>

## Sobre 
A ideia por trás deste projeto é aprimorar o projeto Siga Bem Caminhoneiro 1.0, criando novas funções de gerenciamento de estradas e geração de caminhos utilizando os conhecimentos adquiridos no módulo 2 de Grafos, principalmente, a utilização de pesos nas arestas.

## Screenshots

<i>Ainda não disponível.</i>

## Instalação 
**Linguagem**: Python<br>
**Framework**: Tkinter (biblioteca), NetworkX (biblioteca)<br>



Para criar um ambiente em que seja possível rodar o programa, é necessário:

- Instalar a versão <b>3.9.5</b> do Python.

- Instalar via terminal as seguintes bibliotecas

```python
pip install tk
```
```python
pip install networkx
```
```python
pip install matplotlib
```

- Clonar o nosso repositório do GitHub para a sua máquina, digitando no terminal (necessário ter o Git instalado):

```python
git clone https://github.com/projeto-de-algoritmos/Grafos1_SigaBemCaminhoneiro.git
```

## Uso 

Para utilizar o nosso programa, é necessário que navegue no terminal até o diretório em que está clonado o nosso repositório, no caso, <b>Grafos2_SigaBemCaminhoneiro</b>.

Com o repositório aberto, rodar o seguinte comando:

```python
python interface.py
```

## Outros 

Uma observação é quanto ao mapa gerado. Por estarmos utilizando a função de plotagem do matplotlib, e de desenho de grafo do NetworkX, é uma impossibilidade dessa tecnologia manter 100% das vezes o grafo visualmente organizado. Então, se ao clicar no botão <b>Ver um mapa com estradas atuais</b> for gerado um grafo um pouco confuso, basta fechá-lo e gerar um novo mapa novamente, que o mesmo estará visualmente organizado de outra forma - mas sem perder suas propriedades físicas fundamentais, como os nós e suas arestas.
