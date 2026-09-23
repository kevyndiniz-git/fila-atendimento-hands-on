# Sistema Inteligente de Atendimento

Projeto desenvolvido em Python para a disciplina de **Estrutura de Dados II**, com o objetivo de aplicar e comparar diferentes estruturas de filas em um sistema de atendimento.

## Criador

**Kevyn Cardoso**

## Descrição do projeto

O sistema simula o atendimento de clientes utilizando três diferentes estruturas de dados:

- Fila clássica (FIFO);
- Fila circular;
- Fila de prioridade.

Também foi desenvolvido um desafio final com **20 clientes gerados automaticamente**, permitindo comparar o comportamento das três estruturas.

Cada cliente possui:

- **Nome**
- **Senha**
- **Prioridade**

As prioridades utilizadas são:

- **1 — Emergência**
- **2 — Prioritário**
- **3 — Normal**

---

## Estrutura do projeto

```text
fila-atendimento-hands-on/
├── classica.py
├── circular.py
├── prioridade.py
├── desafio.py
├── main.py
└── README.md
```

### Arquivos

**`classica.py`**  
Implementa a fila clássica utilizando o princípio **FIFO (First In, First Out)**, no qual o primeiro cliente que entra é o primeiro a ser atendido.

**`circular.py`**  
Implementa uma fila circular com capacidade de **5 clientes**. Quando posições são liberadas, elas podem ser reutilizadas por novos clientes.

**`prioridade.py`**  
Implementa uma fila de prioridade utilizando a biblioteca `heapq`. Clientes com prioridade menor são atendidos primeiro. Em caso de mesma prioridade, a ordem de chegada é preservada.

**`desafio.py`**  
Executa a simulação final com **20 clientes gerados automaticamente**, comparando o comportamento das três estruturas.

**`main.py`**  
Apresenta o menu principal do sistema e permite executar cada uma das estruturas individualmente ou o desafio final.

---

# Funcionamento das estruturas

## 1. Fila Clássica — FIFO

A fila clássica segue o princípio **FIFO (First In, First Out)**.

Isso significa que os clientes são atendidos exatamente na ordem em que chegaram, independentemente de sua prioridade.

### Operações implementadas

- `enqueue()` — insere um cliente;
- `dequeue()` — remove o primeiro cliente;
- `head()` — mostra o próximo cliente;
- `size()` — informa o tamanho da fila;
- `empty()` — verifica se a fila está vazia.

### Exemplo

```text
Fila Clássica (FIFO):

Ana → Bruno → Carlos → Daniela → Eduardo

Ordem de atendimento:

Ana
Bruno
Carlos
Daniela
Eduardo
```

---

# 2. Fila Circular

A fila circular possui capacidade limitada de **5 posições**.

Quando o final do vetor é alcançado, a próxima posição volta para o início. Dessa forma, posições liberadas podem ser reutilizadas.

A estrutura utiliza:

- `front` — indica a posição do primeiro cliente;
- `rear` — indica a próxima posição disponível para inserção;
- `quantidade` — quantidade atual de clientes.

### Funcionamento

Inicialmente:

```text
Front: 0
Rear: 0
```

Após inserir cinco clientes:

```text
Front: 0
Rear: 0
Quantidade: 5
```

Depois de remover dois clientes:

```text
Front: 2
Rear: 0
Quantidade: 3
```

As posições liberadas podem então ser reutilizadas por novos clientes.

O `front` e o `rear` avançam de forma circular pelas posições da estrutura.

### Capacidade máxima

Quando as cinco posições estão ocupadas, novos clientes não podem ser inseridos até que uma posição seja liberada.

---

# 3. Fila de Prioridade

A fila de prioridade organiza os clientes de acordo com sua prioridade.

Neste projeto:

```text
Prioridade 1 → Emergência
Prioridade 2 → Prioritário
Prioridade 3 → Normal
```

Quanto **menor o número**, maior a prioridade.

A implementação utiliza `heapq`, formando uma estrutura de **min-heap**.

Quando dois clientes possuem a mesma prioridade, a ordem de chegada é preservada por meio de um contador.

