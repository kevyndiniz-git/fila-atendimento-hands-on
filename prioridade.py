import heapq


class FilaPrioridade:
    def __init__(self):
        self.clientes = []
        self.contador = 0
        self.contador_senha = 1

    def enqueue(self, nome, prioridade):
        senha = f"P{self.contador_senha:03d}"
        self.contador_senha += 1

        cliente = {
            "nome": nome,
            "senha": senha,
            "prioridade": prioridade
        }

        heapq.heappush(
            self.clientes,
            (prioridade, self.contador, cliente)
        )

        self.contador += 1

        return cliente

    def dequeue(self):
        if self.empty():
            return None

        _, _, cliente = heapq.heappop(self.clientes)

        return cliente

    def head(self):
        if self.empty():
            return None

        return self.clientes[0][2]

    def size(self):
        return len(self.clientes)

    def empty(self):
        return len(self.clientes) == 0


# Teste da fila de prioridade
if __name__ == "__main__":
    fila = FilaPrioridade()

    print("FILA DE PRIORIDADE:")

    clientes = [
        ("Ana", 3),
        ("Bruno", 2),
        ("Carlos", 1),
        ("Daniela", 3),
        ("Eduardo", 2),
        ("Fernanda", 1),
        ("Gabriel", 3),
        ("Helena", 2),
        ("Igor", 1),
        ("Juliana", 3)
    ]

    print("\nClientes na ordem de chegada:")

    for nome, prioridade in clientes:
        cliente = fila.enqueue(nome, prioridade)

        print(
            f"Nome: {cliente['nome']} | "
            f"Senha: {cliente['senha']} | "
            f"Prioridade: {cliente['prioridade']}"
        )

    print(f"\nTamanho da fila: {fila.size()}")

    proximo = fila.head()

    print(
        f"\nPróximo cliente: {proximo['nome']} "
        f"- Senha {proximo['senha']} "
        f"- Prioridade {proximo['prioridade']}"
    )

    print("\nORDEM DE ATENDIMENTO: ")

    while not fila.empty():
        cliente = fila.dequeue()

        print(
            f"Atendendo: {cliente['nome']} "
            f"- Senha {cliente['senha']} "
            f"- Prioridade {cliente['prioridade']}"
        )

    print(f"\nFila vazia? {fila.empty()}")