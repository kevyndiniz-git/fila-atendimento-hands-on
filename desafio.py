import random

from classica import Fila
from circular import FilaCircular
from prioridade import FilaPrioridade


def gerar_clientes():
    nomes = [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
        "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
        "Lucas", "Mariana", "Nicolas", "Olivia", "Paulo",
        "Rafaela", "Samuel", "Tatiana", "Vinicius", "Yasmin"
    ]

    clientes = []

    for nome in nomes:
        prioridade = random.randint(1, 3)

        clientes.append({
            "nome": nome,
            "prioridade": prioridade
        })

    return clientes


def testar_fila_classica(clientes):
    print("\nATENDIMENTO - FILA CLÁSSICA")

    fila = Fila()

    for cliente in clientes:
        fila.enqueue(cliente["nome"], cliente["prioridade"])

    while not fila.empty():
        atendido = fila.dequeue()

        print(
            f"{atendido['nome']} - "
            f"Senha {atendido['senha']} - "
            f"Prioridade {atendido['prioridade']}"
        )


def testar_fila_circular(clientes):
    print("\nCOMPORTAMENTO - FILA CIRCULAR")

    fila = FilaCircular(5)

    print(f"Front inicial: {fila.front}")
    print(f"Rear inicial: {fila.rear}")

    indice = 0

    while indice < len(clientes):

        while indice < len(clientes) and fila.size() < fila.capacidade:
            cliente = clientes[indice]

            inserido = fila.enqueue(
                cliente["nome"],
                cliente["prioridade"]
            )

            if inserido:
                print(
                    f"Inserido: {inserido['nome']} - "
                    f"Senha {inserido['senha']} - "
                    f"Prioridade {inserido['prioridade']}"
                )

                indice += 1

        if fila.size() == fila.capacidade:

            print("\nFila atingiu a capacidade máxima.")
            print(f"Front: {fila.front}")
            print(f"Rear: {fila.rear}")
            print(f"Quantidade: {fila.size()}")

            print("\nRemovendo 2 clientes para liberar posições:")

            for _ in range(2):
                atendido = fila.dequeue()

                if atendido:
                    print(
                        f"Atendido: {atendido['nome']} - "
                        f"Senha {atendido['senha']}"
                    )

            print(f"\nFront: {fila.front}")
            print(f"Rear: {fila.rear}")
            print(f"Quantidade: {fila.size()}")

    print("\nAtendendo os clientes restantes:")

    while not fila.empty():
        atendido = fila.dequeue()

        print(
            f"Atendido: {atendido['nome']} - "
            f"Senha {atendido['senha']} - "
            f"Prioridade {atendido['prioridade']}"
        )

    print("\nEstado final:")
    print(f"Front: {fila.front}")
    print(f"Rear: {fila.rear}")
    print(f"Quantidade: {fila.size()}")

def testar_fila_prioridade(clientes):
    print("\nATENDIMENTO - FILA DE PRIORIDADE")

    fila = FilaPrioridade()

    for cliente in clientes:
        fila.enqueue(cliente["nome"], cliente["prioridade"])

    while not fila.empty():
        atendido = fila.dequeue()

        print(
            f"{atendido['nome']} - "
            f"Senha {atendido['senha']} - "
            f"Prioridade {atendido['prioridade']}"
        )


def executar_desafio():
    print("\nDESAFIO FINAL")

    clientes = gerar_clientes()

    print("\nCLIENTES NA ORDEM DE CHEGADA:")

    for i, cliente in enumerate(clientes, start=1):
        print(
            f"{i:02d}. {cliente['nome']} - "
            f"Prioridade {cliente['prioridade']}"
        )

    testar_fila_classica(clientes)
    testar_fila_circular(clientes)
    testar_fila_prioridade(clientes)

    print("\nFIM DA SIMULAÇÃO")


if __name__ == "__main__":
    executar_desafio()