class Fila:
    def __init__(self):
        self.clientes = []
        self.contador_senha = 1

    def enqueue(self, nome, prioridade):
        senha = f"A{self.contador_senha:03d}"
        self.contador_senha += 1

        cliente = {
            "nome": nome,
            "senha": senha,
            "prioridade": prioridade
        }

        self.clientes.append(cliente)

        return cliente

    def dequeue(self):
        if self.empty():
            return None

        return self.clientes.pop(0)

    def head(self):
        if self.empty():
            return None

        return self.clientes[0]

    def size(self):
        return len(self.clientes)

    def empty(self):
        return len(self.clientes) == 0


# Teste da fila clássica
if __name__ == "__main__":
    fila = Fila()

    nomes = [
        "Ana",
        "Bruno",
        "Carlos",
        "Daniela",
        "Eduardo",
        "Fernanda",
        "Gabriel",
        "Helena",
        "Igor",
        "Juliana"
    ]

    prioridades = [3, 2, 1, 3, 2, 3, 1, 2, 3, 1]

    print("FILA CLÁSSICA (FIFO):")
    print("\nClientes na ordem de chegada:")

    for nome, prioridade in zip(nomes, prioridades):
        cliente = fila.enqueue(nome, prioridade)

        print(
            f"Nome: {cliente['nome']} | "
            f"Senha: {cliente['senha']} | "
            f"Prioridade: {cliente['prioridade']}"
        )

    print(f"\nTamanho da fila: {fila.size()}")

    proximo = fila.head()

    print(
        f"Próximo cliente: {proximo['nome']} "
        f"- Senha {proximo['senha']}"
    )

    print("\nORDEM DE ATENDIMENTO:")

    while not fila.empty():
        cliente = fila.dequeue()

        print(
            f"Atendendo: {cliente['nome']} "
            f"- Senha {cliente['senha']}"
        )

    print(f"\nFila vazia? {fila.empty()}")