### Exemplo

Entrada:

```text
Ana - Prioridade 3
Bruno - Prioridade 1
Carlos - Prioridade 2
Daniela - Prioridade 1
```

Atendimento:

```text
Bruno - Prioridade 1
Daniela - Prioridade 1
Carlos - Prioridade 2
Ana - Prioridade 3
```

---

# 4. Desafio Final

No desafio final são gerados automaticamente **20 clientes**, cada um recebendo uma prioridade aleatória entre 1 e 3.

Os mesmos clientes são utilizados nas três estruturas para permitir a comparação do comportamento de cada fila.

A fila clássica mantém a ordem de chegada.

A fila circular trabalha com capacidade limitada de 5 posições e reutilização dos espaços liberados.

A fila de prioridade organiza os clientes de acordo com sua prioridade.

---

# Execução

Para executar o sistema completo, utilize:

```bash
python main.py
```

O menu principal apresenta as seguintes opções:

```text
SISTEMA INTELIGENTE DE ATENDIMENTO

1 - Fila Clássica
2 - Fila Circular
3 - Fila de Prioridade
4 - Desafio Final
0 - SAIR
```

---

# Evidências dos testes

## Fila Clássica

A execução demonstra que os clientes são atendidos na mesma ordem em que foram inseridos.

```text
FILA CLÁSSICA (FIFO):

Clientes na ordem de chegada:
Nome: Ana | Senha: A001 | Prioridade: 3
Nome: Bruno | Senha: A002 | Prioridade: 2
Nome: Carlos | Senha: A003 | Prioridade: 1
Nome: Daniela | Senha: A004 | Prioridade: 3
Nome: Eduardo | Senha: A005 | Prioridade: 2
Nome: Fernanda | Senha: A006 | Prioridade: 3
Nome: Gabriel | Senha: A007 | Prioridade: 1
Nome: Helena | Senha: A008 | Prioridade: 2
Nome: Igor | Senha: A009 | Prioridade: 3
Nome: Juliana | Senha: A010 | Prioridade: 1

Tamanho da fila: 10
Próximo cliente: Ana - Senha A001

ORDEM DE ATENDIMENTO:
Atendendo: Ana - Senha A001
Atendendo: Bruno - Senha A002
Atendendo: Carlos - Senha A003
Atendendo: Daniela - Senha A004
Atendendo: Eduardo - Senha A005
Atendendo: Fernanda - Senha A006
Atendendo: Gabriel - Senha A007
Atendendo: Helena - Senha A008
Atendendo: Igor - Senha A009
Atendendo: Juliana - Senha A010

Fila vazia? True
```

---

## Fila Circular

O teste demonstra o preenchimento da capacidade máxima, a remoção de clientes e o reaproveitamento das posições liberadas.

```text
---FILA CIRCULAR---

Inserindo 5 clientes:
Inserido: Ana - Senha C001
Inserido: Bruno - Senha C002
Inserido: Carlos - Senha C003
Inserido: Daniela - Senha C004
Inserido: Eduardo - Senha C005

Estado da fila:
Front: 0 | Rear: 0
Quantidade: 5

Fila: [{'nome': 'Ana', 'senha': 'C001', 'prioridade': 3}, {'nome': 'Bruno', 'senha': 'C002', 'prioridade': 2}, {'nome': 'Carlos', 'senha': 'C003', 'prioridade': 1}, {'nome': 'Daniela', 'senha': 'C004', 'prioridade': 3}, {'nome': 'Eduardo', 'senha': 'C005', 'prioridade': 2}]

Tentando inserir um sexto cliente:
Fila circular cheia!

Removendo dois clientes:
Atendido: Ana - Senha C001
Atendido: Bruno - Senha C002

Estado após as remoções:
Front: 2 | Rear: 0
Quantidade: 3

Fila: [None, None, {'nome': 'Carlos', 'senha': 'C003', 'prioridade': 1}, {'nome': 'Daniela', 'senha': 'C004', 'prioridade': 3}, {'nome': 'Eduardo', 'senha': 'C005', 'prioridade': 2}]

Inserindo novos clientes nas posições liberadas:
Inserido: Fernanda - Senha C006
Inserido: Gabriel - Senha C007

Estado final:
Front: 2 | Rear: 2
Quantidade: 5

Fila: [{'nome': 'Fernanda', 'senha': 'C006', 'prioridade': 1}, {'nome': 'Gabriel', 'senha': 'C007', 'prioridade': 3}, {'nome': 'Carlos', 'senha': 'C003', 'prioridade': 1}, {'nome': 'Daniela', 'senha': 'C004', 'prioridade': 3}, {'nome': 'Eduardo', 'senha': 'C005', 'prioridade': 2}]
```

