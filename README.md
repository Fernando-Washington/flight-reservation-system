# ✈️ Fight Reservation System

Um sistema de gerenciamento de voos, passageiros, tripulação e aeronaves, com geração de dados fictícios para simulação.

---

## 📋 Descrição

O projeto simula a criação e gestão de voos aéreos. Ele inclui algumas funcionalidades como:

- Criação de voos aleatórios
- Cadastro automático de tripulação (piloto, copiloto e comissários)
- Geração de passageiros e reservas de assentos
- Cálculo de preços
- Visualização detalhada dos voos com resumo de informações

O sistema utiliza programação orientada a objetos com boas práticas, como abstração, herança e uso de `Enum`.

---

## 📁 Estrutura do Projeto
```
├── classes/
│ ├── airplane.py # Classe Airplane e seus enums
│ ├── airplane_crews.py # Classe AirplaneCrews (herda de Person)
│ ├── colors.py # Códigos de cores ANSI para terminal
│ ├── flight.py # Classe principal que representa um voo
│ ├── passenger.py # Classe Passenger (herda de Person)
│ ├── person.py # Classe abstrata Person
│ ├── price.py # Classe Price (preço por assento)
│ └── seats.py # Classe Seats (gerencia reservas)
├── resources.py # Utilitários: logo, CPF e alguns imports
├── main.py # Script principal para executar o sistema
└── README.md # Documentação do projeto
```


---

## 🏗️ Principais Classes

### `AirplaneCrews`

Representa um membro da tripulação (piloto, copiloto ou comissário).

### `Flight`

O coração do sistema responsável por representar os voos. Permite:

- Adição de passageiros e tripulação
- Visualização de detalhes dos voos
- Resumo com informações como assentos disponíveis e ocupados

### `Airplane`

Contém dados da aeronave, como modelo, alcance (nacional/internacional) e capacidade máxima.

### `Passenger`

Representa um passageiro com nome, CPF e assento reservado.

### `Seats`

Gerencia reserva e cancelamento de assentos.

### `Price`

Associa um valor ao voo com base no ID do voo.

---

## 🔧 Requisitos

- Python 3.8+
- Biblioteca externa:
  - [`Faker`](https://faker.readthedocs.io/en/master/) (`pip install faker`)

---

## ▶️ Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/Fernando-Washington/flight-reservation-system.git
   cd flight-reservation-system
2. Instale as depenências

   ```bash
   pip install faker
3. Execute o sistema:

   ```bash
   python main.py
   
📌 Observações
Todos os dados (nomes, CPFs, etc.) são gerados com a biblioteca Faker e não representam dados reais.

A arquitetura foi pensada para ser modular e extensível.
