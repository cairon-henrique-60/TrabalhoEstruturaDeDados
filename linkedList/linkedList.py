class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserirSemPrioridade(self, nodo):
        if self.cabeca is None:
            self.cabeca = nodo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.cabeca is None:
            self.cabeca = nodo
        else:
            atual = self.cabeca
            anterior = None
            while atual and atual.cor == 'A':
                anterior = atual
                atual = atual.proximo
            if anterior is None:
                nodo.proximo = self.cabeca
                self.cabeca = nodo
            else:
                nodo.proximo = atual
                anterior.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A/V): ").strip().upper()
        numero = int(input("Informe o número do cartão: ").strip())
        nodo = Nodo(numero, cor)

        if self.cabeca is None:
            self.cabeca = nodo
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)
        elif cor == 'A':
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        if self.cabeca is None:
            print("A lista de espera está vazia.")
        else:
            atual = self.cabeca
            while atual:
                print(f"Cartão {atual.cor} - Número {atual.numero}")
                atual = atual.proximo

    def atenderPaciente(self):
        if self.cabeca is None:
            print("Não há pacientes na lista de espera.")
        else:
            paciente_atendido = self.cabeca
            self.cabeca = self.cabeca.proximo
            print(f"Paciente com cartão {paciente_atendido.cor} - Número {paciente_atendido.numero} chamado para atendimento.")
            del paciente_atendido


class SistemaTriagem:
    def __init__(self):
        self.lista = ListaEncadeada()

    def exibir_menu(self):
        while True:
            print("\nMenu:")
            print("1 - Adicionar paciente à fila")
            print("2 - Mostrar pacientes na fila")
            print("3 - Chamar paciente")
            print("4 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                self.lista.inserir()
            elif opcao == '2':
                self.lista.imprimirListaEspera()
            elif opcao == '3':
                self.lista.atenderPaciente()
            elif opcao == '4':
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")