---

## Fila de Prioridade

O teste demonstra que os clientes são atendidos pela prioridade, começando pela prioridade 1.

```text
FILA DE PRIORIDADE:

Clientes na ordem de chegada:
Nome: Ana | Senha: P001 | Prioridade: 3
Nome: Bruno | Senha: P002 | Prioridade: 2
Nome: Carlos | Senha: P003 | Prioridade: 1
Nome: Daniela | Senha: P004 | Prioridade: 3
Nome: Eduardo | Senha: P005 | Prioridade: 2
Nome: Fernanda | Senha: P006 | Prioridade: 1
Nome: Gabriel | Senha: P007 | Prioridade: 3
Nome: Helena | Senha: P008 | Prioridade: 2
Nome: Igor | Senha: P009 | Prioridade: 1
Nome: Juliana | Senha: P010 | Prioridade: 3

Tamanho da fila: 10

Próximo cliente: Carlos - Senha P003 - Prioridade 1

ORDEM DE ATENDIMENTO:
Atendendo: Carlos - Senha P003 - Prioridade 1
Atendendo: Fernanda - Senha P006 - Prioridade 1
Atendendo: Igor - Senha P009 - Prioridade 1
Atendendo: Bruno - Senha P002 - Prioridade 2
Atendendo: Eduardo - Senha P005 - Prioridade 2
Atendendo: Helena - Senha P008 - Prioridade 2
Atendendo: Ana - Senha P001 - Prioridade 3
Atendendo: Daniela - Senha P004 - Prioridade 3
Atendendo: Gabriel - Senha P007 - Prioridade 3
Atendendo: Juliana - Senha P010 - Prioridade 3

Fila vazia? True
```

---

# Desafio Final — Evidência

O desafio utiliza 20 clientes e aplica as três estruturas de filas.

### Clientes gerados

```text
01. Ana - Prioridade 3
02. Bruno - Prioridade 1
03. Carlos - Prioridade 2
04. Daniela - Prioridade 3
05. Eduardo - Prioridade 3
06. Fernanda - Prioridade 3
07. Gabriel - Prioridade 2
08. Helena - Prioridade 2
09. Igor - Prioridade 1
10. Juliana - Prioridade 1
11. Lucas - Prioridade 1
12. Mariana - Prioridade 1
13. Nicolas - Prioridade 3
14. Olivia - Prioridade 3
15. Paulo - Prioridade 3
16. Rafaela - Prioridade 3
17. Samuel - Prioridade 2
18. Tatiana - Prioridade 2
19. Vinicius - Prioridade 1
20. Yasmin - Prioridade 2
```

### Fila clássica

```text
ATENDIMENTO - FILA CLÁSSICA
Ana - Senha A001 - Prioridade 3
Bruno - Senha A002 - Prioridade 1
Carlos - Senha A003 - Prioridade 2
Daniela - Senha A004 - Prioridade 3
Eduardo - Senha A005 - Prioridade 3
Fernanda - Senha A006 - Prioridade 3
Gabriel - Senha A007 - Prioridade 2
Helena - Senha A008 - Prioridade 2
Igor - Senha A009 - Prioridade 1
Juliana - Senha A010 - Prioridade 1
Lucas - Senha A011 - Prioridade 1
Mariana - Senha A012 - Prioridade 1
Nicolas - Senha A013 - Prioridade 3
Olivia - Senha A014 - Prioridade 3
Paulo - Senha A015 - Prioridade 3
Rafaela - Senha A016 - Prioridade 3
Samuel - Senha A017 - Prioridade 2
Tatiana - Senha A018 - Prioridade 2
Vinicius - Senha A019 - Prioridade 1
Yasmin - Senha A020 - Prioridade 2
```

