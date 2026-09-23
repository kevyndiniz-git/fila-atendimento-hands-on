from classica import Fila
from circular import FilaCircular
from prioridade import FilaPrioridade
from desafio import executar_desafio


def fila_classica():
    fila = Fila()

    clientes = [
        ("Ana", 3),
        ("Bruno", 2),
        ("Carlos", 1),
        ("Daniela", 3),
        ("Eduardo", 2),
        ("Fernanda", 3),
        ("Gabriel", 1),
        ("Helena", 2),
        ("Igor", 3),
        ("Juliana", 1)
    ]

    print("\n    FILA CLÁSSICA    ")
    print("Ordem de atendimento:")

    for nome, prioridade in clientes:
        fila.enqueue(nome, prioridade)

    while not fila.empty():
        cliente = fila.dequeue()

        print(
            f"{cliente['nome']} - "
            f"Senha {cliente['senha']} - "
            f"Prioridade {cliente['prioridade']}"
        )


def fila_circular():
    fila = FilaCircular(5)

    clientes = [
        ("Ana", 3),
        ("Bruno", 2),
        ("Carlos", 1),
        ("Daniela", 3),
        ("Eduardo", 2)
    ]

    print("\n    FILA CIRCULAR    ")

    print("\nInserindo 5 clientes:")

    for nome, prioridade in clientes:
        cliente = fila.enqueue(nome, prioridade)

        print(
            f"{cliente['nome']} - "
            f"Senha {cliente['senha']}"
        )

    print("\nEstado da fila:")
    fila.mostrar_estado()

    print("\nRemovendo dois clientes:")

    for _ in range(2):
        cliente = fila.dequeue()

        print(
            f"Atendido: {cliente['nome']} - "
            f"Senha {cliente['senha']}"
        )

    print("\nInserindo novos clientes:")

    for nome, prioridade in [
        ("Fernanda", 1),
        ("Gabriel", 3)
    ]:
        cliente = fila.enqueue(nome, prioridade)

        print(
            f"Inserido: {cliente['nome']} - "
            f"Senha {cliente['senha']}"
        )

    print("\nEstado final:")
    fila.mostrar_estado()


def fila_prioridade():
    fila = FilaPrioridade()

    clientes = [
        ("Ana", 3),
        ("Bruno", 2),
        ("Carlos", 1),
        ("Daniela", 3),
        ("Eduardo", 2),
        ("Fernanda", 1)
    ]

    print("\n    FILA DE PRIORIDADE    ")
    print("Ordem de atendimento:")

    for nome, prioridade in clientes:
        fila.enqueue(nome, prioridade)

    while not fila.empty():
        cliente = fila.dequeue()

        print(
            f"{cliente['nome']} - "
            f"Senha {cliente['senha']} - "
            f"Prioridade {cliente['prioridade']}"
        )


def menu():
    while True:
        print("\n                                       ")
        print("   SISTEMA INTELIGENTE DE ATENDIMENTO")
        print("                                       ")
        print("1 - Fila Clássica")
        print("2 - Fila Circular")
        print("3 - Fila de Prioridade")
        print("4 - Desafio Final")
        print("0 - SAIR")
        print("                                        ")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            fila_classica()

        elif opcao == "2":
            fila_circular()

        elif opcao == "3":
            fila_prioridade()

        elif opcao == "4":
            executar_desafio()

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    menu()
