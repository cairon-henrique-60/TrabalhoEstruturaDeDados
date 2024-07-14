from tableHash import tableHash
from linkedList import linkedList


def main():
    tabela_hash = tableHash.TabelaHash()

    print("Tabela Hash:")
    tabela_hash.imprimir_tabela()

    tabela_hash.inserir_estados()

    print("Tabela Hash:")
    tabela_hash.imprimir_tabela()

    tabela_hash.inserir_estado_ficticio('UZ', 'Urzikistão')

    print("Tabela Hash:")
    tabela_hash.imprimir_tabela()

    sistema = linkedList.SistemaTriagem()
    sistema.exibir_menu()


if __name__ == "__main__":
    main()
