# Gerenciador de Impressão 📄🖨️

## 🖨 Sobre o Projeto

**Gerenciador de Impressão** é uma aplicação de linha de comando em Python que simula um sistema de gerenciamento de fila de impressão. Este projeto foi desenvolvido para demonstrar conceitos de estruturas de dados (filas) e programação orientada a objetos em Python.

---

## 🚀 Funcionalidades

- **Adicionar Documentos**: Permite adicionar documentos à fila de impressão com diferentes prioridades (alta, média, baixa).
- **Processar Impressões**: Processa o próximo documento na fila, respeitando a ordem de prioridade.
- **Visualizar Relatório**: Exibe um relatório detalhado das filas de impressão atuais.
- **Interface Interativa**: Menu de fácil utilização para navegar entre as diferentes funcionalidades.

---

## 💡 Tecnologias Utilizadas

- **Python 3** - Linguagem de programação.
- **Deque** - Estrutura de dados de fila, utilizada para organizar os documentos nas diferentes prioridades.
- **Cores ANSI** - Para colorir e tornar a interface no terminal mais bonita e intuitiva.

---

## 💻 Como Usar

1. Certifique-se de ter Python 3.x instalado em seu sistema.
2. Clone este repositório ou baixe o arquivo `gerenciador_impressao.py`.
3. Abra um terminal e navegue até o diretório onde o arquivo está localizado. 
5. Siga as instruções na tela para interagir com o programa.

## 🔍 Estrutura do Código

O projeto consiste em uma única classe principal `GerenciadorImpressao` com os seguintes métodos:

- `adicionar_documento(nome, prioridade)`: Adiciona um novo documento à fila apropriada.
- `processar_proximo()`: Remove e "imprime" o próximo documento na fila de maior prioridade.
- `relatorio()`: Exibe o estado atual das filas de impressão.

Funções auxiliares incluem:
- `menu()`: Exibe o menu principal e captura a escolha do usuário.
- `adicionar_mais()`: Pergunta ao usuário se deseja adicionar mais documentos.


---

## 👥 Desenvolvedores

Este projeto foi desenvolvido por:

- [MaahTorro](https://github.com/MaahTorro)
- [Matheus A.]()
- [Matheus Q.]()
- [Gustavo]()
- [Rodrigo]()
