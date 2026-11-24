
# 📘 Assignment: Hangman Game

## 🎯 Objetivo

Construa o clássico jogo da Forca em Python usando manipulação de strings, loops, condicionais e entrada de dados do usuário.

## 📝 Tarefas encontrada

### 🛠️ Implement the Game Setup

#### Descrição

Prepare o estado inicial do jogo usando a lista de palavras fornecida no código inicial.

#### Requisitos

O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista `words`.
- Inicializar uma coleção para registrar as letras já adivinhadas.
- Inicializar o número de palpites incorretos como zero.
- Definir uma quantidade máxima de palpites incorretos.

### 🛠️ Run the Guessing Loop

#### Descrição

Crie o ciclo principal do jogo. O jogador deve informar uma letra por vez até revelar a palavra ou esgotar suas tentativas.

#### Requisitos

O programa concluído deve:

- Mostrar o progresso da palavra no formato `_ _ _`.
- Solicitar ao usuário uma letra a cada rodada.
- Registrar letras corretas e incorretas sem contar repetidamente um mesmo palpite incorreto.
- Informar quantas tentativas incorretas ainda restam.
- Encerrar quando todas as letras forem adivinhadas ou o limite de erros for atingido.
- Exibir uma mensagem clara de vitória ou derrota ao final do jogo.