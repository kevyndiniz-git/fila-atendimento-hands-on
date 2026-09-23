class FilaCircular:
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self.clientes = [None] * capacidade
        self.front = 0
        self.rear = 0
        self.quantidade = 0
        self.contador_senha = 1

    def enqueue(self, nome, prioridade):
        if self.quantidade == self.capacidade:
            print("Fila circular cheia!")
            return None

        senha = f"C{self.contador_senha:03d}"
        self.contador_senha += 1

        cliente = {
            "nome": nome,
            "senha": senha,
            "prioridade": prioridade
        }

        self.clientes[self.rear] = cliente
        self.rear = (self.rear + 1) % self.capacidade
        self.quantidade += 1

        return cliente

    def dequeue(self):
        if self.empty():
            print("Fila circular vazia!")
            return None

        cliente = self.clientes[self.front]
        self.clientes[self.front] = None
        self.front = (self.front + 1) % self.capacidade
        self.quantidade -= 1

        return cliente

    def head(self):
        if self.empty():
            return None

        return self.clientes[self.front]

    def size(self):
        return self.quantidade

    def empty(self):
        return self.quantidade == 0

    def mostrar_estado(self):
        print(f"Front: {self.front} | Rear: {self.rear}")
        print(f"Quantidade: {self.quantidade}")
        print("Fila:", self.clientes)


# Teste da fila circular
if __name__ == "__main__":
    fila = FilaCircular(5)

    print("---FILA CIRCULAR---")

    print("\nInserindo 5 clientes:")

    for nome, prioridade in [
        ("Ana", 3),
        ("Bruno", 2),
        ("Carlos", 1),
        ("Daniela", 3),
        ("Eduardo", 2)
    ]:
        cliente = fila.enqueue(nome, prioridade)

        print(
            f"Inserido: {cliente['nome']} - "
            f"Senha {cliente['senha']}"
        )

    print("\nEstado da fila:")
    fila.mostrar_estado()

    print("\nTentando inserir um sexto cliente:")
    fila.enqueue("Fernanda", 1)

    print("\nRemovendo dois clientes:")

    for _ in range(2):
        cliente = fila.dequeue()

        print(
            f"Atendido: {cliente['nome']} - "
            f"Senha {cliente['senha']}"
        )

    print("\nEstado após as remoções:")
    fila.mostrar_estado()

    print("\nInserindo novos clientes nas posições liberadas:")

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