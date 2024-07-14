class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def inserir_estados(tabela_hash):
        estados = [
            ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
            ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
            ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
            ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
            ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
            ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
            ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
        ]

        for sigla, nome_estado in estados:
            posicao = funcao_hash(sigla)
            tabela_hash.inserir_no_inicio(posicao, sigla, nome_estado)

    def inserir_estado_ficticio(tabela_hash, sigla, nome_estado):
        posicao = funcao_hash(sigla)
        tabela_hash.inserir_no_inicio(posicao, sigla, nome_estado)

    def inserir_no_inicio(self, posicao, sigla, nomeEstado):
        novo_nodo = Nodo(sigla, nomeEstado)
        if self.tabela[posicao] is None:
            self.tabela[posicao] = novo_nodo
        else:
            novo_nodo.proximo = self.tabela[posicao]
            self.tabela[posicao] = novo_nodo

    def imprimir_tabela(self):
        for i, lista in enumerate(self.tabela):
            if lista is None:
                print(f'{i}: None')
            else:
                print(f'{i}:', end=' ')

                atual = lista
                siglas = []

                while atual is not None:
                    siglas.append(atual.sigla)
                    atual = atual.proximo

                print('->'.join(siglas) + '->None')

def funcao_hash(sigla):
    if sigla == "DF":
        return 7
    char1, char2 = sigla[0], sigla[1]
    posicao = (ord(char1) + ord(char2)) % 10
    return posicao