### Fila circular

Durante o teste, a fila circular atingiu sua capacidade de 5 posições diversas vezes. Após as remoções, as posições liberadas foram reutilizadas.

Exemplos observados durante a execução:

```text
Front: 0
Rear: 0
Quantidade: 5

Front: 2
Rear: 0
Quantidade: 3

Front: 2
Rear: 2
Quantidade: 5

Front: 4
Rear: 2
Quantidade: 3

Front: 4
Rear: 4
Quantidade: 5

Front: 1
Rear: 4
Quantidade: 3
```

A sequência demonstra o comportamento circular, com `front` e `rear` avançando e retornando ao início da estrutura após alcançar a última posição.

Ao final:

```text
Atendendo os clientes restantes:
Atendido: Samuel - Senha C017 - Prioridade 2
Atendido: Tatiana - Senha C018 - Prioridade 2
Atendido: Vinicius - Senha C019 - Prioridade 1
Atendido: Yasmin - Senha C020 - Prioridade 2

Estado final:
Front: 0
Rear: 0
Quantidade: 0
```

### Fila de prioridade

```text
ATENDIMENTO - FILA DE PRIORIDADE
Bruno - Senha P002 - Prioridade 1
Igor - Senha P009 - Prioridade 1
Juliana - Senha P010 - Prioridade 1
Lucas - Senha P011 - Prioridade 1
Mariana - Senha P012 - Prioridade 1
Vinicius - Senha P019 - Prioridade 1
Carlos - Senha P003 - Prioridade 2
Gabriel - Senha P007 - Prioridade 2
Helena - Senha P008 - Prioridade 2
Samuel - Senha P017 - Prioridade 2
Tatiana - Senha P018 - Prioridade 2
Yasmin - Senha P020 - Prioridade 2
Ana - Senha P001 - Prioridade 3
Daniela - Senha P004 - Prioridade 3
Eduardo - Senha P005 - Prioridade 3
Fernanda - Senha P006 - Prioridade 3
Nicolas - Senha P013 - Prioridade 3
Olivia - Senha P014 - Prioridade 3
Paulo - Senha P015 - Prioridade 3
Rafaela - Senha P016 - Prioridade 3
```

---

# Questões da atividade

## 1. Por que a ordem de atendimento pode ser diferente entre a fila clássica e a fila de prioridade?

Na fila clássica, o atendimento segue a ordem de chegada dos clientes (FIFO). Já na fila de prioridade, clientes com maior prioridade são atendidos primeiro. Por isso, um cliente que chegou depois pode ser atendido antes de outro que chegou anteriormente.

## 2. Em quais situações uma fila de prioridade seria mais adequada?

A fila de prioridade é adequada quando alguns clientes precisam ser atendidos antes de outros devido ao seu nível de urgência. Um exemplo é uma unidade hospitalar, onde casos de emergência precisam ser atendidos antes de situações menos urgentes.

## 3. Quais são as vantagens e limitações de uma fila circular?

A principal vantagem é o reaproveitamento das posições que foram liberadas, evitando desperdício de espaço e permitindo o uso contínuo do vetor. Como limitação, a fila possui capacidade definida e não pode receber novos elementos quando todas as posições estão ocupadas.

## 4. O que acontece quando tentamos inserir um elemento em uma fila circular cheia?

Quando a fila circular está cheia, uma nova inserção não pode ser realizada. É necessário remover algum elemento primeiro para liberar uma posição.

---

# Conclusão

O projeto permitiu aplicar na prática diferentes formas de organização de clientes em um sistema de atendimento.

A fila clássica mantém a ordem de chegada, a fila circular permite reutilizar posições liberadas e a fila de prioridade organiza o atendimento de acordo com a prioridade de cada cliente.

Com o desafio final, foi possível observar na prática como o mesmo conjunto de clientes pode apresentar ordens de atendimento diferentes dependendo da estrutura utilizada.
