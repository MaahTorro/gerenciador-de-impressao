import time
from collections import deque

# Códigos ANSI para cores
RED = "\033[91m"      # Vermelho
GREEN = "\033[92m"    # Verde 
YELLOW = "\033[93m"   # Amarelo
CYAN = "\033[96m"     # Ciano 
BLUE = "\033[94m"     # Azul 
RESET = "\033[0m"     


class GerenciadorImpressao:
    def __init__(self):
        self.fila_alta = deque()
        self.fila_media = deque()
        self.fila_baixa = deque()
        self.documentos = set()

    def adicionar_documento(self, nome, prioridade):
        if nome in self.documentos:
            print(RED + f"❌ Erro: O documento '{nome}' já existe." + RESET)
            return False

        if prioridade == "alta":
            self.fila_alta.append(nome)
        elif prioridade == "media":
            self.fila_media.append(nome)
        elif prioridade == "baixa":
            self.fila_baixa.append(nome)
        else:
            print(RED + f"⚠️ Erro: Prioridade '{prioridade}' inválida." + RESET)
            return False

        self.documentos.add(nome)
        print(GREEN + f"✅ Documento '{nome}' adicionado com sucesso!" + RESET)
        return True

    def processar_proximo(self):
        if self.fila_alta:
            doc = self.fila_alta.popleft()
        elif self.fila_media:
            doc = self.fila_media.popleft()
        elif self.fila_baixa:
            doc = self.fila_baixa.popleft()
        else:
            print(RED + "🚫 Não há documentos para processar." + RESET)
            return None

        self.documentos.remove(doc)
        print(YELLOW + f"🖨️ Processando (imprimindo) o documento: {doc}" + RESET)
        time.sleep(1.5)  
        print(GREEN + f"✅ Documento '{doc}' impresso com sucesso!" + RESET)
        return doc

    def relatorio(self):
        print(CYAN + "\n📊 --- RELATÓRIO DE FILA --- 📊" + RESET)
        print(f"🔴 Prioridade Alta: {list(self.fila_alta)}")
        print(f"🟡 Prioridade Média: {list(self.fila_media)}")
        print(f"🔵 Prioridade Baixa: {list(self.fila_baixa)}")
        print(CYAN + "-----------------------------------\n" + RESET)

def menu():
    print("\n" + CYAN + "═" * 45 + RESET)
    print(GREEN + "📄 GERENCIADOR DE IMPRESSÃO 📄".center(45) + RESET)
    print(CYAN + "═" * 45 + RESET)
    print("\nO que deseja fazer?")
    print(BLUE + "1️⃣  - Adicionar uma impressão" + RESET)
    print(BLUE + "2️⃣  - Processar próxima impressão" + RESET)
    print(BLUE + "3️⃣  - Ver o Relatório" + RESET)
    print(RED + "4️⃣  - Sair" + RESET)
    print(CYAN + "═" * 45 + RESET)

    return input("➤ Escolha uma opção: ")


def adicionar_mais():
    while True:
        escolha = input(YELLOW + "\n➕ Deseja adicionar mais uma impressão? (S/N): " + RESET).lower()
        if escolha in ['s', 'n']:
            return escolha == 's'
        print(RED + "⚠️ Por favor, responda com 'S' para Sim ou 'N' para Não." + RESET)


def main():
    gerenciador = GerenciadorImpressao()

    while True:
        escolha = menu()

        if escolha == '1':
            while True:
                nome = input(YELLOW + "📝 Nome do documento: " + RESET)
                prioridade = input(YELLOW + "⚡ Prioridade (alta/media/baixa): " + RESET).lower()
                if gerenciador.adicionar_documento(nome, prioridade):
                    if not adicionar_mais():
                        print("\n🔙 Voltando ao menu principal.")
                        break
        elif escolha == '2':
            gerenciador.processar_proximo()
        elif escolha == '3':
            gerenciador.relatorio()
        elif escolha == '4':
            print(RED + "\n🚪 Programa encerrado. Até logo!" + RESET)
            break
        else:
            print(RED + "❌ Opção inválida. Por favor, escolha 1, 2, 3 ou 4." + RESET)


if __name__ == "__main__":
    main()
